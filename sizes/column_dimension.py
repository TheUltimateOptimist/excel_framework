from sizes.dimension import Dimension

class ColumnDimension(Dimension):
    """
    auto_size will be set to False if a width is provided
    """
    def __init__(self, index: int, width: float = None, max_width: float = None, min_width: float = 13, auto_size = True):
        super().__init__()
        self.index = index
        self.width = width
        self.max_width = max_width
        self.min_width = min_width
        if self.width is not None:
            auto_size = False
        self.auto_size = auto_size



    
        