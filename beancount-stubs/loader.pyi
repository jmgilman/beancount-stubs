from __future__ import annotations

from beancount.core.data import Directive
from typing import Any, Callable, TextIO, Optional

class LoadError:
    source: Any
    message: str
    entry: Directive
    def _replace(self: LoadError) -> LoadError: ...
    def _asdict(self: LoadError) -> dict[str, Any]: ...

PLUGINS_PRE: list[tuple[str, None]]
DEFAULT_PLUGINS_AUTO: list[tuple[str, None]]
PLUGINS_AUTO: list
PLUGINS_POST: list[tuple[str, None]]
RENAMED_MODULES: dict
PICKLE_CACHE_FILENAME: str
PICKLE_CACHE_THRESHOLD: float

def load_file(
    filename: str,
    log_timings: TextIO | Callable[[str], None] | None = ...,
    log_errors: TextIO | Callable[[str], None] | None = ...,
    extra_validations: Callable[[list[Directive], dict[str, Any]], list]
    | None = ...,
    encoding: str | None = ...,
) -> tuple[list[Directive], list, dict[str, Any]]: ...
def load_encrypted_file(
    filename: str,
    log_timings: TextIO | Callable[[str], None] | None = ...,
    log_errors: TextIO | Callable[[str], None] | None = ...,
    extra_validations: Callable[[list[Directive], dict[str, Any]], list]
    | None = ...,
    dedent: bool = ...,
    encoding: str | None = ...,
) -> tuple[list[Directive], list, dict[str, Any]]: ...
def get_cache_filename(pattern: str, filename: str) -> str: ...
def pickle_cache_function(
    cache_getter: Callable[[str], str],
    time_threshold: float,
    function: Callable,
) -> Callable: ...
def delete_cache_function(
    cache_getter: Callable[[str], str], function: Callable
) -> Callable: ...
def needs_refresh(options_map: dict[str, Any]) -> bool: ...
def compute_input_hash(filenames: list[str]) -> str: ...
def load_string(
    string: str,
    log_timings: TextIO | Callable[[str], None] | None = ...,
    log_errors: TextIO | Callable[[str], None] | None = ...,
    extra_validations: Callable[[list[Directive], dict[str, Any]], list]
    | None = ...,
    dedent: bool = ...,
    encoding: str | None = ...,
): ...
def aggregate_options_map(
    options_map: dict[str, Any], src_options_map: dict[str, Any]
) -> dict[str, Any]: ...
def run_transformations(
    entries: list[Directive],
    parse_errors: list,
    options_ma: dict[str, Any],
    log_timings: TextIO | Callable[[str], None] | None,
) -> tuple[list[Directive], list]: ...
def combine_plugins(*plugin_modules: list) -> list: ...
def load_doc(expect_errors: bool = ...) -> Callable[[Any], Any]: ...
def initialize(
    use_cache: bool, cache_filename: Optional[str] = ...
) -> None: ...
