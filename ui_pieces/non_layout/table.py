from internals.build_context import BuildContext
from ui_pieces.non_layout.excel_cell import ExcelCell
from sizes.size import Size
from ui_pieces.ui_piece import UIPiece
from abc import abstractmethod

class Table(UIPiece):
    def __init__(self, data: list[tuple], column_names: tuple[str]) -> None:
        super().__init__()
        self.data = data
        self.column_names = column_names

    def build(self, context: BuildContext) -> None:
        start_column_index = context.column_index
        for row in self.__get_all_cells():
            for cell in row:
                cell.build(context)
                context.column_index+=1
            context.column_index = start_column_index
            context.row_index+=1

    def __get_all_cells(self) -> list[tuple[ExcelCell]]:
        all_cells = []
        all_cells.append(self.get_column_name_cells(self.column_names))
        for row in self.data:
            all_cells.append(self.get_cells(row))
        return all_cells

    def get_size(self) -> Size:
        return Size(len(self.column_names), len(self.data) + 1)
            
    @abstractmethod
    def get_cells(self, data: tuple) -> tuple[ExcelCell]:
        pass

    @abstractmethod
    def get_column_name_cells(self, column_names: tuple[str]) -> tuple[ExcelCell]:
        pass


    

