from abc import ABC
from typing import Union
from dataclasses import dataclass
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
import excel.excel as excel
import sizes.sizes as sizes
import styling.styling as styling


@dataclass
class BuildContext(ABC):
    workbook: Workbook
    sheet: Worksheet
    resizer: sizes.Resizer
    row_index: int = 1
    column_index: int = 1
    style: Union[styling.Style, None] = None
    parent_border_coordinates: Union[styling.ParentBorderCoordinates, None] = None

    @staticmethod
    def initial(sheet: excel.ExcelSheet) -> 'BuildContext':
        workbook = Workbook()
        workbook.active.title = sheet.title
        return BuildContext(workbook, workbook.active, sizes.Resizer(workbook.active, sheet.dimensions))

    def new_sheet(self, sheet: excel.ExcelSheet) -> 'BuildContext':
        new_sheet: Worksheet = self.workbook.create_sheet(sheet.title)
        return BuildContext(self.workbook, new_sheet, sizes.Resizer(new_sheet, sheet.dimensions))

    def collect_length(self, length: int):
        self.resizer.collect_length(self.row_index, self.column_index, length)

    def with_style_change(self, styler: styling.Styler) -> 'BuildContext':
        new_style = styler.style
        if self.style:
            new_style = self.style.join(new_style)
        new_parent_border_coordinates = self.parent_border_coordinates
        if new_style.parent_border:
            child_size = styler.child.get_size()
            new_parent_border_coordinates = styling.ParentBorderCoordinates(
                self.row_index,
                self.column_index,
                self.row_index + child_size.width - 1,
                self.column_index + child_size.height - 1
            )
        return BuildContext(
            self.workbook,
            self.sheet,
            self.resizer,
            self.row_index,
            self.column_index,
            new_style,
            new_parent_border_coordinates
        )
