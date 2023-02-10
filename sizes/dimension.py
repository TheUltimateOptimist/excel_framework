from dataclasses import dataclass
from abc import ABC
from typing import Union


@dataclass(frozen=True)
class Dimension(ABC):
    index: Union[int, None]


@dataclass(frozen=True)
class RowDimension(Dimension):
    """
    If the given index is None, the dimension will be applied onto all rows
    """
    height: float = 15


@dataclass(frozen=True)
class ColumnDimension(Dimension):
    """
    Do not use the default constructor!\n
    Use ColumnDimension.fixed() or ColumnDimension.auto() instead
    """
    width: Union[float, None]
    min_width: Union[float, None]
    max_width: Union[float, None]
    auto_size: bool
    max_content_length: int = 0
    length_multiplier: float = 1

    @staticmethod
    def fixed(index: Union[int, None], width: float) -> 'ColumnDimension':
        """
        If the given index is None, the dimension will be applied onto all columns
        """
        return ColumnDimension(index, width, min_width=None, max_width=None, auto_size=False)

    @staticmethod
    def auto(index: Union[int, None], min_width: float = 13, max_width: Union[float, None] = None, length_multiplier: float = 1) -> 'ColumnDimension':
        """
        If the given index is None, the dimension will be applied onto all columns
        """
        return ColumnDimension(index, None, min_width, max_width, auto_size=True, length_multiplier=length_multiplier)

    def with_length(self, length: int) -> 'ColumnDimension':
        return ColumnDimension(
            self.index,
            self.width,
            self.min_width,
            self.max_width,
            self.auto_size,
            length if length > self.max_content_length else self.max_content_length,
            self.length_multiplier
        )
