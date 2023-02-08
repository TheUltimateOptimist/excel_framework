from sizes.dimension import Dimension

class RowDimension(Dimension):
    def __init__(self, index: int, height: float = 15) -> None:
        super().__init__()
        self.index = index
        self.height = height
        
