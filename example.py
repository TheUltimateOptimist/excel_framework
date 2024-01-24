from excel_framework import *

ExcelFile(
    "hello.xlsx", 
    sheets=[
        ExcelSheet(
            "first sheet",
            child=Styler(
                child=ExcelCell("Hello World!"),
                style=Style(
                    text_style=TextStyle(bold=True)
                )
            )
        )
    ]
).create()