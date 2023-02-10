import internals.internals as internal
import sizes.sizes as sizes
from overrides import override


class Column(internal.Buildable):
    def __init__(self, children: list[internal.Buildable] = []) -> None:
        super().__init__()
        self.children = children

    @override
    def get_size(self) -> sizes.Size:
        width = 0
        height = 0
        for child in self.children:
            child_size = child.get_size()
            height += child_size.height
            if child_size.width > width:
                width = child_size.width
        return sizes.Size(width, height)

    @override
    def internal_build(self, context: internal.BuildContext) -> None:
        row_index = context.row_index
        column_index = context.column_index
        for child in self.children:
            child_size = child.get_size()
            child.internal_build(context)
            row_index += child_size.height
            context.row_index = row_index
            context.column_index = column_index
