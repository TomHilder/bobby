def check_move_legal(current_square, destination_square, piece_kind) -> bool:
    if destination_square in get_legal_moves(current_square, piece_kind):
        return True
    else:
        return False

def get_legal_moves(current_square, piece_kind) -> set:
    # get movement class for piece kind
    movement = get_movement_class(piece_kind=piece_kind)

def get_movement_class(piece_kind):
    PIECE_MOVEMENT = dict(
        pawn=PawnMove,
        knight=KnightMove,
        bishop=BishopMove,
        rook=RookMove,
        queen=QueenMove,
        king=KingMove,
    )
    if piece_kind not in PIECE_MOVEMENT:
        raise Exception(f"{piece_kind} is not a valid piece")
    return PIECE_MOVEMENT[piece_kind]

class PawnMove():
    
    @staticmethod
    def move(current_square, destination_square) -> bool:
        pass
    
    @staticmethod
    def take(current_square, destination_square) -> bool:
        pass
    
    @staticmethod
    def promote(current_square, destination_square) -> bool:
        pass

class KnightMove():
    
    @staticmethod
    def move(current_square, destination_square) -> bool:
        pass
    
    @staticmethod
    def take(current_square, destination_square) -> bool:
        pass

class BishopMove():
    
    @staticmethod
    def move(current_square, destination_square) -> bool:
        pass
    
    @staticmethod
    def take(current_square, destination_square) -> bool:
        pass

class RookMove():
    
    @staticmethod
    def move(current_square, destination_square) -> bool:
        pass
    
    @staticmethod
    def take(current_square, destination_square) -> bool:
        pass

class QueenMove():
    
    @staticmethod
    def move(current_square, destination_square) -> bool:
        pass
    
    @staticmethod
    def take(current_square, destination_square) -> bool:
        pass

class KingMove():
    
    @staticmethod
    def move(current_square, destination_square) -> bool:
        pass
    
    @staticmethod
    def take(current_square, destination_square) -> bool:
        pass