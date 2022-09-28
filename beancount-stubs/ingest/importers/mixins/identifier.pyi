from _typeshed import Incomplete
from beancount.ingest import cache as cache, importer as importer

def identify(remap, converter, file): ...

class IdentifyMixin(importer.ImporterProtocol):
    remap: Incomplete
    converter: Incomplete
    def __init__(self, **kwds) -> None: ...
    def identify(self, file): ...
