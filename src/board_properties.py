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
