from _typeshed import Incomplete
from beancount import loader as loader
from beancount.core import data as data
from beancount.core.number import D as D
from beancount.ingest import similar as similar
from beancount.parser import cmptest as cmptest, parser as parser

class TestDups(cmptest.TestCase):
    def test_find_similar_entries(self, entries, _, __): ...
    def test_find_similar_entries__multiple_matches(self, entries, _, __) -> None: ...
    def test_amounts_map(self, entries, _, __) -> None: ...

class TestSimilarityComparator(cmptest.TestCase):
    comparator: Incomplete
    def setUp(self) -> None: ...
    def test_simple(self, entries, _, __) -> None: ...
