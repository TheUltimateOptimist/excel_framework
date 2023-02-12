from dataclasses import dataclass
from excel.excel_file import ExcelFile
from excel.excel_sheet import ExcelSheet
from buildables.non_layout.excel_cell import ExcelCell
from buildables.layout.column import Column
from buildables.layout.row import Row
from buildables.layout.table import Table, TableColumn, AutoWidth, FixedWidth
from styling.border import Border, BorderSide, BorderStyle
from styling.style import Style
from styling.color import Colors
from styling.fill import Fill
from styling.text_style import TextStyle


@dataclass(frozen=True)
class TestModel:
    one: str
    two: str
    three: str


test_model = TestModel("jdfdf", "das ist sehr schön", "ja du")
table = Table[TestModel](
    [
        TableColumn[TestModel](
            "one", lambda model: model.one, width=FixedWidth(6)),
        TableColumn[TestModel](
            "two", lambda model: model.two, width=AutoWidth()),
        TableColumn[TestModel](
            "three", lambda model: model.three, )
    ],
    [
        test_model,
        test_model
    ],
    column_name_style=Style(fill=Fill(Colors.blue.dark),
                            text_style=TextStyle(font_color=Colors.white), parent_border=Border(all=BorderSide(Colors.black, border_style=BorderStyle.THICK.value)))
)

ExcelFile("test_exce.xlsx", sheets=[
    ExcelSheet(
        "Sheet One",
        child=Column(
            children=[
                ExcelCell("1"),
                ExcelCell("2"),
                ExcelCell("3"),
                table
            ]
        )
    ),
    ExcelSheet(
        "Sheet Two",
        child=Row(
            children=[
                ExcelCell("1"),
                ExcelCell("2"),
                ExcelCell("3"),
                table
            ]
        )
    ),
    ExcelSheet("Sheet tABLE", child=table)
],
).create()

# from openpyxl.workbook import Workbook
# from openpyxl.worksheet.worksheet import Worksheet
# from openpyxl.cell import Cell
# from openpyxl.styles import Alignment, PatternFill, GradientFill, Color, Font, Border, Protection, Side


# class One:
#     def __init__(self) -> None:
#         self.one = 1
#         self.count = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count == 10:
#             raise StopIteration
#         else:
#             self.count += 1
#             return self.one


# for value in One():
#     print(value)

# workbook = Workbook()
# sheet: Worksheet = workbook.active
# cell: Cell = sheet.cell(1, 1, 1000)
# cell.border = Border()
# cell.number_format = ""
# workbook.save("test_excel.xlsx")
# from abc import ABC, abstractmethod
# from overrides import override


# class Doer(ABC):
#     @abstractmethod
#     def do(self, other: 'Doer') -> 'Doer':
#         pass


# class Child(Doer):
#     def __init__(self, value: int) -> None:
#         super().__init__()
#         self.value = value

#     @override
#     def do(self, other: 'Child') -> 'Child':
#         self.value = other.value
#         return self


# child = Child(1)
# other = Child(2)
# print(child.do(other).value)
# from typing import Union
# some_dict = dict[Union[int, None], int]()
# #some_dict[None] = 1
# some_dict[1] = 2
# del some_dict[None]
# print(some_dict[None])
# if None:
#     print("yes")
# if 1:
#     print("no")
# from dataclasses import dataclass


# @dataclass
# class One:
#     a: int
#     b: int

#     @property
#     def sum(self) -> int:
#         return self.a + self.b


# one = One(3, 3)
# print(one.sum)
# import buildables.layout.table
