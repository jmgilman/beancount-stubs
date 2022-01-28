import datetime

from beancount.core.data import Currency, Directive, Price
from decimal import Decimal
from typing import Optional

def get_last_price_entries(
    entries: list[Directive], date: datetime.date
) -> list[Price]: ...

class PriceMap(dict): ...

def build_price_map(
    entries: list[Directive],
) -> dict[tuple[Currency, Currency], tuple[datetime.date, Decimal]]: ...
def project(
    orig_price_map: PriceMap,
    from_currency: Currency,
    to_currency: Currency,
    base_currencies: Optional[set[Currency]] = ...,
) -> PriceMap: ...
def normalize_base_quote(
    base_quote: str | tuple[Currency, Currency]
) -> tuple[Currency, Currency]: ...
def get_all_prices(
    price_map: dict[tuple[Currency, Currency], tuple[datetime.date, Decimal]],
    base_quote: str | tuple[Currency, Currency],
) -> list[tuple[datetime.date, Decimal]]: ...
def get_latest_price(
    price_map: dict[tuple[Currency, Currency], tuple[datetime.date, Decimal]],
    base_quote: str | tuple[Currency, Currency],
) -> tuple[datetime.date, Decimal]: ...
def get_price(
    price_map: dict[tuple[Currency, Currency], tuple[datetime.date, Decimal]],
    base_quote: str | tuple[Currency, Currency],
    date: datetime.date | None = ...,
) -> tuple[datetime.date, Decimal]: ...
