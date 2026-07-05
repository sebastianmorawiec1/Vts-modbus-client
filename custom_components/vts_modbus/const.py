"""Stałe integracji vts_modbus."""

DOMAIN = "vts_modbus"
PLATFORMS = ["sensor", "binary_sensor", "switch", "number"]

CONF_UNIT_ID = "unit_id"
CONF_REGISTERS_FILE = "registers_file"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_APP_CODE = "app_code"

DEFAULT_PORT = 502
DEFAULT_UNIT_ID = 1
DEFAULT_SCAN_INTERVAL = 30  # sekundy
