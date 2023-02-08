from abc import abstractmethod
from internals.buildable import Buildable
from sizes.size import Size

class UIPiece(Buildable):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_size(self) -> Size:
        pass

    