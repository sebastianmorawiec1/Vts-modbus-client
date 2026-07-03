{
  "config": {
    "step": {
      "user": {
        "title": "Połączenie z centralą VTS (Modbus TCP/IP)",
        "data": {
          "host": "Adres IP / host",
          "port": "Port",
          "unit_id": "Unit ID (adres slave)",
          "scan_interval": "Interwał odpytywania (s)",
          "registers_file": "Ścieżka do własnego pliku registers.yaml (opcjonalnie)"
        }
      }
    },
    "error": {
      "cannot_connect": "Nie udało się połączyć z urządzeniem. Sprawdź adres IP i port.",
      "invalid_registers_file": "Nie udało się wczytać pliku z mapą rejestrów.",
      "unknown": "Wystąpił nieoczekiwany błąd."
    },
    "abort": {
      "already_configured": "To urządzenie jest już skonfigurowane."
    }
  }
}
