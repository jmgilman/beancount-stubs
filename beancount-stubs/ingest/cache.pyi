from typing import Callable, Generator, Optional

HEAD_DETECT_MAX_BYTES: int

class _FileMemo:
    name: str

    def __init__(self, filename: str) -> None: ...
    def __str__(self) -> str: ...
    def convert(self, converter_func: Callable[[str], bytes]) -> bytes: ...
    def mimetype(self) -> Optional[str]: ...
    def head(self, num_bytes: Optional[int], encoding: Optional[str]) -> str: ...
    def contents(self) -> bytes: ...

def mimetype(filename: str) -> str: ...
def head(
    num_bytes: Optional[int], encoding: Optional[str]
) -> Callable[[str], Generator[str, None, None]]: ...
def contents(filename: str) -> bytes: ...
def get_file(filename: str) -> _FileMemo: ...
