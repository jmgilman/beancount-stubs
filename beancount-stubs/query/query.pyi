from beancount.core.data import Directive
from typing import Any

def run_query(
    entries: list[Directive],
    options_map: dict[str, Any],
    query: str,
    *format_args,
    numberify: bool = ...
) -> tuple[list[tuple[str, type]], list[Any]]: ...
