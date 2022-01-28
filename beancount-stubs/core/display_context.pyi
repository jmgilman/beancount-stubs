from __future__ import annotations

import enum

from beancount.core.data import Currency
from beancount.core.distribution import Distribution
from decimal import Decimal
from typing import Callable, Optional

class Precision(enum.Enum):
    MOST_COMMON: int
    MAXIMUM: int

class Align(enum.Enum):
    NATURAL: int
    DOT: int
    RIGHT: int

class _CurrencyContext:
    has_sign: bool
    integer_max: int
    fractional_dist: Distribution
    def __init__(self: _CurrencyContext) -> None: ...
    def update(self: _CurrencyContext, number: Decimal) -> None: ...
    def get_fractional(
        self: _CurrencyContext, precision: Precision
    ) -> int: ...

class DisplayContext:
    ccontexts: dict[Currency, _CurrencyContext]
    commas: bool
    def __init__(self: DisplayContext) -> None: ...
    def set_commas(self: DisplayContext, commas: bool) -> None: ...
    def update(
        self: DisplayContext, number: Decimal, currency: Currency = ...
    ) -> None: ...
    def quantize(
        self, number: Decimal, currency: Currency, precision: Precision = ...
    ) -> Decimal: ...
    def build(
        self,
        alignment: Align = ...,
        precision: Precision = ...,
        commas: Optional[bool] = ...,
        reserved: int = ...,
    ): ...
    DEFAULT_UNINITIALIZED_PRECISION: int

class DisplayFormatter:
    dcontext: DisplayContext
    precision: Precision
    fmtstrings: dict[Currency, str]
    fmtfuncs: dict[Currency, Callable]
    def __init__(
        self: DisplayFormatter,
        dcontext: DisplayContext,
        precision: Precision,
        fmtstrings: dict[Currency, str],
    ) -> None: ...
    def format(
        self: DisplayFormatter, number: Decimal, currency: Currency = ...
    ) -> Callable: ...
    def quantize(
        self: DisplayFormatter, number: Decimal, currency: Currency = ...
    ) -> Decimal: ...
    __call__: Callable[[DisplayFormatter, Decimal, Currency], Callable]

DEFAULT_DISPLAY_CONTEXT: DisplayContext
DEFAULT_FORMATTER: DisplayFormatter
