from openpyxl.styles import Fill, Font, Border, Alignment
from openpyxl.cell import Cell

class CellStyle:
    def __init__(self, fill = Fill(), font = Font(), border = Border(), alignment = Alignment(), format = "") -> None:
        self.fill = fill
        self.font = font
        self.border = border
        self.format = format
        self.alignment = alignment
        
    def apply_to(self, cell: Cell):
        cell.fill = self.fill
        cell.font = self.font
        cell.border = self.border
        cell.number_format = self.format
        cell.alignment = self.alignment

    # @classmethod
    # def bad(cls, format = ""):
    #     red = Color(rgb="FFFF0000")
    #     red_fill = PatternFill(start_color=red, end_color=red, fill_type="solid")
    #     return cls(fill=red_fill, format=format)

    # @classmethod
    # def good(cls, format = ""):
    #     green = Color(rgb="FF00FF00")
    #     green_fill = PatternFill(start_color=green, end_color=green, fill_type="solid")
    #     return cls(fill=green_fill, format=format)

 
    # """
    # attention: when this method is executed, the previous font gets lost
    # """
    # def bold(self):
    #     return CellStyle(fill=self.__fill, font=Font(bold=True), border=self.__border, format=self.__format)