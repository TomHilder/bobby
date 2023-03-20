from .pieces import *
from .board_properties import BoardProperties


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
