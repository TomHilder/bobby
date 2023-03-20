from .pieces import PieceProperties, Piece


class BoardProperties:
    # all file and rank labels
    FILES = {"a", "b", "c", "d", "e", "f", "g", "h"}
    RANKS = {"1", "2", "3", "4", "5", "6", "7", "8"}

    # number of files and ranks
    N_FILES = len(FILES)
    N_RANKS = len(RANKS)

    # number of each pieces per player
    N_PIECES = dict(pawn=8, knight=2, bishop=2, rook=2, queen=1, king=1)

    # colours
    COLOURS = {"light", "dark"}

    # static method for find the colour of a square
    @staticmethod
    def get_square_colour(file, rank):
        # if the file is odd
        if (ord(file) - 96) % 2:
            # if the rank is odd
            if int(rank) % 2:
                return "dark"
            # if the rank is even
            else:
                return "light"
        # if the file is even
        else:
            # if the rank is odd
            if int(rank) % 2:
                return "light"
            # if the rank is even
            else:
                return "dark"


class Board(BoardProperties):
    # start with no squares set up
    _squares = None

    # instantiate class and set up squares
    def __init__(self) -> None:
        # set up empty dictionary to contain square objects
        self._squares = dict()
        # loop over all square labels
        for file in self.FILES:
            for rank in self.RANKS:
                self._squares[file + rank] = Square(file=file, rank=rank)

    @classmethod
    def default_setup(cls) -> None:
        # constructs and returns Board object setup for start of a game
        pass

    def reset_setup(self) -> None:
        # clear all squares
        # create new pieces
        # place pieces into default position
        pass


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
