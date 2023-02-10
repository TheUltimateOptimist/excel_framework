from typing import Union
from dataclasses import dataclass
from excel.excel_sheet import ExcelSheet
import styling.styling as styling
import internals.internals as internal


@dataclass(frozen=True)
class ExcelFile:
    filename: str
    sheets: list[ExcelSheet] = []
    global_style: Union[styling.Style, None] = None

    def create(self):
        if len(self.sheets) == 0:
            return
        context = internal.BuildContext.initial(self.sheets[0])
        for i, sheet in enumerate(self.sheets):
            if i > 0:
                context = context.new_sheet(sheet)
            if sheet.child and self.global_style:
                styling.Styler.from_style(
                    sheet.child, self.global_style).internal_build(context)
            elif sheet.child:
                sheet.child.internal_build(context)
            context.resizer.resize()
        context.workbook.save(self.filename)
