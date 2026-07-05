"""Dekoder kodu aplikacji VTS "Automatyka 2019" (np. AP11000000610000101).

Kod: 2 litery + ciag cyfr. Litera okresla typ centrali/odzysku:
  AS = Supply (tylko nawiew)
  AD = Supply&Exhaust (bez odzysku)
  AR = S/E + wymiennik obrotowy (rotary wheel)
  AG = S/E + glikol
  AP = S/E + wymiennik krzyzowy (plate cross)
  AE = Exhaust (tylko wywiew)

UWAGA: pozycje cyfr (POSITIONS) odwzorowano z diagramu "Automatyka 2019 -
Kodowanie" najlepiej jak sie dalo; w razie rozbieznosci z dokumentacja
zaktualizuj slownik POSITIONS (1-indeksowane pozycje w ciagu cyfr) - ta sama
mapa jest powielona w vts-ahu-card.js (DIGITS).
"""

from __future__ import annotations

from typing import Any, Dict

LETTER_CODES = {
    "AS": "supply",
    "AD": "supply_exhaust",
    "AR": "rotary",
    "AG": "glycol",
    "AP": "plate_cross",
    "AE": "exhaust",
}

# 1-indeksowane pozycje cyfr w kodzie (po literach)
POSITIONS = {
    "recovery_mode": 1,      # 0=none 1=Winter 2=Summer 3=Winter+Summer
    "redundant": 2,          # 0/1
    "main_heater": 3,        # 0=none 1=hot water 2=DX 3=electric 4=steam
    "main_cooler": 4,        # 0=none 1=chilled water 2=DX
    "rev_heater_cooler": 5,  # 0=none 1=hydronic 2=DX
    "pre_heater": 6,         # 0=none 1=hot water 2=DX 3=electric
    "re_heater": 7,          # 0=none 1=hot water 2=DX 3=electric
    "fn_total": 8,           # 0/1
    "upc3_config": 9,        # 0=brak HMI Basic 3=HMI Basic 6=none
    "ch_base": 10,           # 0/1
    "no_bypass": 11,         # 0/1 (1 = odzysk bez by-passu)
    "economizer": 12,        # 0/1 (przepustnica recyrkulacji / komora mieszania)
    "fast_heating": 13,     # 0/1
    "humidifier": 14,        # 0=none 1=evaporative 2=steam
    "drct": 15,              # 0/1
}


class InvalidAppCode(ValueError):
    """Kod aplikacji ma nieprawidlowy format."""


def decode_app_code(code: str) -> Dict[str, Any]:
    """Dekoduje kod aplikacji do slownika cech centrali."""
    code = (code or "").strip().upper().replace(" ", "").replace("-", "")
    if len(code) < 4 or not code[:2].isalpha() or not code[2:].isdigit():
        raise InvalidAppCode(f"Nieprawidlowy kod aplikacji: '{code}'")

    letter = code[:2]
    if letter not in LETTER_CODES:
        raise InvalidAppCode(f"Nieznana litera kodu: '{letter}' (oczekiwano {list(LETTER_CODES)})")

    digits = code[2:]
    result: Dict[str, Any] = {
        "code": code,
        "letter": letter,
        "unit_type": LETTER_CODES[letter],
        "has_supply": letter != "AE",
        "has_exhaust": letter not in ("AS",),
        "recovery": LETTER_CODES[letter] if letter in ("AR", "AG", "AP") else "none",
    }
    for key, pos in POSITIONS.items():
        result[key] = int(digits[pos - 1]) if pos <= len(digits) else 0

    result["has_bypass"] = result["recovery"] != "none" and result["no_bypass"] == 0
    return result
