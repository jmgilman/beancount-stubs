from __future__ import annotations

from beancount.query.query_execute import Allocator
from typing import Any, Callable, Iterator, Optional

SUPPORT_IMPLICIT_GROUPBY: bool

class CompilationError(Exception): ...

class EvalNode:
    dtype: type
    def __init__(self: EvalNode, dtype: type) -> None: ...
    def __eq__(self: EvalNode, other: object) -> bool: ...
    def childnodes(self: EvalNode) -> Iterator[EvalNode]: ...
    def __call__(self: EvalNode, context: Any) -> Any: ...

class EvalConstant(EvalNode):
    value: Any
    def __init__(self: EvalConstant, value: Any) -> None: ...
    def __call__(self: EvalConstant, _) -> Any: ...

class EvalUnaryOp(EvalNode):
    operand: Callable
    operator: Callable
    def __init__(
        self: EvalUnaryOp, operator: Callable, operand: Callable, dtype: type
    ) -> None: ...
    def __call__(self: EvalUnaryOp, context: Any) -> Any: ...

class EvalNot(EvalUnaryOp):
    def __init__(self: EvalNot, operand: Callable) -> None: ...

class EvalBinaryOp(EvalNode):
    operator: Callable
    left: Callable
    right: Callable
    def __init__(
        self: EvalBinaryOp,
        operator: Callable,
        left: Callable,
        right: Callable,
        dtype: type,
    ) -> None: ...
    def __call__(self: EvalBinaryOp, context: Any) -> Any: ...

class EvalEqual(EvalBinaryOp):
    def __init__(self: EvalEqual, left: Callable, right: Callable) -> None: ...

class EvalAnd(EvalBinaryOp):
    def __init__(self: EvalAnd, left: Callable, right: Callable) -> None: ...

class EvalOr(EvalBinaryOp):
    def __init__(self: EvalOr, left: Callable, right: Callable) -> None: ...

class EvalGreater(EvalBinaryOp):
    def __init__(
        self: EvalGreater, left: Callable, right: Callable
    ) -> None: ...

class EvalGreaterEq(EvalBinaryOp):
    def __init__(
        self: EvalGreaterEq, left: Callable, right: Callable
    ) -> None: ...

class EvalLess(EvalBinaryOp):
    def __init__(self: EvalLess, left: Callable, right: Callable) -> None: ...

class EvalLessEq(EvalBinaryOp):
    def __init__(
        self: EvalLessEq, left: Callable, right: Callable
    ) -> None: ...

class EvalMatch(EvalBinaryOp):
    @staticmethod
    def match(left: Callable, right: Callable) -> bool: ...
    def __init__(self: EvalMatch, left: Callable, right: Callable) -> None: ...

class EvalContains(EvalBinaryOp):
    def __init__(
        self: EvalContains, left: Callable, right: Callable
    ) -> None: ...
    def __call__(self: EvalContains, context: Any) -> Any: ...

class EvalMul(EvalBinaryOp):
    def __init__(self: EvalMul, left: Callable, right: Callable): ...

class EvalDiv(EvalBinaryOp):
    def __init__(self: EvalDiv, left: Callable, right: Callable): ...

class EvalAdd(EvalBinaryOp):
    def __init__(self: EvalAdd, left: Callable, right: Callable): ...

class EvalSub(EvalBinaryOp):
    def __init__(self: EvalSub, left: Callable, right: Callable): ...

OPERATORS: dict[Callable, Callable]
ANY: object

class EvalFunction(EvalNode):
    __intypes__: list
    operands: list[Callable]
    def __init__(
        self: EvalFunction, operands: list[Callable], dtype: type
    ) -> None: ...
    def eval_args(self: EvalFunction, context: Any) -> list: ...

class EvalColumn(EvalNode): ...

class EvalAggregator(EvalFunction):
    def allocate(self: EvalAggregator, allocator: Allocator) -> None: ...
    def initialize(self: EvalAggregator, store: list) -> None: ...
    def update(self: EvalAggregator, store: list, context: Any) -> None: ...
    def finalize(self: EvalAggregator, store: list) -> None: ...
    def __call__(self: EvalAggregator, context: Any) -> None: ...

class CompilationEnvironment:
    context_name: str
    columns: dict[str, Callable]
    functions: dict[str, Callable]
    def get_column(self: CompilationEnvironment, name: str) -> Any: ...
    def get_function(
        self: CompilationEnvironment, name: str, operands: list
    ) -> Any: ...

class AttributeColumn(EvalColumn):
    def __call__(self: AttributeColumn, row: Any) -> Any: ...

class ResultSetEnvironment(CompilationEnvironment):
    context_name: str
    def get_column(
        self: ResultSetEnvironment, name: str
    ) -> AttributeColumn: ...

def compile_expression(expr: Any, environ: CompilationEnvironment) -> Any: ...
def get_columns_and_aggregates(
    node: EvalNode,
) -> tuple[list[EvalNode], list[EvalNode]]: ...
def is_aggregate(node: EvalNode) -> bool: ...
def is_hashable_type(node: EvalNode) -> bool: ...
def find_unique_name(name: str, allocated_set: set[str]) -> str: ...

class EvalTarget:
    c_expr: EvalNode
    name: Optional[str]
    is_aggregate: bool

def compile_targets(targets: Any, environ: CompilationEnvironment) -> list: ...
def compile_group_by(
    group_by: Any, c_targets: list, environ: CompilationEnvironment
) -> tuple[list, list[int]]: ...
def compile_order_by(
    order_by: Any, c_targets: list, environ: CompilationEnvironment
) -> tuple[list, list[int]]: ...

class EvalFrom:
    c_expr: EvalNode
    open: Any
    close: Any
    clear: Any

def compile_from(
    from_clause: Any, environ: CompilationEnvironment
) -> EvalFrom | None: ...

class EvalQuery:
    c_targets: list[EvalTarget]
    c_from: EvalNode
    c_where: EvalNode
    group_indexes: list[int]
    order_indexes: list[int]
    ordering: Any
    limit: int
    distinct: bool
    flatten: bool

def compile_select(
    select: Any,
    targets_environ: CompilationEnvironment,
    postings_environ: CompilationEnvironment,
    entries_environ: CompilationEnvironment,
) -> EvalQuery: ...
def transform_journal(journal: Any) -> Any: ...
def transform_balances(balances: Any) -> Any: ...

class EvalPrint:
    c_from: EvalNode

def compile_print(print_stmt: Any, env_entries: CompilationEnvironment): ...
def compile(
    statement: Any,
    targets_environ: CompilationEnvironment,
    postings_environ: CompilationEnvironment,
    entries_environ: CompilationEnvironment,
) -> EvalQuery | EvalPrint: ...
