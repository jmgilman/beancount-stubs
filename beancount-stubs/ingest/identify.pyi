from _typeshed import Incomplete
from beancount.ingest import cache as cache
from beancount.utils import file_utils as file_utils
from collections.abc import Generator

SECTION: str
FILE_TOO_LARGE_THRESHOLD: Incomplete

def find_imports(importer_config, files_or_directories, logfile: Incomplete | None = ...) -> Generator[Incomplete, None, None]: ...
def identify(importers_list, files_or_directories) -> None: ...

DESCRIPTION: str

def add_arguments(parser) -> None: ...
def run(_, __, importers_list, files_or_directories, hooks: Incomplete | None = ...): ...
