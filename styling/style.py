from typing import Union
from abc import ABC, abstractmethod
from dataclasses import dataclass

from overrides import override
from openpyxl.cell import Cell

import internals.internals as internal
from styling.text_style import TextStyle
from styling.fill import Fill
from styling.border import Border


class StylePart(ABC):
    @abstractmethod
    def join(self, other: Union['StylePart', None]) -> 'StylePart':
        pass

    @abstractmethod
    def apply_to(self, cell: Cell) -> None:
        pass


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


@dataclass(frozen=True)
class Styler(internal.Buildable):
    child: internal.Buildable
    fill: Union[Fill, None] = None
    text_style: Union[TextStyle, None] = None
    parent_border: Union[Border, None] = None
    child_border: Union[Border, None] = None

    @override
    def internal_build(self, context: internal.BuildContext) -> None:
        new_context = context.with_style_change(self)
        self.child.internal_build(new_context)

    @override
    def build(self) -> 'internal.Buildable':
        return self.child

    @property
    def style(self):
        return Style(
            fill=self.fill,
            text_style=self.text_style,
            parent_border=self.parent_border,
            child_border=self.child_border
        )

    @staticmethod
    def from_style(child: internal.Buildable, style: Style):
        return Styler(child, style.fill, style.text_style, style.parent_border, style.child_border)
