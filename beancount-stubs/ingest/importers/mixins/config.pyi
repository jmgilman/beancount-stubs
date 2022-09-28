from _typeshed import Incomplete
from beancount.ingest import importer as importer

def validate_config(config, schema, importer): ...

class ConfigMixin(importer.ImporterProtocol):
    REQUIRED_CONFIG: Incomplete
    config: Incomplete
    def __init__(self, **kwds) -> None: ...
