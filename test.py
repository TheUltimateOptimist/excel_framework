# from queue import LifoQueue

import excel.excel as excel
from sizes.dimension import ColumnDimension, RowDimension
from buildables.non_layout.excel_cell import ExcelCell
from buildables.layout.column import Column
from buildables.layout.row import Row

excel.ExcelFile("test_exce.xlsx", sheets=[
    excel.ExcelSheet(
        "Sheet One",
        child=Column(
            children=[
                ExcelCell("1"),
                ExcelCell("2"),
                ExcelCell("3")
            ]
        )
    ),
    excel.ExcelSheet(
        "Sheet Two",
        child=Row(
            children=[
                ExcelCell("1"),
                ExcelCell("2"),
                ExcelCell("3")
            ]
        )
    )
],
)

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
