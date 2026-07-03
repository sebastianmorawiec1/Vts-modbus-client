# PRZYKŁADOWA mapa rejestrów Modbus dla centrali wentylacyjnej VTS.
#
# WAŻNE: Adresy rejestrów poniżej są POGLĄDOWE i służą jako szablon
# struktury pliku. Rzeczywiste adresy, typy danych i skale zależą od
# konkretnego modelu centrali oraz wersji firmware sterownika — sprawdź
# je w dokumentacji Modbus dostarczonej przez producenta / integratora
# i podmień wartości `address` (oraz w razie potrzeby `data_type`, `scale`)
# przed użyciem na produkcyjnym urządzeniu.

temp_nawiew:
  address: 0
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Temperatura powietrza nawiewanego"

temp_wywiew:
  address: 1
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read
  description: "Temperatura powietrza wywiewanego"

temp_zadana:
  address: 2
  table: holding
  data_type: int16
  scale: 0.1
  unit: "°C"
  access: read_write
  description: "Zadana temperatura nawiewu"

wydajnosc_wentylatora:
  address: 10
  table: holding
  data_type: uint16
  scale: 1
  unit: "%"
  access: read_write
  description: "Aktualna wydajność wentylatora nawiewnego/wywiewnego"

tryb_pracy:
  address: 20
  table: holding
  data_type: uint16
  scale: 1
  unit: ""
  access: read_write
  description: "Tryb pracy centrali (0=stop,1=auto,2=ręczny,3=wietrzenie itd. — zweryfikuj)"

status_pracy:
  address: 30
  table: coil
  data_type: bitmask
  access: read
  description: "Stan pracy centrali (włączona/wyłączona)"

alarm_ogolny:
  address: 40
  table: discrete_input
  access: read
  description: "Zbiorczy sygnał alarmowy"

licznik_godzin_pracy:
  address: 50
  table: input
  data_type: uint32
  scale: 1
  unit: "h"
  access: read
  description: "Licznik motogodzin pracy centrali"
