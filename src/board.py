

class BoardProperties():
    
    # all file and rank labels
    FILES = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    RANKS = {'1', '2', '3', '4', '5', '6', '7', '8'}
    
    # number of files and ranks
    N_FILES = len(FILES)
    N_RANKS = len(RANKS)
    
    # static method for find the colour of a square
    @staticmethod
    def get_square_colour(file, rank):
        # if the file is odd
        if (ord(file) - 96) % 2:
            # if the rank is odd
            if int(rank) % 2:
                return "black"
            # if the rank is even
            else:
                return "white"
        # if the file is even
        else:
            # if the rank is odd
            if int(rank) % 2:
                return "white"
            # if the rank is even
            else:
                return "black"

class Board(BoardProperties):
    
    # instantiate class
    def __init__(self) -> None:
        """ Instantiate board object
        """
        
class Square(BoardProperties):
    
    # instantiate class
    def __init__(self, file: str, rank: str) -> None:
        self.file_label = file
        self.rank_label = rank
    
    @property
    def file_label(self) -> str:
        return self._file_label
    
    @file_label.setter
    def file_label(self, file) -> None:
        # add code to check that choice makes sense
        self._file_label = file
    
    @property
    def rank_label(self) -> str:
        return self._rank_label
    
    @rank_label.setter
    def rank_label(self, rank) -> None:
        # add code to check that choice makes sense
        self._rank_label = rank
    
    @property
    def contents(self) -> None: #update type hint
        return self._contents
    
    @contents.setter
    def contents(self, piece):
        self._contents = piece
        