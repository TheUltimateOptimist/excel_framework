# from ui_pieces.non_layout.excel_cell import ExcelCell
# from ui_pieces.non_layout.table import Table

# class DefaultTable(Table):
#     def __init__(self, data: list[tuple], column_names: tuple[str]) -> None:
#         super().__init__(data, column_names)

#     def get_cells(self, data: tuple) -> tuple[ExcelCell]:
#         final_cells = []
#         for value in data:
#             final_cells.append(ExcelCell(value))
#         return tuple(final_cells)

#     def get_column_name_cells(self, column_names: tuple[str]) -> tuple[ExcelCell]:
#         final_cells = []
#         for column_name in column_names:
#             final_cells.append(ExcelCell(column_name))
#         return tuple(final_cells)