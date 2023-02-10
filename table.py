from internals.buildable import Buildable
from overrides import override
from typing import Generic, TypeVar

T = TypeVar("T")


class Table(Buildable, Generic[T]):
    def __init__(self, data: list[T]) -> None:
        super().__init__()

    @override
    def build(self) -> 'Buildable':
