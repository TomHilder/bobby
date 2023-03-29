from .pieces import Piece
from .squares import Square
from .board_properties import BoardProperties

from typing import Tuple

# def check_move_legal(current_square, destination_square, piece_kind) -> bool:
#     if destination_square in get_legal_moves(current_square, piece_kind):
#         return True
#     else:
#         return False

# def get_legal_moves(current_square, piece_kind) -> set:
#     # get movement class for piece kind
#     movement = get_movement_class(piece_kind=piece_kind)

# NOTE: put movement type into Piece classes!

class BasicMovements():
    
    @staticmethod
    def get_file_and_rank(in_square_label: str) -> Tuple[str, str]:
        # check length of label is correct
        if len(in_square_label) != 2:
            raise Exception(f"{in_square_label} must have length 2.")
        # get file and rank
        file = in_square_label[0]
        rank = in_square_label[1]
        # check that file and rank are valid
        if file not in BoardProperties.FILES or rank not in BoardProperties.RANKS:
            raise Exception(f"{in_square_label} is not a valid square.")
        # return file and rank
        return file, rank
    
    @staticmethod
    def increment_file(in_file: str) -> str:
        # increment file
        out_file = chr(ord(in_file) + 1)
        # check output file is valid
        if out_file not in BoardProperties.FILES:
            raise Exception(f"Cannot increment file, {in_file} is already the max.")
        # return output file
        return out_file
    
    @staticmethod
    def decrement_file(in_file: str) -> str:
        # decrement file
        out_file = chr(ord(in_file) - 1)
        # check output file is valid
        if out_file not in BoardProperties.FILES:
            raise Exception(f"Cannot decrement file, {in_file} is already the min.")
        # return output file
        return out_file
    
    @staticmethod
    def increment_rank(in_rank: str) -> str:
        # increment rank
        out_rank = chr(ord(in_rank) + 1)
        # check output is valid
        if out_rank not in BoardProperties.RANKS:
            raise Exception(f"Cannot increment rank, {in_rank} is already the max.")
        # return output rank
        return out_rank
    
    @staticmethod
    def decrement_rank(in_rank: str) -> str:
        # decrement rank
        out_rank = chr(ord(in_rank) - 1)
        # check output is valid
        if out_rank not in BoardProperties.RANKS:
            raise Exception(f"Cannot decrement rank, {in_rank} is already the min.")
    
    @staticmethod
    def up(in_square_label: str) -> str:
        file, rank = BasicMovements.get_file_and_rank(in_square_label)
        rank
        

# class Movement():
    
#     _current_square = None
#     _piece          = None
    
#     def __init__(self, current_square: Square, piece: Piece) -> None:
#         pass

# class Movement():
    
#     _current_square = None
#     _destinations   = None
    
#     def __init__(self, current_square) -> None:
#         pass
    
#     @classmethod
#     def get_destinations(cls, current_square) -> None:
        
#         movement = cls(current_square)
#         # find all legal moves and store in legal_moves
#         return cls

# class PawnMove():
    
#     @staticmethod
#     def move(current_square, destination_square) -> bool:
#         pass
    
#     @staticmethod
#     def take(current_square, destination_square) -> bool:
#         pass
    
#     @staticmethod
#     def promote(current_square, destination_square) -> bool:
#         pass

# class KnightMove():
    
#     @staticmethod
#     def move(current_square, destination_square) -> bool:
#         pass
    
#     @staticmethod
#     def take(current_square, destination_square) -> bool:
#         pass

# class BishopMove():
    
#     @staticmethod
#     def move(current_square, destination_square) -> bool:
#         pass
    
#     @staticmethod
#     def take(current_square, destination_square) -> bool:
#         pass

# class RookMove():
    
#     @staticmethod
#     def move(current_square, destination_square) -> bool:
#         pass
    
#     @staticmethod
#     def take(current_square, destination_square) -> bool:
#         pass

# class QueenMove():
    
#     @staticmethod
#     def move(current_square, destination_square) -> bool:
#         pass
    
#     @staticmethod
#     def take(current_square, destination_square) -> bool:
#         pass

# class KingMove():
    
#     @staticmethod
#     def move(current_square, destination_square) -> bool:
#         pass
    
#     @staticmethod
#     def take(current_square, destination_square) -> bool:
#         pass
    
# def get_movement_class(piece_kind: str) -> Movement:
#     PIECE_MOVEMENT = dict(
#         pawn=PawnMove,
#         knight=KnightMove,
#         bishop=BishopMove,
#         rook=RookMove,
#         queen=QueenMove,
#         king=KingMove,
#     )
#     if piece_kind not in PIECE_MOVEMENT:
#         raise Exception(f"{piece_kind} is not a valid piece")
#     return PIECE_MOVEMENT[piece_kind]