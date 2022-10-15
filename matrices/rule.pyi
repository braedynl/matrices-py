from enum import IntEnum
from typing import Literal, TypeVar, final

__all__ = [
    "Rule",
    "ROW",
    "COL",
]

Self = TypeVar("Self")


@final
class Rule(IntEnum):

    ROW: int = 0
    COL: int = 1

    @property
    def inverse(self: Self) -> Rule: ...
    @property
    def true_name(self: Self) -> Literal["row", "column"]: ...


ROW: Literal[Rule.ROW]
COL: Literal[Rule.COL]