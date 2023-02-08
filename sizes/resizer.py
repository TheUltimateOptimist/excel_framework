from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.utils import get_column_letter
from sizes.column_dimension import ColumnDimension
from sizes.column_size_data import ColumnSizeData
from sizes.dimension import Dimension
from sizes.row_dimension import RowDimension

class Resizer:
    def __init__(self, sheet: Worksheet, dimensions: list[Dimension]) -> None:
        self.sheet = sheet
        self.row_dimensions = list[RowDimension]()
        self.column_sizes = dict[int, ColumnSizeData]()
        for dimension in dimensions:
            if isinstance(dimension, RowDimension):
                self.row_dimensions.append(dimension)
            elif isinstance(dimension, ColumnDimension):
                self.column_sizes[dimension.index] = ColumnSizeData(dimension)
            
    def collect(self, column_index: int, length: int):
        if column_index in self.column_sizes.keys():
            self.column_sizes[column_index].add_length(length)
        else:
            self.column_sizes[column_index] = ColumnSizeData.from_index_and_length(column_index, length)

    def resize(self):
        self.__resize_columns()
        self.__resize_rows()

    def __resize_columns(self):
        for (index, column_size_data) in self.column_sizes.items():
            assert isinstance(column_size_data, ColumnSizeData)
            column_dimension = column_size_data.column_dimension
            column_letter = get_column_letter(index)
            if not column_dimension.auto_size and column_dimension.width is not None:
                self.sheet.column_dimensions[column_letter].width = column_dimension.width
            else:
                width = column_size_data.get_max_length()
                if width < column_dimension.min_width:
                    width = column_dimension.min_width
                if column_dimension.max_width is not None and width > column_dimension.max_width:
                    width = column_dimension.max_width
                self.sheet.column_dimensions[column_letter].width = width

    def __resize_rows(self):
        for row_dimension in self.row_dimensions:
            self.sheet.row_dimensions[row_dimension.index].height = row_dimension.height