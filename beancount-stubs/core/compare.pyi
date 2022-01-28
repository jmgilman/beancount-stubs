from attr import frozen
from beancount.core import data as data
from beancount.core.data import Price as Price
from typing import Any, NamedTuple

class CompareError(NamedTuple):
    source: dict[str, Any]
    message: str
    entry: Any

IGNORED_FIELD_NAMES: set

def stable_hash_namedtuple(
    objtuple: tuple[Any], ignore: frozenset = ...
) -> str: ...
def hash_entry(entry: Any, exclude_meta: bool = ...) -> str: ...
def hash_entries(
    entries: list[Any], exclude_meta: bool = ...
) -> tuple[dict[str, Any], list[CompareError]]: ...
def compare_entries(
    entries1: list[Any], entries2: list[Any]
) -> tuple[bool, list[Any], list[Any]]: ...
def includes_entries(
    subset_entries: set[Any], entries: list[Any]
) -> tuple[bool, list[Any]]: ...
def excludes_entries(
    subset_entries: set[Any], entries: list[Any]
) -> tuple[bool, list[Any]]: ...
