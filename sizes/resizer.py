from openpyxl.worksheet.worksheet import Worksheet
from typing import Union
from openpyxl.utils import get_column_letter
import sizes.sizes as sizes


class Resizer:
    def __init__(self, sheet: Worksheet, dimensions: list[sizes.Dimension]) -> None:
        self.sheet = sheet
        self.row_dimensions = dict[Union[int, None], sizes.RowDimension]()
        self.column_dimensions = dict[Union[int,
                                            None], sizes.ColumnDimension]()
        for dimension in dimensions:
            if isinstance(dimension, sizes.RowDimension):
                self.row_dimensions[dimension.index] = dimension
            elif isinstance(dimension, sizes.ColumnDimension):
                self.column_dimensions[dimension.index] = dimension

    def collect_length(self, row_index: int, column_index: int, length: int) -> None:
        if row_index not in self.row_dimensions and None in self.row_dimensions:
            self.row_dimensions[row_index] = self.row_dimensions[None]
        if column_index in self.column_dimensions:
            dimension = self.column_dimensions[column_index]
            self.column_dimensions[column_index] = dimension.with_length(
                length)
        elif None in self.column_dimensions:
            dimension = self.column_dimensions[None]
            self.column_dimensions[column_index] = dimension.with_length(
                length)

    def resize(self):
        self.__resize_rows()
        self.__resize_columns()

    def __resize_rows(self):
        if None in self.row_dimensions:
            del self.row_dimensions[None]
        for row_index in self.row_dimensions:
            self.sheet.row_dimensions[row_index].height = self.row_dimensions[row_index].height

    def __resize_columns(self):
        if None in self.column_dimensions:
            del self.column_dimensions[None]
        for col_index in self.column_dimensions:
            assert(type(col_index) is int)
            column_dimension = self.column_dimensions[col_index]
            column_letter = get_column_letter(col_index)
            if column_dimension.auto_size:
                width = column_dimension.max_content_length*column_dimension.length_multiplier
                if column_dimension.min_width is not None and width < column_dimension.min_width:
                    width = column_dimension.min_width
                if column_dimension.max_width is not None and width > column_dimension.max_width:
                    width = column_dimension.max_width
                self.sheet.column_dimensions[column_letter].width = width
            else:
                self.sheet.column_dimensions[column_letter].width = column_dimension.width
