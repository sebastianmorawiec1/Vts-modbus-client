"""Platforma sensor dla VTS Modbus."""

from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import CONF_APP_CODE, DOMAIN
from .coordinator import VTSModbusCoordinator
from .vts_code import InvalidAppCode, decode_app_code
from . import entry_slug


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    coordinator: VTSModbusCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities = [
        VTSSensor(coordinator, entry, name)
        for name, reg in coordinator.registers.items()
        if reg.table in ("holding", "input") and reg.access == "read"
    ]
    app_code = entry.data.get(CONF_APP_CODE)
    if app_code:
        entities.append(VTSAppCodeSensor(coordinator, entry, app_code))
    async_add_entities(entities)


class VTSAppCodeSensor(CoordinatorEntity[VTSModbusCoordinator], SensorEntity):
    """Sensor diagnostyczny: kod aplikacji VTS + zdekodowana konfiguracja."""

    _attr_has_entity_name = True
    _attr_icon = "mdi:barcode"

    def __init__(self, coordinator: VTSModbusCoordinator, entry: ConfigEntry, code: str) -> None:
        super().__init__(coordinator)
        self._code = code
        self._attr_unique_id = f"{entry.entry_id}_app_code"
        self.entity_id = f"sensor.{entry_slug(entry)}_app_code"
        self._attr_name = "Kod aplikacji"
        try:
            self._decoded = decode_app_code(code)
        except InvalidAppCode:
            self._decoded = {"code": code, "error": "invalid"}
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name=entry.title,
            manufacturer="VTS",
            model="Centrala wentylacyjna (Modbus TCP/IP)",
        )

    @property
    def native_value(self):
        return self._decoded.get("code", self._code)

    @property
    def extra_state_attributes(self):
        return self._decoded


class VTSSensor(CoordinatorEntity[VTSModbusCoordinator], SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator: VTSModbusCoordinator, entry: ConfigEntry, name: str) -> None:
        super().__init__(coordinator)
        self._name = name
        reg = coordinator.registers[name]

        self._attr_unique_id = f"{entry.entry_id}_{name}"
        self.entity_id = f"sensor.{entry_slug(entry)}_{name.lower()}"
        self._attr_translation_key = name
        self._attr_name = reg.description or name
        self._attr_native_unit_of_measurement = reg.unit or None
        self._attr_device_class = reg.device_class
        self._attr_state_class = reg.state_class
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name=entry.title,
            manufacturer="VTS",
            model="Centrala wentylacyjna (Modbus TCP/IP)",
        )

    @property
    def native_value(self):
        return self.coordinator.data.get(self._name)
