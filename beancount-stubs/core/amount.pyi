from __future__ import annotations

from beancount.core.display_context import DisplayContext
from decimal import Decimal
from tokenize import Name
from typing import (
    Any,
    Callable,
    Optional,
)

CURRENCY_RE: str

class Amount:
    currency: str
    number: Optional[Decimal]
    valid_types_number: tuple
    valid_types_currency: tuple
    def __new__(cls, number: Decimal, currency: str) -> Amount: ...
    def to_string(self: Amount, dformat: DisplayContext = ...) -> str: ...
    def __bool__(self: Amount) -> bool: ...
    def __eq__(self: Amount, other: object) -> bool: ...
    def __lt__(self: Amount, other: object) -> bool: ...
    def __hash__(self: Amount) -> int: ...
    def __neg__(self: Amount) -> Amount: ...
    def _replace(self: Amount, /, **kwargs) -> Amount: ...
    def _asdict(self: Amount) -> dict[str, Any]: ...
    @staticmethod
    def from_string(string: str) -> Amount: ...

def sortkey(amount: Amount) -> tuple[str, Decimal]: ...
def mul(amount: Amount, number: Decimal) -> Amount: ...
def div(amount: Amount, number: Decimal) -> Amount: ...
def add(amount1: Amount, amount2: Amount) -> Amount: ...
def sub(amount1: Amount, amount2: Amount) -> Amount: ...
def abs(amount: Amount) -> Amount: ...

from_string: Callable[[str], Amount]
NULL_AMOUNT: Amount
