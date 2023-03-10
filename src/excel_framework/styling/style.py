from typing import Union
from dataclasses import dataclass

from overrides import override
from openpyxl.cell import Cell

from .style_part import StylePart
from .text_style import TextStyle
from .fill import Fill
from .border import Border


@dataclass(frozen=True)
class Style(StylePart):
    fill: Union[Fill, None] = None
    text_style: Union[TextStyle, None] = None
    parent_border: Union[Border, None] = None
    child_border: Union[Border, None] = None

    @override
    def join(self, other: Union['Style', None]) -> 'Style':
        if other is None:
            return self
        return Style(
            fill=other.fill if self.fill is None else self.fill.join(
                other.fill),
            text_style=other.text_style if self.text_style is None else self.text_style.join(
                other.text_style),
            parent_border=other.parent_border if self.parent_border is None else self.parent_border.join(
                other.parent_border),
            child_border=other.child_border if self.child_border is None else self.child_border.join(
                other.child_border)
        )

    def apply_to(self, cell: Cell) -> None:
        if self.fill:
            self.fill.apply_to(cell)
        if self.text_style:
            self.text_style.apply_to(cell)
        if self.child_border:
            self.child_border.apply_to(cell)
