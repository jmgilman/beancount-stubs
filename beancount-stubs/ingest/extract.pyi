from _typeshed import Incomplete
from beancount import loader as loader
from beancount.core import data as data
from beancount.ingest import cache as cache, identify as identify, similar as similar
from beancount.parser import printer as printer

HEADER: str
DUPLICATE_META: str

def extract_from_file(filename, importer, existing_entries: Incomplete | None = ..., min_date: Incomplete | None = ..., allow_none_for_tags_and_links: bool = ...): ...
def find_duplicate_entries(new_entries_list, existing_entries): ...
def print_extracted_entries(entries, file): ...
def extract(importer_config, files_or_directories, output, entries: Incomplete | None = ..., options_map: Incomplete | None = ..., mindate: Incomplete | None = ..., ascending: bool = ..., hooks: Incomplete | None = ...) -> None: ...

DESCRIPTION: str

def add_arguments(parser) -> None: ...
def run(args, _, importers_list, files_or_directories, hooks: Incomplete | None = ...): ...
