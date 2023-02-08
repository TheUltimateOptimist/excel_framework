from abc import ABC
from openpyxl.workbook import Workbook
from sizes.resizer import Resizer

class BuildContext(ABC):
    def __init__(self, row_index = 1, column_index = 1) -> None:
        super().__init__()
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.row_index = row_index
        self.column_index = column_index
        self.resizer: Resizer = None
    
    def collect_length(self, length: int):
        self.resizer.collect(self.column_index, length)

    def new_sheet(self):
        self.sheet = self.workbook.create_sheet("")
        self.row_index = 1
        self.column_index = 1 