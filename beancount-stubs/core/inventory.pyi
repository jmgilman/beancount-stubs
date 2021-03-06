from __future__ import annotations

from decimal import Decimal
import enum
from turtle import pos

from beancount.core.amount import Amount
from beancount.core.data import Currency
from beancount.core.display_context import DisplayFormatter
from beancount.core.position import Cost, Position
from typing import Any, Callable, Iterable, Iterator, Optional

ASSERTS_TYPES: bool

class MatchResult(enum.Enum):
    CREATED: int
    REDUCED: int
    AUGMENTED: int
    IGNORED: int

class Inventory(dict):
    def __init__(
        self: Inventory,
        positions: list[Position] | dict[Any, Any] | None = ...,
    ) -> None: ...
    def __iter__(self: Inventory) -> Iterator[Position]: ...
    def __lt__(self: Inventory, other: object) -> bool: ...
    def to_string(
        self: Inventory, dformat: DisplayFormatter = ..., parens: bool = ...
    ) -> str: ...
    def is_empty(self: Inventory) -> bool: ...
    def __bool__(self: Inventory) -> None: ...
    def __copy__(self: Inventory) -> Inventory: ...
    def is_small(self: Inventory, tolerances: Decimal) -> bool: ...
    def is_mixed(self: Inventory) -> bool: ...
    def is_reduced_by(self: Inventory, ramount: Amount) -> bool: ...
    def __neg__(self: Inventory) -> Inventory: ...
    def __abs__(self: Inventory) -> Inventory: ...
    def __mul__(self, scalar: Decimal) -> Inventory: ...
    def currencies(self: Inventory) -> set[Currency]: ...
    def cost_currencies(self: Inventory) -> set[Currency]: ...
    def currency_pairs(self: Inventory) -> set[Currency]: ...
    def get_positions(self: Inventory) -> list[Position]: ...
    def get_only_position(self: Inventory) -> Optional[Position]: ...
    def get_currency_units(self: Inventory, currency: Currency) -> Amount: ...
    def segregate_units(
        self, currencies: list[Currency]
    ) -> dict[Currency, Inventory]: ...
    def split(self: Inventory) -> dict[Currency, Inventory]: ...
    def reduce(
        self: Inventory, reducer: Callable, *args: list[Any]
    ) -> Inventory: ...
    def average(self: Inventory) -> Inventory: ...
    def add_amount(
        self: Inventory, units: Amount, cost: Cost | None = ...
    ) -> tuple[Position, MatchResult]: ...
    def add_position(
        self: Inventory, position: Position
    ) -> tuple[Position, MatchResult]: ...
    def add_inventory(self: Inventory, other: Inventory) -> Inventory: ...
    def __add__(self: Inventory, other: Inventory) -> Inventory: ...
    __iadd__: Callable[[Inventory, Inventory], Inventory]
    @staticmethod
    def from_string(string: str) -> Inventory: ...

from_string: Callable[[str], Inventory]

def check_invariants(inv: Inventory) -> None: ...
