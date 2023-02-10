from dataclasses import dataclass
from typing import Any
import internals.internals as internal
import sizes.sizes as sizes
from overrides import override


@dataclass
class ExcelCell(internal.Buildable):
    value: Any = None

    def __get_length(self):
        if self.value is None:
            return 0
        if str(self.value).startswith('='):
            return 0
        return len(str(self.value))

    @override
    def get_size(self) -> sizes.Size:
        return sizes.Size(1, 1)

    @override
    def internal_build(self, context: internal.BuildContext) -> None:
        context.collect_length(self.__get_length())
        cell = context.sheet.cell(
            context.row_index, context.column_index, self.value)
        if context.style:
            context.style.apply_to(cell)
        if context.style and context.style.parent_border:
            assert context.parent_border_coordinates is not None
            context.style.parent_border.apply_as_parent_to(
                cell, context.parent_border_coordinates)
