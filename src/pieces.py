from .board_properties import BoardProperties
from .piece_properties import PieceProperties


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
