from abc import ABC, abstractmethod
from internals.build_context import BuildContext

class Buildable(ABC):
    @abstractmethod
    def build(self, context: BuildContext) -> None:
        pass