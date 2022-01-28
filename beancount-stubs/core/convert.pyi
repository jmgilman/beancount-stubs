import datetime

from beancount.core.amount import Amount
from beancount.core.data import Currency, Posting
from beancount.core.position import Position
from decimal import Decimal

def get_units(pos: Position | Posting) -> Amount: ...
def get_cost(pos: Position | Posting) -> Amount: ...
def get_weight(pos: Position | Posting) -> Amount: ...
def get_value(
    pos: Position | Posting,
    price_map: dict[tuple[Currency, Currency], tuple[datetime.date, Decimal]],
    date: datetime.date | None = ...,
    output_date_prices: list[tuple[datetime.date, Decimal]] | None = ...,
): ...
def convert_position(
    pos: Position | Posting,
    target_currency: Currency,
    price_map: dict[tuple[Currency, Currency], tuple[datetime.date, Decimal]],
    date: datetime.date | None = ...,
): ...
def convert_amount(
    amt: Amount,
    target_currency: Currency,
    price_map: dict[tuple[Currency, Currency], tuple[datetime.date, Decimal]],
    date: datetime.date | None = ...,
    via: list[Currency] | None = ...,
): ...
