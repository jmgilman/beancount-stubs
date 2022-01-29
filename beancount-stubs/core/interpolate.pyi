from __future__ import annotations

import datetime

from beancount.core.data import (
    Account,
    Currency,
    Directive,
    Posting,
    Transaction,
)
from beancount.core.inventory import Inventory
from decimal import Decimal
from typing import Any

MAXIMUM_TOLERANCE: Decimal
MAX_TOLERANCE_DIGITS: int

def is_tolerance_user_specified(tolerance: Decimal) -> bool: ...

class BalanceError:
    source: Any
    message: str
    entry: Directive
    def __new__(
        cls,
        source: Any,
        equity: str,
        message: str,
        entry: Directive,
    ) -> BalanceError: ...
    def _replace(self: BalanceError) -> BalanceError: ...
    def _asdict(self: BalanceError) -> dict[str, Any]: ...

def has_nontrivial_balance(posting: Posting) -> bool: ...
def compute_residual(postings: list[Posting]) -> Inventory: ...
def infer_tolerances(
    postings: list[Posting],
    options_map: dict[str, str],
    use_cost: bool | None = ...,
) -> dict[Currency, Decimal]: ...

AUTOMATIC_META: str
AUTOMATIC_RESIDUAL: str
AUTOMATIC_TOLERANCES: str

def get_residual_postings(
    residual: Inventory, account_rounding: Account
) -> list[Posting]: ...
def fill_residual_posting(
    entry: Transaction, account_rounding: Account
) -> Transaction: ...
def compute_entries_balance(
    entries: list[Directive],
    prefix: str | None = ...,
    date: datetime.date | None = ...,
) -> Inventory: ...
def compute_entry_context(
    entries: list[Directive],
    context_entry: Directive,
    additional_accounts: list[Account] | None = ...,
) -> tuple[dict[Account, Inventory], dict[Account, Inventory]]: ...
def quantize_with_tolerance(
    tolerances: dict[Currency, Decimal], currency: Currency, number: Decimal
) -> Decimal: ...
