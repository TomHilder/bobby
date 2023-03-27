from .pieces import *
from .squares import *
from .board_properties import *


class Board(BoardProperties):
    # start with no squares set up
    _squares = None

    # instantiate class and set up squares
    def __init__(self) -> None:
        self.setup_squares()

    @classmethod
    def default_setup(cls) -> "Board":
        # construct board
        board = cls()
        # reset the setup
        board.reset_setup()
        # return the set up board
        return board
    
    def move(self, square_start: str, square_destination: str) -> None:
        # grab square objects
        try:
            sq_1 = self.squares[square_start]
            sq_2 = self.squares[square_destination]
        except:
            raise Exception("Square labels are not valid.")
        # grab piece in start square
        piece = sq_1.contents
        # NOTE: add piece-dependent movement logic 
        # clear both squares
        sq_1.clear()
        sq_2.clear()
        # put piece into destination square
        sq_2.contents = piece

    def reset_setup(self) -> None:
        # clear all squares
        self.clear_squares()
        # create and place pieces
        self.setup_all_pieces()

    def setup_squares(self) -> None:
        # set up empty dictionary to contain square objects
        self._squares = dict()
        # loop over all square labels
        for file in self.FILES:
            for rank in self.RANKS:
                self._squares[file + rank] = Square(file=file, rank=rank)

    def clear_squares(self) -> None:
        # loop over all squares
        for square in self.squares:
            self.squares[square].clear()

    @property
    def squares(self) -> dict:
        if self._squares is None:
            raise Exception(f"Board contains no squares.")
        return self._squares

    def setup_all_pieces(self) -> None:
        # setup pieces for both colours
        for colour in PieceProperties.COLOURS:
            self.setup_pieces(colour=colour)

    def setup_pieces(self, colour: str) -> None:
        # check colour is valid
        if colour not in PieceProperties.COLOURS:
            raise Exception(f"{colour} is not a valid piece colour.")
        # loop over all piece kinds for that colour
        for piece_kind in PieceProperties.DEFAULT_LOC[colour]:
            # loop over all default locations
            for square in PieceProperties.DEFAULT_LOC[colour][piece_kind]:
                # place piece
                PieceClass = get_piece_class(piece_kind=piece_kind)
                self.squares[square].contents = PieceClass(colour)


