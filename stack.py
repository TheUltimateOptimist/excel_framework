from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        super().__init__()
        self.__values: list[T] = []
        self.__current = -1

    def push(self, value: T):
        self.__values.append(value)
        self.__current += 1

    def pop(self) -> T:
        return self.__values.pop()

    def __iter__(self):
        self.__current = len(self.__values) - 1
        return self

    def __next__(self):
        if self.__current == -1:
            raise StopIteration
        else:
            item = self.__values[self.__current]
            self.__current -= 1
            return item

    def __len__(self):
        return len(self.__values)
