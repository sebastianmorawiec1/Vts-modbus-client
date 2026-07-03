# vts-modbus-client

Biblioteka i narzędzia w Pythonie do komunikacji z urządzeniami **VTS**
(centrale wentylacyjne / klimatyzacyjne) po protokole **Modbus TCP/IP**.

> ⚠️ **Uwaga dotycząca rejestrów Modbus**
> Adresy rejestrów Modbus (temperatura, wydajność wentylatora, stany pracy,
> alarmy itd.) **różnią się w zależności od modelu centrali VTS oraz wersji
> firmware sterownika**. Plik `config/registers_example.yaml` zawiera
> przykładową, poglądową mapę rejestrów – przed użyciem produkcyjnym należy
> ją zweryfikować i uzupełnić na podstawie dokumentacji Modbus dołączonej do
> konkretnego urządzenia (dostarcza ją producent / integrator VTS).

## Funkcje

- Klient Modbus TCP/IP oparty o `pymodbus` (obsługa read holding/input
  registers, coils, write single/multiple registers).
- Mapowanie rejestrów po nazwie (np. `temp_nawiew`) zamiast surowych adresów,
  konfigurowane w pliku YAML.
- Automatyczne skalowanie wartości (np. dzielenie przez 10 dla temperatur
  w dziesiątych częściach stopnia).
- Obsługa typów danych: `uint16`, `int16`, `uint32`, `int32`, `bitmask`.
- Context manager (`with VTSModbusClient(...) as client:`) z automatycznym
  łączeniem/rozłączeniem.
- Przykłady: jednorazowy odczyt stanu centrali oraz ciągły monitoring.

## Instalacja

```bash
git clone <adres-tego-repo>
cd vts-modbus-client
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Konfiguracja

### 1. Połączenie z urządzeniem — `config/device.yaml`

```yaml
host: 192.168.1.50
port: 502
unit_id: 1          # adres slave / ID urządzenia Modbus
timeout: 3           # sekundy
retries: 3
```

### 2. Mapa rejestrów — `config/registers_example.yaml`

Każdy wpis opisuje jeden parametr centrali:

```yaml
temp_nawiew:
  address: 0            # adres rejestru (0-based, zweryfikuj wg dokumentacji!)
  table: holding         # holding | input | coil | discrete_input
  data_type: int16       # uint16 | int16 | uint32 | int32 | bitmask
  scale: 0.1              # wartość_surowa * scale = wartość rzeczywista
  unit: "°C"
  access: read             # read | write | read_write
  description: "Temperatura nawiewu"
```

Uzupełnij ten plik realnymi adresami z dokumentacji Modbus swojego modelu
centrali VTS (rejestry wentylatorów, przepustnic, nagrzewnicy/chłodnicy,
trybów pracy, alarmów, harmonogramu itd.).

## Szybki start

```python
from vts_modbus.client import VTSModbusClient
from vts_modbus.config import load_device_config, load_register_map

device_cfg = load_device_config("config/device.yaml")
registers = load_register_map("config/registers_example.yaml")

with VTSModbusClient(device_cfg, registers) as client:
    temp = client.read("temp_nawiew")
    print(f"Temperatura nawiewu: {temp} °C")

    client.write("tryb_pracy", 2)  # np. przełączenie trybu pracy
```

Zobacz też gotowe skrypty w `examples/`:

```bash
python examples/read_status.py
python examples/monitor.py --interval 5
```

## Struktura repozytorium

```
vts-modbus-client/
├── vts_modbus/
│   ├── __init__.py
│   ├── client.py        # klient Modbus TCP/IP
│   ├── registers.py      # definicje i dekodowanie rejestrów
│   ├── config.py          # ładowanie configów YAML
│   └── exceptions.py       # wyjątki biblioteki
├── config/
│   ├── device.yaml           # połączenie z centralą
│   └── registers_example.yaml # przykładowa mapa rejestrów
├── examples/
│   ├── read_status.py
│   └── monitor.py
├── custom_components/
│   └── vts_modbus/          # integracja Home Assistant (sensor/binary_sensor/switch/number)
├── tests/
│   └── test_client.py
├── requirements.txt
├── pyproject.toml
└── LICENSE
```

## Testy

```bash
pip install pytest
pytest tests/
```

## Integracja z Home Assistant

Repozytorium zawiera gotową integrację (`custom_components/vts_modbus/`) do
zainstalowania jako **custom integration** w Home Assistant. Udostępnia:

| Rejestry (przykłady)        | Encja HA        | Ilość |
|-----------------------------|-----------------|-------|
| temperatury AI1–AI7, prądy/częstotliwości falowników, `gActOpMode` | `sensor` | 62 |
| alarmy `fAlarm_*`, `GLOBAL_ALARM`, stany DI/przekaźników | `binary_sensor` | 59 |
| `gAlarmAckPRG` (kasowanie alarmów), `gBMS_SummerWinter`, kalendarz | `switch` | 8 |
| `gTSetp_Main`, `gOpMode_BMS`, nastawy wentylatorów Low/Ekono/Komfort | `number` | 47 |

### Instalacja

**Ręcznie:**
1. Skopiuj katalog `custom_components/vts_modbus/` do `<config>/custom_components/vts_modbus/`
   w Twojej instalacji Home Assistant.
2. Zrestartuj Home Assistant.
3. Przejdź do **Ustawienia → Urządzenia i usługi → Dodaj integrację** i wyszukaj
   **VTS Modbus**.
4. Podaj adres IP, port (domyślnie 502), Unit ID oraz interwał odpytywania.
   Opcjonalnie możesz wskazać ścieżkę do własnego pliku `registers.yaml`
   (ten sam format co `config/registers_example.yaml`) — jeśli go nie podasz,
   użyta zostanie wbudowana, przykładowa mapa rejestrów z `const.py`.

**Przez HACS (custom repository):** dodaj to repozytorium jako "Custom repository"
typu *Integration* w HACS, następnie zainstaluj **VTS Modbus** z listy.

### Domyślna mapa rejestrów

Integracja zawiera wbudowaną, pełną mapę **176 rejestrów** dla sterowników
VTS typu **VS...uPC z modułem rozszerzeń Carel TCP/IP**
(`custom_components/vts_modbus/registers_vts_carel_tcpip.yaml`), opracowaną
na podstawie oficjalnej instrukcji VTS. Jeśli Twoja centrala ma inny
sterownik, przygotuj własny plik `registers.yaml` i wskaż go w polu
"Ścieżka do własnego pliku registers.yaml" podczas konfiguracji integracji.

Uwaga na adresowanie: pola `address` odpowiadają kolumnie "Modbus Index"
z dokumentacji. Jeśli po uruchomieniu odczyty będą przesunięte o jeden
rejestr, odejmij 1 od wszystkich adresów w pliku YAML.

### Jak to działa

- `coordinator.py` — `DataUpdateCoordinator` cyklicznie odczytuje wszystkie
  skonfigurowane rejestry (domyślnie co 30 s) w osobnym wątku
  (`async_add_executor_job`), żeby nie blokować pętli zdarzeń HA.
- Zapis wartości z encji `number`/`switch` wywołuje
  `coordinator.async_write_register()`, które zapisuje rejestr i od razu
  wymusza odświeżenie danych.
- Każda centrala VTS pojawia się w HA jako jedno urządzenie (`DeviceInfo`)
  grupujące wszystkie powiązane encje.

## Rozwój / TODO

- [ ] Uzupełnić `registers_example.yaml` o pełną, potwierdzoną mapę rejestrów
      dla konkretnych modeli VTS (np. WING, VS-xx, VP-xx).
- [ ] Dodać obsługę zapisu wielu rejestrów naraz (`write_multiple`).
- [ ] Dodać eksport odczytów do MQTT / bazy danych (InfluxDB, Prometheus).
- [ ] Obsługa reconnect przy zerwaniu połączenia TCP.

## Licencja

MIT — patrz [LICENSE](LICENSE).
