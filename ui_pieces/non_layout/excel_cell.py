from internals.build_context import BuildContext
from styling.cell_style import CellStyle
from sizes.size import Size
from ui_pieces.ui_piece import UIPiece

class ExcelCell(UIPiece):
    def __init__(self, value = None, style = CellStyle()) -> None:
        super().__init__()
        self.style = style
        self.value = value

    def get_length(self):
        if self.value is None:
            return 0
        if str(self.value).startswith('='):
            return 0
        return len(str(self.value))

    def get_size(self) -> Size:
        return Size(1,1)

    def build(self, context: BuildContext) -> None:
        context.collect_length(self.get_length())
        cell = context.sheet.cell(context.row_index, context.column_index, self.value)
        self.style.apply_to(cell)

