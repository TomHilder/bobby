from .pieces import Piece
from .squares import Square
from .board_properties import BoardProperties, InvalidSquareError

from typing import Tuple, Set, Callable
from copy   import copy

# def check_move_legal(current_square, destination_square, piece_kind) -> bool:
#     if destination_square in get_legal_moves(current_square, piece_kind):
#         return True
#     else:
#         return False

# def get_legal_moves(current_square, piece_kind) -> set:
#     # get movement class for piece kind
#     movement = get_movement_class(piece_kind=piece_kind)

# NOTE: put movement type into Piece classes!

class InvalidMoveError(Exception):
    "Raised when a destination square does not exist"
    pass


class BasicMovements():
    
    @staticmethod
    def get_file_and_rank(in_square_label: str) -> Tuple[str, str]:
        # check length of label is correct
        if len(in_square_label) != 2:
            raise InvalidSquareError(f"{in_square_label} is not a valid square.")
        # get file and rank
        file = in_square_label[0]
        rank = in_square_label[1]
        # check that file and rank are valid
        if file not in BoardProperties.FILES or rank not in BoardProperties.RANKS:
            raise InvalidSquareError(f"{in_square_label} is not a valid square.")
        # return file and rank
        return file, rank
    
    @staticmethod
    def increment_file(in_square_label: str) -> str:
        # get input file and rank
        in_file, in_rank = BasicMovements.get_file_and_rank(in_square_label)
        # increment file
        out_file = chr(ord(in_file) + 1)
        # check output file is valid
        if out_file not in BoardProperties.FILES:
            raise InvalidMoveError(f"Cannot increment file, {in_file} is already the max.")
        # return output square
        return f"{out_file}{in_rank}"
    
    @staticmethod
    def decrement_file(in_square_label: str) -> str:
        # get input file and rank
        in_file, in_rank = BasicMovements.get_file_and_rank(in_square_label)
        # decrement file
        out_file = chr(ord(in_file) - 1)
        # check output file is valid
        if out_file not in BoardProperties.FILES:
            raise InvalidMoveError(f"Cannot decrement file, {in_file} is already the min.")
        # return output square
        return f"{out_file}{in_rank}"
    
    @staticmethod
    def increment_rank(in_square_label: str) -> str:
        # get input file and rank
        in_file, in_rank = BasicMovements.get_file_and_rank(in_square_label)
        # increment rank
        out_rank = chr(ord(in_rank) + 1)
        # check output is valid
        if out_rank not in BoardProperties.RANKS:
            raise InvalidMoveError(f"Cannot increment rank, {in_rank} is already the max.")
        # return output square
        return f"{in_file}{out_rank}"
    
    @staticmethod
    def decrement_rank(in_square_label: str) -> str:
        # get input file and rank
        in_file, in_rank = BasicMovements.get_file_and_rank(in_square_label)
        # decrement rank
        out_rank = chr(ord(in_rank) - 1)
        # check output is valid
        if out_rank not in BoardProperties.RANKS:
            raise InvalidMoveError(f"Cannot decrement rank, {in_rank} is already the min.")
        # return output square
        return f"{in_file}{out_rank}"
    
    @staticmethod
    def increment_upwards_diag(in_square_label: str) -> str:
        # increment file
        square_step1 = BasicMovements.increment_file(in_square_label)
        # increment rank
        square_step2 = BasicMovements.increment_rank(square_step1)
        # return result
        return square_step2
    
    @staticmethod
    def decrement_upwards_diag(in_square_label: str) -> str:
        # decrement file
        square_step1 = BasicMovements.decrement_file(in_square_label)
        # decrement rank
        square_step2 = BasicMovements.decrement_rank(square_step1)
        # return result
        return square_step2
    
    @staticmethod
    def increment_downwards_diag(in_square_label: str) -> str:
        # increment file
        square_step1 = BasicMovements.increment_file(in_square_label)
        # decrement rank
        square_step2 = BasicMovements.decrement_rank(square_step1)
        # return result
        return square_step2
    
    @staticmethod
    def decrement_downwards_diag(in_square_label: str) -> str:
        # decrement file
        square_step1 = BasicMovements.decrement_file(in_square_label)
        # increment rank
        square_step2 = BasicMovements.increment_rank(square_step1)
        # return result
        return square_step2
    
    @staticmethod
    def L_move_generator(in_square_label: str, long_move_func: Callable, short_move_func: Callable) -> str:
        # move 2 squares in long direction
        square_step1 = long_move_func(long_move_func(in_square_label))
        # move 1 square in short direction
        square_step2 = short_move_func(square_step1)
        # return result
        return square_step2
    
    @staticmethod
    def L_move_iterator(in_square_label: str, move_func1: Callable, move_func2: Callable) -> Set[str]:
        # initialise set for possible destinations
        destination_squares = set()
        # put the move functions in a list
        moves = [move_func1, move_func2]
        # try both combinations
        for i in range(len(moves)):
            try:
                destination_squares.add(
                    BasicMovements.L_move_generator(in_square_label, moves[i], moves[i-1])
                )
            except InvalidMoveError:
                pass
        # return results
        return destination_squares

    @staticmethod
    def straight_move_iterator(in_square_label: str, iter_func: Callable) -> Set[str]:
        # initialise set for possible destinations
        destination_squares = set()
        # start iteration with starting square
        i_square = copy(in_square_label)
        # loop until we get an illegal square, which will raise an Exception
        while True:
            try:
                i_square = iter_func(i_square)
            except InvalidMoveError:
                break
            destination_squares.add(i_square)
        # return all destinations
        return destination_squares
    
    @staticmethod
    def king_move_iterator(in_square_label: str) -> Set[str]:
        # initialise set for possible destinations
        destination_squares = set()
        # put the possible move functions in a list
        moves = [
            BasicMovements.increment_file,
            BasicMovements.decrement_file,
            BasicMovements.increment_rank,
            BasicMovements.decrement_rank,
            BasicMovements.increment_upwards_diag,
            BasicMovements.decrement_upwards_diag,
            BasicMovements.increment_downwards_diag,
            BasicMovements.decrement_downwards_diag
        ]
        # try all moves
        for i in range(len(moves)):
            try:
                destination_squares.add(
                    moves[i](in_square_label)
                )
            except InvalidMoveError:
                pass
        # return results
        return destination_squares        
    
    @staticmethod
    def get_all_rook_like(in_square_label: str) -> Set[str]:
        # get all horizontal moves
        pos_hor = BasicMovements.straight_move_iterator(in_square_label, BasicMovements.increment_file)
        neg_hor = BasicMovements.straight_move_iterator(in_square_label, BasicMovements.decrement_file)
        # get all vertical moves
        pos_ver = BasicMovements.straight_move_iterator(in_square_label, BasicMovements.increment_rank)
        neg_ver = BasicMovements.straight_move_iterator(in_square_label, BasicMovements.decrement_rank)
        # return the union of all move sets above
        return pos_hor | neg_hor | pos_ver | neg_ver
    
    @staticmethod
    def get_all_bishop_like(in_square_label: str) -> Set[str]:
        # get all moves along the positive diagonal
        pos_updiag = BasicMovements.straight_move_iterator(in_square_label, BasicMovements.increment_upwards_diag)
        neg_updiag = BasicMovements.straight_move_iterator(in_square_label, BasicMovements.decrement_upwards_diag)
        # get all moves along the negative diagonal
        pos_downdiag = BasicMovements.straight_move_iterator(in_square_label, BasicMovements.increment_downwards_diag)
        neg_downdiag = BasicMovements.straight_move_iterator(in_square_label, BasicMovements.decrement_downwards_diag)
        # return the union of all move sets above
        return pos_updiag | neg_updiag | pos_downdiag | neg_downdiag
    
    @staticmethod
    def get_all_knight_like(in_square_label: str) -> Set[str]:
        # get all moves near the positive diagonal
        pos_updiag = BasicMovements.L_move_iterator(in_square_label, BasicMovements.increment_file, BasicMovements.increment_rank)
        neg_updiag = BasicMovements.L_move_iterator(in_square_label, BasicMovements.decrement_file, BasicMovements.decrement_rank)
        # get all moves near the negative diagonal
        pos_downdiag = BasicMovements.L_move_iterator(in_square_label, BasicMovements.increment_file, BasicMovements.decrement_rank)
        neg_downdiag = BasicMovements.L_move_iterator(in_square_label, BasicMovements.decrement_file, BasicMovements.increment_rank)
        # return the union of all move sets above
        return pos_updiag | neg_updiag | pos_downdiag | neg_downdiag
    
    @staticmethod
    def get_all_king_like(in_square_label: str) -> Set[str]:
        # get all moves using iterator function
        moves = BasicMovements.king_move_iterator(in_square_label)
        # return results
        return moves
    
    @staticmethod
    def get_all_queen_like(in_square_label: str) -> Set[str]:
        # get all rook-like moves
        rook_moves = BasicMovements.get_all_rook_like(in_square_label)
        # get all bisop-like moves
        bishop_moves = BasicMovements.get_all_bishop_like(in_square_label)
        # return the union of rook-like and bishop-like moves
        return rook_moves | bishop_moves
    
    @staticmethod
    def get_all_pawn_move_like(in_square_label: str, piece_color: str) -> Set[str]:
        # get the correct movement function, and original rank, based on color
        if piece_color == "white":
            move_func = BasicMovements.increment_rank
            original_rank = "2"
        elif piece_color == "black":
            move_func = BasicMovements.decrement_rank
            original_rank = "7"
        # get file and rank of piece
        file, rank = BasicMovements.get_file_and_rank(in_square_label)
        # initial set set for possible moves
        moves = set()
        # add single move
        try:
            moves.add(move_func(in_square_label))
        except InvalidMoveError:
            pass 
        # add double move only if on original rank 
        if rank == original_rank:
            # this will never throw an exception by construction
            moves.add(move_func(move_func(in_square_label)))
        # return moves
        return moves
    
    @staticmethod
    def get_all_pawn_take_like(in_square_label: str, piece_color: str) -> Set[str]:
        pass            
        
class PieceMovements():
    # each method takes starting square and returns two sets
    # set 1 has moves that are possible on an empty board
    # set 2 has moves possible assuming destination sq occupied by enemy piece
    
    @staticmethod
    def rook_moves(square_label: str) -> Tuple[set, set]:
        # initialise set for destinations
        destinations = set()
        # get file and rank of starting square
        start_file, start_rank = BasicMovements.get_file_and_rank(square_label)
        # get all vertical moves
        for rank in BoardProperties.RANKS:
            destinations.add(f"{start_file}{rank}")
        # get all horizontal moves
        for file in BoardProperties.FILES:
            destinations.add(f"{file}{start_rank}")
        # remove starting square from possible moves
        destinations.remove(square_label)
        # normal and take destinations are the same for rooks
        return destinations, copy(destinations)
    
    # def bishop_moves() -> Tuple[set, set]:
    #     pass
    
    # def knight_moves() -> Tuple[set, set]:
    #     pass
    
    # def queen_moves() -> Tuple[set, set]:
    #     pass
    
    # def king_moves() -> Tuple[set, set]:
    #     pass
    
    # def pawn_moves() -> Tuple[set, set]:
    #     pass
        
class RookMove():
    
    @staticmethod
    def get_legal_moves(start_square):
        possible_destinations = {}
        # start by just getting every possible destination sq on an empty board
        # check for blocking (throw out moves PAST piece)
        # check for takes (throw out own-takes)
        

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