from __future__ import annotations

from beancount.core.data import Account, Directive, Posting, TxnPosting
from beancount.core.display_context import DisplayFormatter
from beancount.core.inventory import Inventory
from typing import Any, Callable, Iterator, TypeVar

_T = TypeVar("_T")

class RealAccount(dict):
    account: Account
    txn_postings: list[Posting]
    balance: Inventory
    def __init__(
        self: RealAccount,
        account_name: Account,
        *args: list[Any],
        **kwargs: dict[str, Any]
    ) -> None: ...
    def __setitem__(self: RealAccount, key: str, value: RealAccount): ...
    def copy(self: RealAccount) -> RealAccount: ...
    def __eq__(self: RealAccount, other: object) -> bool: ...
    def __ne__(self: RealAccount, other: object) -> bool: ...

def iter_children(
    real_account: RealAccount, leaf_only: bool = ...
) -> Iterator[RealAccount]: ...
def get(
    real_account: RealAccount, account_name: Account, default: _T | None = ...
) -> RealAccount | _T: ...
def get_or_create(
    real_account: RealAccount, account_name: Account
) -> RealAccount: ...
def contains(real_account: RealAccount, account_name: Account) -> bool: ...
def realize(
    entries: list[Directive],
    min_accounts: list[Account] | None = ...,
    compute_balance: bool = ...,
) -> RealAccount: ...
def postings_by_account(
    entries: list[Directive],
) -> list[dict[Account, TxnPosting | Directive]]: ...
def filter(
    real_account: RealAccount, predicate: Callable[[RealAccount], bool]
) -> RealAccount: ...
def get_postings(real_account: RealAccount) -> list[Posting | Directive]: ...
def iterate_with_balance(
    txn_postings: list[Posting | Directive],
) -> Iterator[tuple[Directive, list[Posting], Inventory, Inventory]]: ...
def compute_balance(
    real_account: RealAccount, leaf_only: bool = ...
) -> Inventory: ...
def find_last_active_posting(
    txn_postings: list[Posting | Directive],
) -> Directive | None: ...
def index_key(
    sequence: list[_T],
    value: _T,
    key: Callable[[], _T],
    cmp: Callable[[_T, _T], bool],
) -> int | None: ...
def dump(root_account: RealAccount) -> list[tuple[str, str, RealAccount]]: ...

PREFIX_CHILD_1: str
PREFIX_CHILD_C: str
PREFIX_LEAF_1: str
PREFIX_LEAF_C: str

def dump_balances(
    real_root: RealAccount,
    dformat: DisplayFormatter,
    at_cost: bool = ...,
    fullnames: bool = ...,
    file: Any | None = ...,
) -> str | None: ...
def compute_postings_balance(
    txn_postings: list[Posting | Directive],
) -> Inventory: ...
