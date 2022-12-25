from collections.abc import Iterator
from typing import Any, Literal, SupportsIndex, TypeVar, overload

from .abstract import MatrixLike
from .frozen import FrozenMatrix
from .shapes import Shape
from .typeshed import (SupportsAbs, SupportsAdd, SupportsAnd,
                       SupportsClosedAdd, SupportsConjugate, SupportsDivMod,
                       SupportsDotProduct, SupportsFloorDiv, SupportsInvert,
                       SupportsLShift, SupportsMod, SupportsMul, SupportsNeg,
                       SupportsOr, SupportsPos, SupportsPow, SupportsRAdd,
                       SupportsRAnd, SupportsRDivMod, SupportsRDotProduct,
                       SupportsRFloorDiv, SupportsRLShift, SupportsRMod,
                       SupportsRMul, SupportsROr, SupportsRPow,
                       SupportsRRShift, SupportsRShift, SupportsRSub,
                       SupportsRTrueDiv, SupportsRXor, SupportsSub,
                       SupportsTrueDiv, SupportsXor)
from .utilities import Rule

T = TypeVar("T")

T1 = TypeVar("T1")
T2 = TypeVar("T2")

M = TypeVar("M", bound=int)
N = TypeVar("N", bound=int)
P = TypeVar("P", bound=int)

SupportsClosedAddT = TypeVar("SupportsClosedAddT", bound=SupportsClosedAdd)

class MatrixTranspose(MatrixLike[T, M, N]):

    __slots__: tuple[Literal["_target"]]

    def __init__(self, target: MatrixLike[T, N, M]) -> None: ...
    def __repr__(self) -> str: ...
    @overload
    def __getitem__(self, key: SupportsIndex) -> T: ...
    @overload
    def __getitem__(self, key: slice) -> FrozenMatrix[T, Literal[1], int]: ...
    @overload
    def __getitem__(self, key: tuple[SupportsIndex, SupportsIndex]) -> T: ...
    @overload
    def __getitem__(self, key: tuple[SupportsIndex, slice]) -> FrozenMatrix[T, Literal[1], int]: ...
    @overload
    def __getitem__(self, key: tuple[slice, SupportsIndex]) -> FrozenMatrix[T, int, Literal[1]]: ...
    @overload
    def __getitem__(self, key: tuple[slice, slice]) -> FrozenMatrix[T, int, int]: ...
    def __iter__(self) -> Iterator[T]: ...
    def __reversed__(self) -> Iterator[T]: ...
    def __contains__(self, value: Any) -> bool: ...

    @overload
    def __add__(self: MatrixLike[SupportsAdd[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __add__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRAdd[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __sub__(self: MatrixLike[SupportsSub[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __sub__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRSub[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __mul__(self: MatrixLike[SupportsMul[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __mul__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRMul[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __truediv__(self: MatrixLike[SupportsTrueDiv[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __truediv__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRTrueDiv[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __floordiv__(self: MatrixLike[SupportsFloorDiv[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __floordiv__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRFloorDiv[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __mod__(self: MatrixLike[SupportsMod[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __mod__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRMod[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __divmod__(self: MatrixLike[SupportsDivMod[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __divmod__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRDivMod[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __pow__(self: MatrixLike[SupportsPow[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __pow__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRPow[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __lshift__(self: MatrixLike[SupportsLShift[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __lshift__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRLShift[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __rshift__(self: MatrixLike[SupportsRShift[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __rshift__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRRShift[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __and__(self: MatrixLike[SupportsAnd[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __and__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRAnd[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __xor__(self: MatrixLike[SupportsXor[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __xor__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRXor[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __or__(self: MatrixLike[SupportsOr[T1, T2], M, N], other: MatrixLike[T1, M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __or__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsROr[T1, T2], M, N]) -> FrozenMatrix[T2, M, N]: ...
    @overload
    def __matmul__(self: MatrixLike[SupportsDotProduct[T1, SupportsClosedAddT], M, N], other: MatrixLike[T1, N, P]) -> FrozenMatrix[SupportsClosedAddT, M, P]: ...
    @overload
    def __matmul__(self: MatrixLike[T1, M, N], other: MatrixLike[SupportsRDotProduct[T1, SupportsClosedAddT], N, P]) -> FrozenMatrix[SupportsClosedAddT, M, P]: ...
    def __neg__(self: MatrixLike[SupportsNeg[T1], M, N]) -> FrozenMatrix[T1, M, N]: ...
    def __pos__(self: MatrixLike[SupportsPos[T1], M, N]) -> FrozenMatrix[T1, M, N]: ...
    def __abs__(self: MatrixLike[SupportsAbs[T1], M, N]) -> FrozenMatrix[T1, M, N]: ...
    def __invert__(self: MatrixLike[SupportsInvert[T1], M, N]) -> FrozenMatrix[T1, M, N]: ...

    @property
    def shape(self) -> Shape[M, N]: ...
    @property
    def nrows(self) -> M: ...
    @property
    def ncols(self) -> N: ...
    @property
    def size(self) -> int: ...

    def equal(self, other: MatrixLike[Any, M, N]) -> FrozenMatrix[bool, M, N]: ...
    def not_equal(self, other: MatrixLike[Any, M, N]) -> FrozenMatrix[bool, M, N]: ...
    def lesser(self, other: MatrixLike[T, M, N]) -> FrozenMatrix[bool, M, N]: ...
    def lesser_equal(self, other: MatrixLike[T, M, N]) -> FrozenMatrix[bool, M, N]: ...
    def greater(self, other: MatrixLike[T, M, N]) -> FrozenMatrix[bool, M, N]: ...
    def greater_equal(self, other: MatrixLike[T, M, N]) -> FrozenMatrix[bool, M, N]: ...
    def logical_and(self, other: MatrixLike[Any, M, N]) -> FrozenMatrix[bool, M, N]: ...
    def logical_or(self, other: MatrixLike[Any, M, N]) -> FrozenMatrix[bool, M, N]: ...
    def logical_not(self) -> FrozenMatrix[bool, M, N]: ...
    def conjugate(self: MatrixLike[SupportsConjugate[T1], M, N]) -> FrozenMatrix[T1, M, N]: ...
    @overload
    def slices(self, *, by: Literal[Rule.ROW]) -> Iterator[FrozenMatrix[T, Literal[1], N]]: ...
    @overload
    def slices(self, *, by: Literal[Rule.COL]) -> Iterator[FrozenMatrix[T, M, Literal[1]]]: ...
    @overload
    def slices(self, *, by: Rule) -> Iterator[FrozenMatrix[T, int, int]]: ...
    @overload
    def slices(self) -> Iterator[FrozenMatrix[T, Literal[1], N]]: ...
    def transpose(self) -> MatrixLike[T, N, M]: ...
    def permute_index(self, key: SupportsIndex) -> int: ...
