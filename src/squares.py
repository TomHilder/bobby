from .board_properties import BoardProperties
from .pieces import *

class Square(BoardProperties):
    # initialise properties to be empty
    _file_label = None
    _rank_label = None
    _colour = None
    _contents = None

    # set up square
    def __init__(self, file: str, rank: str) -> None:
        self.file_label = file
        self.rank_label = rank
        self.colour = self.get_square_colour(file=file, rank=rank)
        
    def __str__(self) -> str:
        try:
            return f"{self.file_label+self.rank_label} contains {self.contents}."
        except:
            return f"{self.file_label+self.rank_label} contains nothing."

    def clear(self) -> None:
        # access private attribute directly since we are not setting a Piece
        self._contents = None

    @property
    def file_label(self) -> str:
        return self._file_label

    @file_label.setter
    def file_label(self, file: str) -> None:
        if file not in self.FILES:
            raise Exception(f"{file} is not a valid file.")
        self._file_label = file

    @property
    def rank_label(self) -> str:
        return self._rank_label

    @rank_label.setter
    def rank_label(self, rank: str) -> None:
        if rank not in self.RANKS:
            raise Exception(f"{rank} is not a valid rank.")
        self._rank_label = rank

    @property
    def colour(self) -> str:
        return self._colour

    @colour.setter
    def colour(self, colour: str) -> None:
        if colour not in self.COLOURS:
            raise Exception(f"{colour} is not a valid square colour.")
        self._colour = colour

    @property
    def contents(self) -> Piece:  # update type hint
        return self._contents

    @contents.setter
    def contents(self, piece: Piece) -> None:
        if piece.kind not in PieceProperties.VALUES.keys():
            raise Exception(f"{piece.kind} is not a valid piece.")
        self._contents = piece
