from styling.cell_style import CellStyle
from ui_pieces.non_layout.excel_cell import ExcelCell
from ui_pieces.non_layout.table import Table
from openpyxl.styles import Side, Color, Border, PatternFill, Font

class StieberDefaultTable(Table):
    def __init__(self, data: list[tuple], column_names: tuple[str]) -> None:
        super().__init__(data, column_names)

    def get_column_name_cells(self, column_names: tuple[str]) -> tuple[ExcelCell]:
        final_cells = []
        for column_name in column_names:
            final_cells.append(ExcelCell(column_name, style=CellStyle(border=self.__get_border(), fill=self.__get_blue_fill(), font=self.__get_white_font())))
        return tuple(final_cells)

    def get_cells(self, data: tuple) -> tuple[ExcelCell]:
        final_cells = []
        for value in data:
            final_cells.append(ExcelCell(value, style=CellStyle(border=self.__get_border())))
        return tuple(final_cells)

    def __get_border(self) -> Border:
        side = Side(style="thin", color=Color(rgb="FF000000"))
        return Border(right=side, left=side, top=side, bottom=side)

    def __get_blue_fill(self):
        blue = "FF000060"
        return PatternFill(start_color=blue, end_color=blue, fill_type="solid")

    def __get_white_font(self) -> Font:
        white = "FFFFFFFF"
        return Font(color=white)
