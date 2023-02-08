from internals.build_context import BuildContext
from excel.excel_sheet import ExcelSheet
from internals.buildable import Buildable

class ExcelFile(Buildable):
    def __init__(self, filename: str, sheets: list[ExcelSheet] = []) -> None:
        self.filename = filename
        self.sheets = sheets

    def build(self, context = None):
        if context is None:
            context = BuildContext()
        for i,sheet in enumerate(self.sheets):
            if i == 0:
                sheet.build(context)
            else:
                context.new_sheet()
                sheet.build(context)
        context.workbook.save(self.filename)