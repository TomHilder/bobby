from .board_properties import BoardProperties


def get_piece_class(piece_kind):
    PIECES = dict(
        pawn=Pawn,
        knight=Knight,
        bishop=Bishop,
        rook=Rook,
        queen=Queen,
        king=King,
    )
    if piece_kind not in PIECES:
        raise Exception(f"{piece_kind} is not a valid piece")
    return PIECES[piece_kind]


class PieceProperties:
    # colours
    COLOURS = {"white", "black"}
    # kinds of piece and their values
    VALUES = dict(pawn=1, knight=3, bishop=3, rook=5, queen=8, king=0)
    # default locations for pieces
    DEFAULT_LOC_WHITE = dict(
        pawn={"a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"},
        knight={"b1", "g1"},
        bishop={"c1", "f1"},
        rook={"a1", "h1"},
        queen={"d1"},
        king={"e1"},
    )
    DEFAULT_LOC_BLACK = dict(
        pawn={"a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"},
        knight={"b8", "g8"},
        bishop={"c8", "f8"},
        rook={"a8", "h8"},
        queen={"d8"},
        king={"e8"},
    )
    DEFAULT_LOC = dict(white=DEFAULT_LOC_WHITE, black=DEFAULT_LOC_BLACK)
    
    # NOTE: not sure if keeping the below
    # # movement logic
    # MOVEMENT_LOGIC = dict() # add movement logic classes here


class Piece(PieceProperties):
    # initialise properties to be empty
    _colour = None
    _kind = None
    _value = None

    def __init__(self, kind: str, colour: str) -> None:
        self.colour = colour
        self.kind = kind
        
    def __str__(self) -> str:
        return f"{self.colour} {self.kind}"

    @property
    def colour(self) -> str:
        return self._colour

    @colour.setter
    def colour(self, colour: str) -> None:
        if colour not in self.COLOURS:
            raise Exception(f"{colour} is not a valid piece colour.")
        self._colour = colour

    @property
    def kind(self) -> str:
        return self._kind

    @kind.setter
    def kind(self, kind: str) -> None:
        if kind not in self.VALUES.keys():
            raise Exception(f"{kind} is not a valid kind of piece.")
        self._kind = kind
        self._value = self.VALUES[kind]

    @property
    def value(self) -> int:
        return self._value


class Pawn(Piece):
    def __init__(self, colour: str) -> None:
        super().__init__(kind="pawn", colour=colour)


class Knight(Piece):
    def __init__(self, colour: str) -> None:
        super().__init__(kind="knight", colour=colour)


class Bishop(Piece):
    def __init__(self, colour: str) -> None:
        super().__init__(kind="bishop", colour=colour)


class Rook(Piece):
    def __init__(self, colour: str) -> None:
        super().__init__(kind="rook", colour=colour)


class Queen(Piece):
    def __init__(self, colour: str) -> None:
        super().__init__(kind="queen", colour=colour)


class King(Piece):
    def __init__(self, colour: str) -> None:
        super().__init__(kind="king", colour=colour)
