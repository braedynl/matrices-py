import functools
import operator
from abc import ABCMeta, abstractmethod
from collections.abc import Sequence
from typing import Generic, TypeVar

from .utilities import Rule

__all__ = ["MatrixLike", "matcmp", "matmul", "matmap"]

T_co = TypeVar("T_co", covariant=True)
M_co = TypeVar("M_co", covariant=True, bound=int)
N_co = TypeVar("N_co", covariant=True, bound=int)


class MatrixLike(Sequence[T_co], Generic[T_co, M_co, N_co], metaclass=ABCMeta):

    def __eq__(self, other):
        """Return true if element-wise `a is b or a == b` is true for all
        element pairs, otherwise false
        """
        if self is other:
            return True
        if isinstance(other, MatrixLike):
            return all(matmap(lambda x, y: x is y or x == y, self, other))
        return NotImplemented

    def __lt__(self, other):
        """Return true if lexicographic `a < b`, otherwise false"""
        return matcmp(self, other) < 0

    def __le__(self, other):
        """Return true if lexicographic `a <= b`, otherwise false"""
        return matcmp(self, other) <= 0

    def __gt__(self, other):
        """Return true if lexicographic `a > b`, otherwise false"""
        return matcmp(self, other) > 0

    def __ge__(self, other):
        """Return true if lexicographic `a >= b`, otherwise false"""
        return matcmp(self, other) >= 0

    def __len__(self):
        """Return the matrix's size"""
        return self.size

    @abstractmethod
    def __getitem__(self, key):
        """Return the element or sub-matrix corresponding to `key`"""
        pass

    def __iter__(self):
        """Return an iterator over the values of the matrix in row-major order"""
        keys = range(self.size)
        yield from map(self.__getitem__, keys)

    def __reversed__(self):
        """Return an iterator over the values of the matrix in reverse
        row-major order
        """
        keys = range(self.size)
        yield from map(self.__getitem__, reversed(keys))

    def __contains__(self, value):
        """Return true if the matrix contains `value`, otherwise false"""
        return any(map(lambda x: x is value or x == value, self))

    @abstractmethod
    def __add__(self, other):
        """Return element-wise `a + b`"""
        pass

    @abstractmethod
    def __sub__(self, other):
        """Return element-wise `a - b`"""
        pass

    @abstractmethod
    def __mul__(self, other):
        """Return element-wise `a * b`"""
        pass

    @abstractmethod
    def __truediv__(self, other):
        """Return element-wise `a / b`"""
        pass

    @abstractmethod
    def __floordiv__(self, other):
        """Return element-wise `a // b`"""
        pass

    @abstractmethod
    def __mod__(self, other):
        """Return element-wise `a % b`"""
        pass

    @abstractmethod
    def __divmod__(self, other):
        """Return element-wise `divmod(a, b)`"""
        pass

    @abstractmethod
    def __pow__(self, other):
        """Return element-wise `a ** b`"""
        pass

    @abstractmethod
    def __lshift__(self, other):
        """Return element-wise `a << b`"""
        pass

    @abstractmethod
    def __rshift__(self, other):
        """Return element-wise `a >> b`"""
        pass

    @abstractmethod
    def __and__(self, other):
        """Return element-wise `a & b`"""
        pass

    @abstractmethod
    def __xor__(self, other):
        """Return element-wise `a ^ b`"""
        pass

    @abstractmethod
    def __or__(self, other):
        """Return element-wise `a | b`"""
        pass

    @abstractmethod
    def __matmul__(self, other):
        """Return the matrix product"""
        pass

    @abstractmethod
    def __neg__(self):
        """Return element-wise `-a`"""
        pass

    @abstractmethod
    def __pos__(self):
        """Return element-wise `+a`"""
        pass

    @abstractmethod
    def __abs__(self):
        """Return element-wise `abs(a)`"""
        pass

    @abstractmethod
    def __invert__(self):
        """Return element-wise `~a`"""
        pass

    @property
    @abstractmethod
    def shape(self):
        """A collection of the matrix's dimensions"""
        pass

    @property
    def nrows(self):
        """The matrix's number of rows"""
        return self.shape.nrows

    @property
    def ncols(self):
        """The matrix's number of columns"""
        return self.shape.ncols

    @property
    def size(self):
        """The product of the matrix's number of rows and columns"""
        nrows, ncols = self.shape
        return nrows * ncols

    @abstractmethod
    def equal(self, other):
        """Return element-wise `a == b`"""
        pass

    @abstractmethod
    def not_equal(self, other):
        """Return element-wise `a != b`"""
        pass

    @abstractmethod
    def lesser(self, other):
        """Return element-wise `a < b`"""
        pass

    @abstractmethod
    def lesser_equal(self, other):
        """Return element-wise `a <= b`"""
        pass

    @abstractmethod
    def greater(self, other):
        """Return element-wise `a > b`"""
        pass

    @abstractmethod
    def greater_equal(self, other):
        """Return element-wise `a >= b`"""
        pass

    @abstractmethod
    def logical_and(self, other):
        """Return element-wise `logical_and(a, b)`"""
        pass

    @abstractmethod
    def logical_or(self, other):
        """Return element-wise `logical_or(a, b)`"""
        pass

    @abstractmethod
    def logical_not(self):
        """Return element-wise `logical_not(a)`"""
        pass

    @abstractmethod
    def conjugate(self):
        """Return element-wise `conjugate(a)`"""
        pass

    def slices(self, *, by=Rule.ROW):
        """Return an iterator that yields shallow copies of each row or column"""
        if by is Rule.ROW:
            for i in range(self.nrows):
                yield self[i, :]
        else:
            for j in range(self.ncols):
                yield self[:, j]

    @abstractmethod
    def transpose(self):
        """Return the transpose of the matrix"""
        pass


def matcmp(a, b):
    """Return -1 if `a < b`, 1 if `a > b`, or 0 if `a == b`, compared
    lexicographically

    Raises `ValueError` if the two matrices have unequal shapes.
    """
    if (u := a.shape) != (v := b.shape):
        raise ValueError(f"matrix of shape {u} is incompatible with operand shape {v}")
    for x, y in zip(a, b):
        if x < y:
            return -1
        if x > y:
            return 1
    return 0


def matmul(a, b):
    """Return an iterator that yields the elements of the matrix product

    Raises `ValueError` if the two matrices have unequal inner dimensions, or
    if the inner dimension is 0.
    """
    (m, n), (p, q) = (u, v) = (a.shape, b.shape)
    if n != p:
        raise ValueError(f"matrix of shape {u} is incompatible with operand shape {v}")
    if not n:
        raise ValueError  # TODO: error message
    ix = range(m)
    jx = range(q)
    kx = range(n)  # TODO: custom iterator with shape information?
    for i in ix:
        for j in jx:
            yield functools.reduce(
                operator.add,
                map(lambda k: a[i * n + k] * b[k * q + j], kx),
            )


def matmap(func, a, b):
    """Return a mapping of `func` across two matrices

    Raises `ValueError` if the two matrices have unequal shapes.
    """
    if (u := a.shape) != (v := b.shape):
        raise ValueError(f"matrix of shape {u} is incompatible with operand shape {v}")
    return map(func, a, b)
