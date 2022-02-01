from __future__ import annotations

import datetime

from beancount.core.data import (
    Account,
    Close,
    Commodity,
    Currency,
    Directive,
    Open,
    Posting,
    Transaction,
)
from beancount.core.inventory import Inventory
from beancount.query.query_compile import (
    EvalFrom,
    EvalNode,
    EvalPrint,
    EvalQuery,
)
from decimal import Decimal
from typing import Any, Optional, IO

def filter_entries(
    c_from: Optional[EvalFrom],
    entries: list[Directive],
    options_map: dict[str, Any],
    context: RowContext,
) -> list[Directive]: ...
def execute_print(
    c_print: EvalPrint,
    entries: list[Directive],
    options_map: dict[str, Any],
    file: IO,
) -> None: ...

class Allocator:
    size: int
    def __init__(self: Allocator) -> None: ...
    def allocate(self: Allocator) -> int: ...
    def create_store(self: Allocator) -> list[None]: ...

class RowContext:
    posting: Posting
    entry: Transaction
    balance: Inventory
    options_map: dict[str, Any]
    account_types: tuple
    open_close_map: dict[Account, tuple[Open, Close]]
    commodity_map: dict[Currency, Commodity]
    price_map: dict[tuple[Currency, Currency], tuple[datetime.date, Decimal]]

def uses_balance_column(c_expr: EvalNode) -> bool: ...
def row_sortkey(
    order_indexes: list[int], values: list[Any], c_exprs: list[EvalNode]
) -> tuple: ...
def create_row_context(
    entries: list[Directive], options_map: dict[str, Any]
) -> RowContext: ...
def execute_query(
    query: EvalQuery, entries: list[Directive], options_map: dict[str, Any]
) -> tuple[list[tuple[str, type]], list[Any]]: ...
def flatten_results(
    result_types: list[tuple[str, type]], result_rows: list[Any]
) -> tuple[list[tuple[str, type]], list[Any]]: ...
