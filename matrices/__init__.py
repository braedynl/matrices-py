"""A basic set of utilities for storing and manipulating data in ≤ 2
dimensions.

Contains the `Matrix` definition, along with its related utility classes and
alternate constructors.

Author: Braedyn Lettinga
Version: 0.2.0
Documentation: https://github.com/braedynl/matrices-py/wiki
"""

from .callable import CallableMatrix
from .generic import GenericMatrix, Rule, Shape
from .numeric import (ComplexMatrix, IntegralMatrix, NumericMatrix,
                      RationalMatrix, RealMatrix)
from .ordering import OrderingMatrix
