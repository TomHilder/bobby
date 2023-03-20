class PieceProperties:
    # colours
    COLOURS = {"white", "black"}
    # kinds of piece and their values
    VALUES = dict(pawn=1, knight=3, bishop=3, rook=5, queen=8, king=0)


class Piece(PieceProperties):
    # initialise properties to be empty
    _colour = None
    _kind = None
    _value = None

    def __init__(self, colour: str, kind: str) -> None:
        self.colour = colour
        self.kind = kind

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
    def __init__(self, colour) -> None:
        super().__init__()
