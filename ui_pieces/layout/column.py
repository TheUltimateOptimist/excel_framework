from internals.build_context import BuildContext
from sizes.size import Size
from ui_pieces.ui_piece import UIPiece

class Column(UIPiece):
    def __init__(self, children: list[UIPiece] = None) -> None:
        super().__init__()
        self.children = children

    def get_size(self) -> Size:
        if self.children is None:
            return Size(0, 0)
        width = 0
        height = 0
        for child in self.children:
            child_size = child.get_size()
            height+=child_size.height
            if child_size.width > width:
                width = child_size.width
        return Size(width, height)

    def build(self, context: BuildContext) -> None:
        row_index = context.row_index
        column_index = context.column_index
        for child in self.children:
            child_size = child.get_size()
            child.build(context)
            row_index+=child_size.height
            context.row_index = row_index
            context.column_index = column_index