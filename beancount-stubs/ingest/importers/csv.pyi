import csv
import enum
from _typeshed import Incomplete
from beancount.core import data as data
from beancount.core.amount import Amount as Amount
from beancount.core.number import D as D, ZERO as ZERO
from beancount.ingest.importers.mixins import filing as filing, identifier as identifier
from beancount.utils import test_utils as test_utils
from beancount.utils.date_utils import parse_date_liberally as parse_date_liberally
from typing import Callable, Dict, Optional, Union

class Col(enum.Enum):
    DATE: str
    TXN_DATE: str
    TXN_TIME: str
    PAYEE: str
    NARRATION: str
    NARRATION1: str
    NARRATION2: str
    NARRATION3: str
    AMOUNT: str
    AMOUNT_DEBIT: str
    AMOUNT_CREDIT: str
    BALANCE: str
    TAG: str
    REFERENCE_ID: str
    DRCR: str
    LAST4: str
    ACCOUNT: str
    CATEGORY: str

def get_amounts(iconfig, row, allow_zero_amounts, parse_amount): ...

class Importer(identifier.IdentifyMixin, filing.FilingMixin):
    config: Incomplete
    currency: Incomplete
    skip_lines: Incomplete
    last4_map: Incomplete
    debug: Incomplete
    dateutil_kwds: Incomplete
    csv_dialect: Incomplete
    narration_sep: Incomplete
    encoding: Incomplete
    invert_sign: Incomplete
    categorizer: Incomplete
    def __init__(self, config, account, currency, regexps: Incomplete | None = ..., skip_lines: int = ..., last4_map: Optional[Dict] = ..., categorizer: Optional[Callable] = ..., institution: Optional[str] = ..., debug: bool = ..., csv_dialect: Union[str, csv.Dialect] = ..., dateutil_kwds: Optional[Dict] = ..., narration_sep: str = ..., encoding: Optional[str] = ..., invert_sign: Optional[bool] = ..., **kwds) -> None: ...
    def file_date(self, file): ...
    def extract(self, file, existing_entries: Incomplete | None = ...): ...
    def call_categorizer(self, txn, row): ...
    def parse_amount(self, string): ...
    def get_amounts(self, iconfig, row, allow_zero_amounts, parse_amount): ...

def normalize_config(config, head, dialect: str = ..., skip_lines: int = ...): ...
