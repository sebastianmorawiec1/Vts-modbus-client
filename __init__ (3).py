"""
Przykład: jednorazowy odczyt stanu centrali VTS po Modbus TCP/IP.

Uruchomienie:
    python examples/read_status.py
"""

import logging
import sys
from pathlib import Path

# pozwala uruchamiać przykład bezpośrednio z katalogu examples/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from vts_modbus.client import VTSModbusClient
from vts_modbus.config import load_device_config, load_register_map
from vts_modbus.exceptions import VTSModbusError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"


def main() -> int:
    device_cfg = load_device_config(CONFIG_DIR / "device.yaml")
    registers = load_register_map(CONFIG_DIR / "registers_example.yaml")

    try:
        with VTSModbusClient(device_cfg, registers) as client:
            values = client.read_all()
            print("\nOdczytane parametry centrali VTS:")
            print("-" * 40)
            for name, value in values.items():
                reg = registers[name]
                unit = f" {reg.unit}" if reg.unit else ""
                print(f"{name:28s}: {value}{unit}")
    except VTSModbusError as exc:
        print(f"Błąd komunikacji z centralą: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
