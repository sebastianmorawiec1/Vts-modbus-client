"""Stałe integracji vts_modbus."""

DOMAIN = "vts_modbus"
PLATFORMS = ["sensor", "binary_sensor", "switch", "number"]

CONF_UNIT_ID = "unit_id"
CONF_REGISTERS_FILE = "registers_file"
CONF_SCAN_INTERVAL = "scan_interval"

DEFAULT_PORT = 502
DEFAULT_UNIT_ID = 1
DEFAULT_SCAN_INTERVAL = 30  # sekundy

# UWAGA: poniższa mapa rejestrów jest PRZYKŁADOWA (placeholder). Rzeczywiste
# adresy zależą od modelu centrali VTS i wersji sterownika — zweryfikuj je
# w dokumentacji Modbus swojego urządzenia. Możesz je nadpisać, podając
# własny plik YAML w polu "registers_file" podczas konfiguracji integracji
# (format identyczny jak config/registers_example.yaml w repozytorium).
DEFAULT_REGISTERS = {
    "temp_nawiew": {
        "address": 0,
        "table": "holding",
        "data_type": "int16",
        "scale": 0.1,
        "unit": "°C",
        "access": "read",
        "description": "Temperatura powietrza nawiewanego",
        "device_class": "temperature",
    },
    "temp_wywiew": {
        "address": 1,
        "table": "holding",
        "data_type": "int16",
        "scale": 0.1,
        "unit": "°C",
        "access": "read",
        "description": "Temperatura powietrza wywiewanego",
        "device_class": "temperature",
    },
    "temp_zadana": {
        "address": 2,
        "table": "holding",
        "data_type": "int16",
        "scale": 0.1,
        "unit": "°C",
        "access": "read_write",
        "description": "Zadana temperatura nawiewu",
        "device_class": "temperature",
        "min": 10.0,
        "max": 30.0,
        "step": 0.5,
    },
    "wydajnosc_wentylatora": {
        "address": 10,
        "table": "holding",
        "data_type": "uint16",
        "scale": 1,
        "unit": "%",
        "access": "read_write",
        "description": "Wydajność wentylatora nawiewnego/wywiewnego",
        "min": 0,
        "max": 100,
        "step": 5,
    },
    "tryb_pracy": {
        "address": 20,
        "table": "holding",
        "data_type": "uint16",
        "scale": 1,
        "unit": "",
        "access": "read_write",
        "description": "Tryb pracy centrali (0=stop,1=auto,2=ręczny,3=wietrzenie — zweryfikuj)",
        "min": 0,
        "max": 3,
        "step": 1,
    },
    "status_pracy": {
        "address": 30,
        "table": "coil",
        "data_type": "bitmask",
        "access": "read_write",
        "description": "Stan pracy centrali (włączona/wyłączona)",
    },
    "alarm_ogolny": {
        "address": 40,
        "table": "discrete_input",
        "access": "read",
        "description": "Zbiorczy sygnał alarmowy",
    },
    "licznik_godzin_pracy": {
        "address": 50,
        "table": "input",
        "data_type": "uint32",
        "scale": 1,
        "unit": "h",
        "access": "read",
        "description": "Licznik motogodzin pracy centrali",
        "state_class": "total_increasing",
    },
}
