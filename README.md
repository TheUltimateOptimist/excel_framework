A framework for creating excel files declaratively.

[openpyxl](https://pypi.org/project/openpyxl/) is a different library that is often used for creating excel files. However, it only provides very rudementary controls forcing you to access, style and fill every cell individually in an imperative manner. This can get unwieldy and difficult to maintain very quickly which is the problem solved by this package.  
[excel-framwork](https://pypi.org/project/excel-framework/) builds on top of [openpyxl](https://pypi.org/project/openpyxl/) providing you with a large set of ui components that you can compose into new ones to create excel files in an easy, readable and maintainable way.  
The archictecture of [excel-framwork](https://pypi.org/project/excel-framework/) was inspired by the cross platform ui development framework [flutter](https://flutter.dev/).

## Quickstart
An excel file with one cell containing hello world in bold:
```python
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
```

