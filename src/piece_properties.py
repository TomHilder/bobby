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