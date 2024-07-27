from typing import Generator
import pytest

from beancount.ingest.cache import _FileMemo as FileMemo
from beancount.ingest.importer import ImporterProtocol

def pytest_addoption(parser: pytest.Parser) -> None: ...
def with_importer(importer: ImporterProtocol) -> pytest.MarkDecorator: ...
def with_testdir(directory: str) -> pytest.MarkDecorator: ...
def find_input_files(directory: str) -> Generator[str, None, None]: ...
def assertStringEqualNoWS(
    actual_string: str, expected_string: str
) -> None: ...
def compare_contents_or_generate(
    actual_string: str, expect_fn: str, generate: bool
) -> None: ...

class ImporterTestBase:
    def test_identify(
        self, importer: ImporterProtocol, file: FileMemo
    ) -> None: ...
    def test_extract(
        self,
        importer: ImporterProtocol,
        file: FileMemo,
        pytestconfig: pytest.Config,
    ) -> None: ...
    def test_file_date(
        self,
        importer: ImporterProtocol,
        file: FileMemo,
        pytestconfig: pytest.Config,
    ) -> None: ...
    def test_file_name(
        self,
        importer: ImporterProtocol,
        file: FileMemo,
        pytestconfig: pytest.Config,
    ) -> None: ...
    def test_file_account(
        self,
        importer: ImporterProtocol,
        file: FileMemo,
        pytestconfig: pytest.Config,
    ) -> None: ...
