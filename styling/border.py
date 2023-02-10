from dataclasses import dataclass, replace
from overrides import override
from styling.color import *
from enum import Enum
from typing import Union
from openpyxl.cell import Cell
import openpyxl.styles as openpyxl
from styling.style import StylePart


class BorderStyle(Enum):
    DASH_DOT = "dashDot"
    DASH_DOT_DOT = "dashDotDot"
    DASHED = "dashed"
    DOTTED = "dotted"
    DOUBLE = "double"
    HAIR = "hair"
    MEDIUM = "medium"
    MEDIUM_DASH_DOT = "mediumDashDot"
    MEDIUM_DASH_DOT_DOT = "mediumDashDotDot"
    MEDIUM_DASHED = "mediumDashed"
    SLANT_DASH_DOT = "slantDashDot"
    THICK = "thick"
    THIN = "thin"


@dataclass(frozen=True)
class BorderSide:
    color: Union[Color, None] = None
    border_style: Union[str, None] = None

    def to_openpyxl(self):
        return openpyxl.Side(
            border_style=self.border_style,
            color=self.color if self.color is None else self.color.to_openpyxl()
        )


@dataclass(frozen=True)
class ParentBorderCoordinates:
    row_left_top: int
    col_left_top: int
    row_right_bottom: int
    col_right_bottom: int


@dataclass(frozen=True)
class Border(StylePart):
    all: Union[BorderSide, None] = None
    horizontal: Union[BorderSide, None] = None
    vertical: Union[BorderSide, None] = None
    left: Union[BorderSide, None] = None
    right: Union[BorderSide, None] = None
    top: Union[BorderSide, None] = None
    bottom: Union[BorderSide, None] = None

    @override
    def join(self, other: Union['Border', None]) -> 'Border':
        if other is None:
            return self
        if other.all is not None:
            return other
        result = self
        if other.horizontal is not None:
            result = replace(result, horizontal=other.horizontal,
                             top=other.top, bottom=other.bottom)
        if other.vertical is not None:
            result = replace(result, vertical=other.vertical,
                             left=other.left, right=other.right)
        result = replace(
            result,
            left=result.left if other.left is None else other.left,
            right=result.right if other.right is None else other.right,
            top=result.top if other.top is None else other.top,
            bottom=result.bottom if other.bottom is None else other.bottom
        )
        return result

    @override
    def apply_to(self, cell: Cell) -> None:
        border = openpyxl.Border()
        if self.all is not None:
            border.left, border.right, border.top, border.bottom = self.all.to_openpyxl()
        if self.horizontal is not None:
            border.top, border.bottom = self.horizontal.to_openpyxl()
        if self.vertical is not None:
            border.left, border.right = self.vertical.to_openpyxl()
        if self.left is not None:
            border.left = self.left.to_openpyxl()
        if self.right is not None:
            border.right = self.right.to_openpyxl()
        if self.top is not None:
            border.top = self.top.to_openpyxl()
        if self.bottom is not None:
            border.bottom = self.bottom.to_openpyxl()
        cell.border = border

    def apply_as_parent_to(self, cell: Cell, parent_border_coordinates: ParentBorderCoordinates) -> None:
        border: openpyxl.Border = cell.border
        if cell.row == parent_border_coordinates.row_left_top:
            if self.all is not None:
                border.top = self.all.to_openpyxl()
            if self.horizontal is not None:
                border.top = self.horizontal.to_openpyxl()
            if self.top is not None:
                border.top = self.top.to_openpyxl()
        if cell.column == parent_border_coordinates.col_right_bottom:
            if self.all is not None:
                border.right = self.all.to_openpyxl()
            if self.vertical is not None:
                border.right = self.vertical.to_openpyxl()
            if self.right is not None:
                border.right = self.right.to_openpyxl()
        if cell.row == parent_border_coordinates.row_right_bottom:
            if self.all is not None:
                border.bottom = self.all.to_openpyxl()
            if self.horizontal is not None:
                border.bottom = self.horizontal.to_openpyxl()
            if self.bottom is not None:
                border.bottom = self.bottom.to_openpyxl()
        if cell.column == parent_border_coordinates.col_left_top:
            if self.all is not None:
                border.left = self.all.to_openpyxl()
            if self.vertical is not None:
                border.left = self.vertical.to_openpyxl()
            if self.right is not None:
                border.left = self.right.to_openpyxl()
