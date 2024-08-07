import datetime
from typing import Optional
from beancount.core.data import Entries
from beancount.ingest.cache import _FileMemo as FileMemo

class ImporterProtocol:
    FLAG: str

    def name(self) -> str: ...
    def identify(self, file: FileMemo) -> bool: ...
    def extract(
        self, file: FileMemo, existing_entries: Entries
    ) -> Entries: ...
    def file_account(self, file: FileMemo) -> str: ...
    def file_name(self, file: FileMemo) -> str: ...
    def file_date(self, file: FileMemo) -> Optional[datetime.date]: ...
