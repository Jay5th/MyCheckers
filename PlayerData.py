from dataclasses import dataclass


@dataclass(frozen=True)
class PlayerData:
    id: int
    color: str
