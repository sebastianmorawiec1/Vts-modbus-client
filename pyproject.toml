"""
Definicje rejestrów Modbus oraz logika kodowania/dekodowania wartości.

Adresy i typy rejestrów są specyficzne dla modelu centrali VTS i sterownika –
wartości podane w config/registers_example.yaml są PRZYKŁADOWE i wymagają
weryfikacji z dokumentacją Modbus producenta.
"""

from dataclasses import dataclass
from typing import Any, Dict, Literal

TableType = Literal["holding", "input", "coil", "discrete_input"]
DataType = Literal["uint16", "int16", "uint32", "int32", "bitmask"]
AccessType = Literal["read", "write", "read_write"]


@dataclass
class RegisterDefinition:
    name: str
    address: int
    table: TableType = "holding"
    data_type: DataType = "uint16"
    scale: float = 1.0
    unit: str = ""
    access: AccessType = "read"
    description: str = ""

    @property
    def register_count(self) -> int:
        """Ile 16-bitowych rejestrów zajmuje ta wartość."""
        return 2 if self.data_type in ("uint32", "int32") else 1

    @classmethod
    def from_dict(cls, name: str, data: Dict[str, Any]) -> "RegisterDefinition":
        return cls(
            name=name,
            address=int(data["address"]),
            table=data.get("table", "holding"),
            data_type=data.get("data_type", "uint16"),
            scale=float(data.get("scale", 1.0)),
            unit=data.get("unit", ""),
            access=data.get("access", "read"),
            description=data.get("description", ""),
        )

    def decode(self, raw_registers) -> Any:
        """Dekoduje surowe słowa (16-bit) na wartość Pythona."""
        if self.data_type == "uint16":
            value = raw_registers[0]
        elif self.data_type == "int16":
            value = raw_registers[0]
            if value >= 0x8000:
                value -= 0x10000
        elif self.data_type in ("uint32", "int32"):
            # big-endian word order (high, low) — zweryfikuj wg dokumentacji
            high, low = raw_registers[0], raw_registers[1]
            value = (high << 16) | low
            if self.data_type == "int32" and value >= 0x80000000:
                value -= 0x100000000
        elif self.data_type == "bitmask":
            return raw_registers[0]  # zwracamy surową maskę bitową
        else:
            raise ValueError(f"Nieobsługiwany data_type: {self.data_type}")

        if self.scale != 1.0:
            value = round(value * self.scale, 6)
        return value

    def encode(self, value: Any):
        """Koduje wartość Pythona na listę słów (16-bit) do zapisu."""
        if self.scale != 1.0:
            value = int(round(value / self.scale))
        else:
            value = int(value)

        if self.data_type in ("uint16", "bitmask"):
            return [value & 0xFFFF]
        if self.data_type == "int16":
            if value < 0:
                value += 0x10000
            return [value & 0xFFFF]
        if self.data_type in ("uint32", "int32"):
            if value < 0:
                value += 0x100000000
            high = (value >> 16) & 0xFFFF
            low = value & 0xFFFF
            return [high, low]

        raise ValueError(f"Nieobsługiwany data_type: {self.data_type}")
