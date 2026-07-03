"""Ładowanie plików konfiguracyjnych YAML (połączenie i mapa rejestrów)."""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Union

import yaml

from .registers import RegisterDefinition


@dataclass
class DeviceConfig:
    host: str
    port: int = 502
    unit_id: int = 1
    timeout: float = 3.0
    retries: int = 3


def load_device_config(path: Union[str, Path]) -> DeviceConfig:
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    return DeviceConfig(
        host=data["host"],
        port=int(data.get("port", 502)),
        unit_id=int(data.get("unit_id", 1)),
        timeout=float(data.get("timeout", 3.0)),
        retries=int(data.get("retries", 3)),
    )


def load_register_map(path: Union[str, Path]) -> Dict[str, RegisterDefinition]:
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    registers: Dict[str, RegisterDefinition] = {}
    for name, cfg in data.items():
        registers[name] = RegisterDefinition.from_dict(name, cfg)
    return registers
