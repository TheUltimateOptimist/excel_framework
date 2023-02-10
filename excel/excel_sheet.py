from dataclasses import dataclass
from typing import Union
import sizes.sizes as sizes
import internals.internals as internal


@dataclass
class ExcelSheet:
    title: str
    child: Union[internal.Buildable, None] = None
    dimensions: list[sizes.Dimension] = []
