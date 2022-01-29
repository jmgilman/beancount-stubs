from __future__ import annotations

from beancount.core.data import Account
from typing import Any

class AccountTypes:
    assets: str
    liabilities: str
    equity: str
    income: str
    expenses: str
    def __new__(
        cls,
        assets: str,
        equity: str,
        income: str,
        expenses: str,
    ) -> AccountTypes: ...
    def _replace(self: AccountTypes) -> AccountTypes: ...
    def _asdict(self: AccountTypes) -> dict[str, Any]: ...

DEFAULT_ACCOUNT_TYPES: AccountTypes

def get_account_sort_key(
    account_types: AccountTypes, account_name: Account
) -> tuple[str, Account]: ...
def get_account_type(account_name: Account) -> str: ...
def is_account_type(account_type: str, account_name: Account) -> bool: ...
def is_root_account(account_name: Account) -> bool: ...
def is_balance_sheet_account(
    account_name: Account, account_types: AccountTypes
) -> bool: ...
def is_income_statement_account(
    account_name: Account, account_types: AccountTypes
) -> bool: ...
def is_equity_account(
    account_name: Account, account_types: AccountTypes
) -> bool: ...
def is_inverted_account(
    account_name: Account, account_types: AccountTypes
) -> bool: ...
def get_account_sign(
    account_name: Account, account_types: AccountTypes | None = ...
) -> int: ...
