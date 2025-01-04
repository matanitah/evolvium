from enum import Enum, auto

class CellType(Enum):
    EMPTY = auto()
    FOOD = auto()
    WALL = auto()
    MOUTH = auto()
    PRODUCER = auto()
    MOVER = auto()
    KILLER = auto()
    ARMOR = auto()
    BUILDER = auto()

class Cell:
    def __init__(self, cell_type=CellType.EMPTY):
        self.type = cell_type
        self.organism = None

    @property
    def is_organism_cell(self):
        return self.type in {
            CellType.MOUTH, CellType.PRODUCER, CellType.MOVER,
            CellType.KILLER, CellType.ARMOR, CellType.BUILDER
        }