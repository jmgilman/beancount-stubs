from __future__ import annotations

from beancount.core.data import Currency
from beancount.core.display_context import DisplayFormatter
from decimal import Decimal
from typing import Any, Callable, NamedTuple

def numberify_results(
    dtypes: list[tuple[str, type]],
    drows: list[NamedTuple],
    dformat: DisplayFormatter | None = ...,
) -> tuple[list[tuple[str, type]], list[NamedTuple]]: ...

class IdentityConverter:
    name: str
    dtype: type
    index: int
    def __init__(
        self: IdentityConverter, name: str, dtype: type, index: int
    ) -> None: ...
    def __call__(self: IdentityConverter, drow: list[Any], _) -> Any: ...

class AmountConverter:
    dtype: Decimal
    name: str
    index: int
    currency: Currency
    def __init__(
        self: AmountConverter, name: str, index: int, currency: Currency
    ) -> None: ...
    def __call__(
        self: AmountConverter, drow: list[Any], dformat: DisplayFormatter
    ) -> Decimal | None: ...

def convert_col_Amount(
    name: str, drows: list[Any], index: int
) -> list[AmountConverter]: ...

class PositionConverter:
    dtype: Decimal
    name: str
    index: int
    currency: Currency
    def __init__(
        self: PositionConverter, name: str, index: int, currency: Currency
    ) -> None: ...
    def __call__(
        self: PositionConverter, drow: list[Any], dformat: DisplayFormatter
    ) -> Decimal | None: ...

def convert_col_Position(
    name: str, drows: list[Any], index: int
) -> list[PositionConverter]: ...

class InventoryConverter:
    dtype: Decimal
    name: str
    index: int
    currency: Currency
    def __init__(
        self: InventoryConverter, name: str, index: int, currency: Currency
    ) -> None: ...
    def __call__(
        self: InventoryConverter, drow: list[Any], dformat: DisplayFormatter
    ) -> Decimal | None: ...

def convert_col_Inventory(
    name: str, drows: list[Any], index: int
) -> list[InventoryConverter]: ...

CONVERTING_TYPES: dict[type, Callable[[str, list[Any], int], list]]
