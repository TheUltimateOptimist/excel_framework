from abc import ABC
from overrides import EnforceOverrides
import sizes.sizes as sizes
import internals.build_context as internal


class Buildable(ABC, EnforceOverrides):
    def build(self) -> 'Buildable':
        return self

    def internal_build(self, context: internal.BuildContext) -> None:
        if self.build() == self:
            raise Exception(
                f"Error: build method not defined: The class {self.__class__.__name__,} failed to override the build method")
        self.build().internal_build(context)

    def get_size(self) -> sizes.Size:
        if self.build() == self:
            raise Exception(
                f"Error: build method not defined: The class {self.__class__.__name__,} failed to override the build method")
        return self.build().get_size()
