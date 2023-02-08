from internals.build_context import BuildContext
from sizes.dimension import Dimension
from sizes.resizer import Resizer
from ui_pieces.ui_piece import UIPiece

class ExcelSheet:
    def __init__(self, title: str, dimensions: list[Dimension] = [], child: UIPiece = None) -> None:
        self.title = title
        self.dimensions = dimensions
        self.child = child

    def build(self, context: BuildContext):
        context.sheet.title = self.title
        context.resizer = Resizer(context.sheet, self.dimensions)
        if self.child is not None:
            self.child.build(context)
        context.resizer.resize()
