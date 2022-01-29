from __future__ import annotations

import datetime
import enum

from beancount.core.amount import Amount
from beancount.core.position import Cost, CostSpec
from decimal import Decimal
from typing import (
    Any,
    Iterator,
    Optional,
    Union,
)
from typing_extensions import TypeAlias

Account: TypeAlias = str
Currency: TypeAlias = str
Flag: TypeAlias = str
Meta: TypeAlias = dict[str, Any]
EMPTY_SET: frozenset

class Booking(enum.Enum):
    STRICT: str
    NONE: str
    AVERAGE: str
    FIFO: str
    LIFO: str

class Open:
    meta: Meta
    date: datetime.date
    account: Account
    currencies: list[Currency]
    booking: Optional[Booking]
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        account: Account,
        currencies: list[Currency],
        booking: Optional[Booking],
    ) -> Open: ...
    def _replace(self: Open) -> Open: ...
    def _asdict(self: Open) -> dict[str, Any]: ...

class Close:
    meta: Meta
    date: datetime.date
    account: Account
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        account: Account,
    ) -> Close: ...
    def _replace(self: Close) -> Close: ...
    def _asdict(self: Close) -> dict[str, Any]: ...

class Commodity:
    meta: Meta
    date: datetime.date
    currency: Currency
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        currency: Currency,
    ) -> Commodity: ...
    def _replace(self: Commodity) -> Commodity: ...
    def _asdict(self: Commodity) -> dict[str, Any]: ...

class Pad:
    meta: Meta
    date: datetime.date
    account: Account
    source_account: Account
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        account: Account,
        source_account: Account,
    ) -> Pad: ...
    def _replace(self: Pad) -> Pad: ...
    def _asdict(self: Pad) -> dict[str, Any]: ...

class Balance:
    meta: Meta
    date: datetime.date
    account: Account
    amount: Amount
    tolerance: Optional[Decimal]
    diff_amount: Optional[Amount]
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        account: Account,
        amount: Amount,
        tolerance: Optional[Decimal],
        diff_amount: Optional[Amount],
    ) -> Balance: ...
    def _replace(self: Balance) -> Balance: ...
    def _asdict(self: Balance) -> dict[str, Any]: ...

class Posting:
    account: Account
    units: Amount
    cost: Optional[Union[Cost, CostSpec]]
    price: Optional[Amount]
    flag: Optional[Flag]
    meta: Optional[Meta]
    def __new__(
        cls,
        account: Account,
        units: Amount,
        cost: Optional[Union[Cost, CostSpec]],
        price: Optional[Amount],
        flag: Optional[Flag],
        meta: Optional[Meta],
    ) -> Posting: ...
    def _replace(self: Posting) -> Posting: ...
    def _asdict(self: Posting) -> dict[str, Any]: ...

class Transaction:
    meta: Meta
    date: datetime.date
    flag: Flag
    payee: Optional[str]
    narration: str
    tags: Optional[set]
    links: Optional[set]
    postings: list[Posting]
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        flag: Flag,
        payee: Optional[str],
        narration: str,
        tags: Optional[set],
        links: Optional[set],
        postings: list[Posting],
    ) -> Transaction: ...
    def _replace(self: Transaction) -> Transaction: ...
    def _asdict(self: Transaction) -> dict[str, Any]: ...

class TxnPosting:
    txn: Transaction
    posting: Posting
    def __new__(
        cls,
        txn: Transaction,
        posting: Posting,
    ) -> TxnPosting: ...
    def _replace(self: TxnPosting) -> TxnPosting: ...
    def _asdict(self: TxnPosting) -> dict[str, Any]: ...

class Note:
    meta: Meta
    date: datetime.date
    account: Account
    comment: str
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        account: Account,
        comment: str,
    ) -> Note: ...
    def _replace(self: Note) -> Note: ...
    def _asdict(self: Note) -> dict[str, Any]: ...

class Event:
    meta: Meta
    date: datetime.date
    type: str
    description: str
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        type: str,
        description: str,
    ) -> Event: ...
    def _replace(self: Event) -> Event: ...
    def _asdict(self: Event) -> dict[str, Any]: ...

class Query:
    meta: Meta
    date: datetime.date
    name: str
    query_string: str
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        name: str,
        query_string: str,
    ) -> Query: ...
    def _replace(self: Query) -> Query: ...
    def _asdict(self: Query) -> dict[str, Any]: ...

class Price:
    meta: Meta
    date: datetime.date
    currency: Currency
    amount: Amount
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        currency: Currency,
        amount: Amount,
    ) -> Price: ...
    def _replace(self: Price) -> Price: ...
    def _asdict(self: Price) -> dict[str, Any]: ...

class Document:
    meta: Meta
    date: datetime.date
    account: Account
    filename: str
    tags: Optional[set]
    links: Optional[set]
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        account: Account,
        filename: str,
        tags: Optional[set],
        links: Optional[set],
    ) -> Document: ...
    def _replace(self: Document) -> Document: ...
    def _asdict(self: Document) -> dict[str, Any]: ...

class Custom:
    meta: Meta
    date: datetime.date
    type: str
    values: list[Any]
    def __new__(
        cls,
        meta: Meta,
        date: datetime.date,
        type: str,
        values: list[Any],
    ) -> Custom: ...
    def _replace(self: Custom) -> Custom: ...
    def _asdict(self: Custom) -> dict[str, Any]: ...

ALL_DIRECTIVES: tuple[type[Directive]]
Directive: TypeAlias = Union[
    Open,
    Close,
    Commodity,
    Pad,
    Balance,
    Transaction,
    Note,
    Event,
    Query,
    Price,
    Document,
    Custom,
]
Entries: TypeAlias = list[Directive]
Options: TypeAlias = dict[str, Any]

def new_metadata(
    filename: str, lineno: int, kvlist: dict[str, Any] | None = ...
) -> Meta: ...
def create_simple_posting(
    entry: Directive, account: Account, number: Decimal, currency: Currency
) -> Posting: ...
def create_simple_posting_with_cost(
    entry: Directive,
    account: Account,
    number: Decimal,
    currency: Currency,
    cost_number: Decimal,
    cost_currency: Currency,
) -> Posting: ...

NoneType: TypeAlias = None

def sanity_check_types(
    entry: Directive, allow_none_for_tags_and_links: bool = ...
) -> None: ...
def posting_has_conversion(posting: Posting) -> bool: ...
def transaction_has_conversion(transaction: Transaction) -> bool: ...
def get_entry(
    posting_or_entry: TxnPosting | Directive,
) -> Transaction | Directive: ...

SORT_ORDER: dict[Open | Balance | Document | Close, int]

def entry_sortkey(entry: Directive) -> tuple[datetime.date, int, int]: ...
def sorted(entries: list[Directive]) -> list[Directive]: ...
def posting_sortkey(
    entry: Directive | Posting,
) -> tuple[datetime.date, int, int]: ...
def filter_txns(entries: list[Directive]) -> list[Transaction]: ...
def has_entry_account_component(entry: Directive, component: str) -> bool: ...
def find_closest(
    entries: list[Directive], filename: str, lineno: int
) -> Directive: ...
def remove_account_postings(
    account: Account, entries: list[Directive]
) -> list[Directive]: ...
def iter_entry_dates(
    entries: list[Directive],
    date_begin: datetime.date,
    date_end: datetime.date,
) -> Iterator[Directive]: ...
