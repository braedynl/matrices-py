from abc import ABCMeta, abstractmethod
from collections.abc import Callable, Iterator, Sequence
from typing import Any, Generic, Literal, TypeVar, overload

from .shapes import ShapeLike
from .typeshed import (SupportsAbs, SupportsAdd, SupportsAnd,
                       SupportsConjugate, SupportsDivMod, SupportsDotProduct,
                       SupportsFloorDiv, SupportsInvert, SupportsLShift,
                       SupportsMod, SupportsMonomorphicAdd, SupportsMul,
                       SupportsNeg, SupportsOr, SupportsPos, SupportsPow,
                       SupportsRAdd, SupportsRAnd, SupportsRDivMod,
                       SupportsRDotProduct, SupportsRFloorDiv, SupportsRLShift,
                       SupportsRMod, SupportsRMul, SupportsROr, SupportsRPow,
                       SupportsRRShift, SupportsRShift, SupportsRSub,
                       SupportsRTrueDiv, SupportsRXor, SupportsSub,
                       SupportsTrueDiv, SupportsXor)
from .utilities import Rule

__all__ = ["MatrixLike", "matrix_order", "matrix_multiply", "matrix_map"]

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)

T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")
T5 = TypeVar("T5")

M = TypeVar("M", bound=int)
M_co = TypeVar("M_co", covariant=True, bound=int)

N = TypeVar("N", bound=int)
N_co = TypeVar("N_co", covariant=True, bound=int)

P = TypeVar("P", bound=int)
P_co = TypeVar("P_co", covariant=True, bound=int)

SupportsMonomorphicAddT = TypeVar("SupportsMonomorphicAddT", bound=SupportsMonomorphicAdd)


class MatrixLike(Sequence[T_co], Generic[T_co, M_co, N_co], metaclass=ABCMeta):

    def __eq__(self, other: Any) -> bool: ...
    def __lt__(self, other: MatrixLike[T_co, M_co, N_co]) -> bool: ...
    def __le__(self, other: MatrixLike[T_co, M_co, N_co]) -> bool: ...
    def __gt__(self, other: MatrixLike[T_co, M_co, N_co]) -> bool: ...
    def __ge__(self, other: MatrixLike[T_co, M_co, N_co]) -> bool: ...
    def __len__(self) -> int: ...
    @overload
    @abstractmethod
    def __getitem__(self, key: int) -> T_co: ...
    @overload
    @abstractmethod
    def __getitem__(self, key: slice) -> MatrixLike[T_co, Literal[1], int]: ...
    @overload
    @abstractmethod
    def __getitem__(self, key: tuple[int, int]) -> T_co: ...
    @overload
    @abstractmethod
    def __getitem__(self, key: tuple[int, slice]) -> MatrixLike[T_co, Literal[1], int]: ...
    @overload
    @abstractmethod
    def __getitem__(self, key: tuple[slice, int]) -> MatrixLike[T_co, int, Literal[1]]: ...
    @overload
    @abstractmethod
    def __getitem__(self, key: tuple[slice, slice]) -> MatrixLike[T_co, int, int]: ...
    def __iter__(self) -> Iterator[T_co]: ...
    def __reversed__(self) -> Iterator[T_co]: ...
    def __contains__(self, value: Any) -> bool: ...
    @overload
    @abstractmethod
    def __add__(self: MatrixLike[SupportsAdd[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __add__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRAdd[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __sub__(self: MatrixLike[SupportsSub[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __sub__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRSub[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __mul__(self: MatrixLike[SupportsMul[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __mul__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRMul[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __truediv__(self: MatrixLike[SupportsTrueDiv[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __truediv__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRTrueDiv[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __floordiv__(self: MatrixLike[SupportsFloorDiv[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __floordiv__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRFloorDiv[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __mod__(self: MatrixLike[SupportsMod[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __mod__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRMod[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __divmod__(self: MatrixLike[SupportsDivMod[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __divmod__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRDivMod[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __pow__(self: MatrixLike[SupportsPow[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __pow__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRPow[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __lshift__(self: MatrixLike[SupportsLShift[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __lshift__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRLShift[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __rshift__(self: MatrixLike[SupportsRShift[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __rshift__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRRShift[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __and__(self: MatrixLike[SupportsAnd[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __and__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRAnd[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __xor__(self: MatrixLike[SupportsXor[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __xor__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsRXor[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __or__(self: MatrixLike[SupportsOr[T1, T2], M_co, N_co], other: MatrixLike[T1, M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @overload
    @abstractmethod
    def __or__(self: MatrixLike[T1, M_co, N_co], other: MatrixLike[SupportsROr[T1, T2], M_co, N_co]) -> MatrixLike[T2, M_co, N_co]: ...
    @abstractmethod
    def __neg__(self: MatrixLike[SupportsNeg[T], M_co, N_co]) -> MatrixLike[T, M_co, N_co]: ...
    @abstractmethod
    def __pos__(self: MatrixLike[SupportsPos[T], M_co, N_co]) -> MatrixLike[T, M_co, N_co]: ...
    @abstractmethod
    def __abs__(self: MatrixLike[SupportsAbs[T], M_co, N_co]) -> MatrixLike[T, M_co, N_co]: ...
    @abstractmethod
    def __invert__(self: MatrixLike[SupportsInvert[T], M_co, N_co]) -> MatrixLike[T, M_co, N_co]: ...
    @overload
    def __matmul__(self: MatrixLike[SupportsDotProduct[T, SupportsMonomorphicAddT], M_co, N_co], other: MatrixLike[T, N_co, P_co]) -> MatrixLike[SupportsMonomorphicAddT, M_co, P_co]: ...
    @overload
    def __matmul__(self: MatrixLike[T, M_co, N_co], other: MatrixLike[SupportsRDotProduct[T, SupportsMonomorphicAddT], N_co, P_co]) -> MatrixLike[SupportsMonomorphicAddT, M_co, P_co]: ...

    @property
    @abstractmethod
    def shape(self) -> ShapeLike[M_co, N_co]: ...
    @property
    def nrows(self) -> M_co: ...
    @property
    def ncols(self) -> N_co: ...
    @property
    def size(self) -> int: ...

    @abstractmethod
    def equal(self, other: MatrixLike[Any, M_co, N_co]) -> MatrixLike[bool, M_co, N_co]: ...
    @abstractmethod
    def not_equal(self, other: MatrixLike[Any, M_co, N_co]) -> MatrixLike[bool, M_co, N_co]: ...
    @abstractmethod
    def lesser(self, other: MatrixLike[T_co, M_co, N_co]) -> MatrixLike[bool, M_co, N_co]: ...
    @abstractmethod
    def lesser_equal(self, other: MatrixLike[T_co, M_co, N_co]) -> MatrixLike[bool, M_co, N_co]: ...
    @abstractmethod
    def greater(self, other: MatrixLike[T_co, M_co, N_co]) -> MatrixLike[bool, M_co, N_co]: ...
    @abstractmethod
    def greater_equal(self, other: MatrixLike[T_co, M_co, N_co]) -> MatrixLike[bool, M_co, N_co]: ...
    @abstractmethod
    def logical_and(self, other: MatrixLike[Any, M_co, N_co]) -> MatrixLike[bool, M_co, N_co]: ...
    @abstractmethod
    def logical_or(self, other: MatrixLike[Any, M_co, N_co]) -> MatrixLike[bool, M_co, N_co]: ...
    @abstractmethod
    def logical_not(self) -> MatrixLike[bool, M_co, N_co]: ...
    @abstractmethod
    def conjugate(self: MatrixLike[SupportsConjugate[T], M_co, N_co]) -> MatrixLike[T, M_co, N_co]: ...
    @overload
    @abstractmethod
    def slices(self, *, by: Literal[Rule.ROW]) -> Iterator[MatrixLike[T_co, Literal[1], N_co]]: ...
    @overload
    @abstractmethod
    def slices(self, *, by: Literal[Rule.COL]) -> Iterator[MatrixLike[T_co, M_co, Literal[1]]]: ...
    @overload
    @abstractmethod
    def slices(self, *, by: Rule) -> Iterator[MatrixLike[T_co, int, int]]: ...
    @overload
    @abstractmethod
    def slices(self) -> Iterator[MatrixLike[T_co, Literal[1], N_co]]: ...


def matrix_order(a: MatrixLike[T, M, N], b: MatrixLike[T, M, N]) -> Literal[-1, 0, 1]: ...
@overload
def matrix_multiply(a: MatrixLike[SupportsDotProduct[T, SupportsMonomorphicAddT], M, N], b: MatrixLike[T, N, P]) -> Iterator[SupportsMonomorphicAddT]: ...
@overload
def matrix_multiply(a: MatrixLike[T, M, N], b: MatrixLike[SupportsRDotProduct[T, SupportsMonomorphicAddT], N, P]) -> Iterator[SupportsMonomorphicAddT]: ...
@overload
def matrix_map(func: Callable[[T1], T], a: MatrixLike[T1, M, N]) -> Iterator[T]: ...
@overload
def matrix_map(func: Callable[[T1, T2], T], a: MatrixLike[T1, M, N], b: MatrixLike[T2, M, N]) -> Iterator[T]: ...
@overload
def matrix_map(func: Callable[[T1, T2, T3], T], a: MatrixLike[T1, M, N], b: MatrixLike[T2, M, N], c: MatrixLike[T3, M, N]) -> Iterator[T]: ...
@overload
def matrix_map(func: Callable[[T1, T2, T3, T4], T], a: MatrixLike[T1, M, N], b: MatrixLike[T2, M, N], c: MatrixLike[T3, M, N], d: MatrixLike[T4, M, N]) -> Iterator[T]: ...
@overload
def matrix_map(func: Callable[[T1, T2, T3, T4, T5], T], a: MatrixLike[T1, M, N], b: MatrixLike[T2, M, N], c: MatrixLike[T3, M, N], d: MatrixLike[T4, M, N], e: MatrixLike[T5, M, N]) -> Iterator[T]: ...
@overload
def matrix_map(func: Callable[..., T], a: MatrixLike[Any, M, N], b: MatrixLike[Any, M, N], c: MatrixLike[Any, M, N], d: MatrixLike[Any, M, N], e: MatrixLike[Any, M, N], *fx: MatrixLike[Any, M, N]) -> Iterator[T]: ...
