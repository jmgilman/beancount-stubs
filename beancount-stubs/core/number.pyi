from decimal import Decimal
from typing import Pattern

ZERO: Decimal
HALF: Decimal
ONE: Decimal
TEN: Decimal

class MISSING: ...

NUMBER_RE: Pattern

def D(strord: str | Decimal | None = ...) -> Decimal: ...
def round_to(number: Decimal, increment: Decimal) -> Decimal: ...
def same_sign(number1: Decimal, number2: Decimal) -> bool: ...
