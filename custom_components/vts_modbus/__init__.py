"""Integracja VTS Modbus dla Home Assistant."""

from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_PORT, Platform
from homeassistant.core import HomeAssistant

from pathlib import Path

from .const import (
    CONF_REGISTERS_FILE,
    CONF_SCAN_INTERVAL,
    CONF_UNIT_ID,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
)
from .coordinator import VTSModbusCoordinator
from .registers import load_registers_from_yaml


def entry_slug(entry: ConfigEntry) -> str:
    """Stabilny prefiks entity_id na podstawie hosta, np. vts_192_168_1_60."""
    host = str(entry.data.get(CONF_HOST, "vts")).lower()
    return "vts_" + "".join(ch if ch.isalnum() else "_" for ch in host)

# Domyślna mapa rejestrów: pełna mapa z oficjalnej dokumentacji VTS dla
# modułu rozszerzeń Carel TCP/IP (sterowniki VS...uPC), dołączona do integracji.
BUNDLED_REGISTERS_FILE = Path(__file__).parent / "registers_vts_carel_tcpip.yaml"

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.SWITCH,
    Platform.NUMBER,
]


CARD_URL = "/vts_modbus/vts-ahu-card.js"
_CARD_REGISTERED = False


async def _register_card(hass: HomeAssistant) -> None:
    """Serwuje karte Lovelace vts-ahu-card.js i dodaje ja do frontendu."""
    global _CARD_REGISTERED
    if _CARD_REGISTERED:
        return
    from homeassistant.components.http import StaticPathConfig
    from homeassistant.components.frontend import add_extra_js_url

    card_path = str(Path(__file__).parent / "vts-ahu-card.js")
    await hass.http.async_register_static_paths(
        [StaticPathConfig(CARD_URL, card_path, False)]
    )
    add_extra_js_url(hass, CARD_URL)
    _CARD_REGISTERED = True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    await _register_card(hass)
    data = entry.data

    registers_file = data.get(CONF_REGISTERS_FILE) or str(BUNDLED_REGISTERS_FILE)
    registers = await hass.async_add_executor_job(load_registers_from_yaml, registers_file)

    coordinator = VTSModbusCoordinator(
        hass,
        host=data[CONF_HOST],
        port=data[CONF_PORT],
        unit_id=data[CONF_UNIT_ID],
        registers=registers,
        scan_interval=data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL),
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unloaded:
        coordinator: VTSModbusCoordinator = hass.data[DOMAIN].pop(entry.entry_id)
        await hass.async_add_executor_job(coordinator.close)
    return unloaded
