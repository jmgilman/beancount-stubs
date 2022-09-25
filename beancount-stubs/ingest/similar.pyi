from _typeshed import Incomplete
from beancount.core import amount as amount, data as data, interpolate as interpolate
from beancount.core.number import D as D, ONE as ONE, ZERO as ZERO

def find_similar_entries(entries, source_entries, comparator: Incomplete | None = ..., window_days: int = ...): ...

class SimilarityComparator:
    EPSILON: Incomplete
    cache: Incomplete
    max_date_delta: Incomplete
    def __init__(self, max_date_delta: Incomplete | None = ...) -> None: ...
    def __call__(self, entry1, entry2): ...

def amounts_map(entry): ...
