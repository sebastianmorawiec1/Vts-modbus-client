"""
Przykład: ciągły monitoring parametrów centrali VTS (odpytywanie cykliczne).

Uruchomienie:
    python examples/monitor.py --interval 5
"""

import argparse
import logging
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from vts_modbus.client import VTSModbusClient
from vts_modbus.config import load_device_config, load_register_map
from vts_modbus.exceptions import VTSModbusError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Monitoring centrali VTS przez Modbus TCP/IP")
    parser.add_argument(
        "--interval", type=float, default=5.0, help="Odstęp między odczytami (sekundy)"
    )
    parser.add_argument(
        "--device-config", default=str(CONFIG_DIR / "device.yaml"), help="Ścieżka do device.yaml"
    )
    parser.add_argument(
        "--registers-config",
        default=str(CONFIG_DIR / "registers_example.yaml"),
        help="Ścieżka do mapy rejestrów",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    device_cfg = load_device_config(args.device_config)
    registers = load_register_map(args.registers_config)

    print(f"Monitoring centrali VTS ({device_cfg.host}:{device_cfg.port}), "
          f"odświeżanie co {args.interval}s. Ctrl+C aby zatrzymać.\n")

    try:
        with VTSModbusClient(device_cfg, registers) as client:
            while True:
                try:
                    values = client.read_all()
                    line = " | ".join(f"{k}={v}" for k, v in values.items())
                    print(line)
                except VTSModbusError as exc:
                    logging.warning("Błąd odczytu cyklu: %s", exc)
                time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nZatrzymano monitoring.")
        return 0
    except VTSModbusError as exc:
        print(f"Błąd połączenia z centralą: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
