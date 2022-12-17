from collections.abc import Iterator
from typing import (Any, Literal, Optional, SupportsIndex, TypeVar, final,
                    overload)

from .abstract import ShapeLike

__all__ = ["ShapeView"]

M_co = TypeVar("M_co", covariant=True, bound=int)
N_co = TypeVar("N_co", covariant=True, bound=int)


@final
class ShapeView(ShapeLike[M_co, N_co]):

    __slots__: tuple[Literal["_target"]]

    def __init__(self, target: ShapeLike[M_co, N_co]) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    @overload
    def __getitem__(self, key: Literal[0]) -> M_co: ...
    @overload
    def __getitem__(self, key: Literal[1]) -> N_co: ...
    @overload
    def __getitem__(self, key: SupportsIndex) -> M_co | N_co: ...
    def __iter__(self) -> Iterator[M_co | N_co]: ...
    def __reversed__(self) -> Iterator[M_co | N_co]: ...
    def __contains__(self, value: Any) -> bool: ...
    def __deepcopy__(self, memo: Optional[dict[int, Any]] = None) -> ShapeView[M_co, N_co]: ...
    def __copy__(self) -> ShapeView[M_co, N_co]: ...