from sizes.column_dimension import ColumnDimension

class ColumnSizeData:
    def __init__(self, column_dimension: ColumnDimension, lengths: set = set()) -> None:
        self.column_dimension = column_dimension
        self.lengths = lengths

    @classmethod
    def from_index_and_length(cls, index: int, length: int): 
        return cls(ColumnDimension(index), {length})

    def add_length(self, length: int):
        self.lengths.add(length)

    def get_max_length(self):
        return max(self.lengths)