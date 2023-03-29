import pygame

from board_properties import BoardProperties as BP


BOARD_BACKGROUND = (46,41,39)


def create_board_backround(screen):
    
    OUTER_BORDER_SIZE = 50
    INNER_BORDER_SIZE = 10
    
    # draw outer background
    screen.fill(BOARD_BACKGROUND)

    # draw inner background
    inner_border_width = 1000 - 2*OUTER_BORDER_SIZE
    pygame.draw.rect(
        surface = screen, 
        color   = BP.COLOUR_VALS["light"], 
        rect    = pygame.Rect(OUTER_BORDER_SIZE, OUTER_BORDER_SIZE, inner_border_width, inner_border_width), 
        width   = INNER_BORDER_SIZE
    )
    
    # draw the dark squares of the board
    board_width = 1000 - 2*INNER_BORDER_SIZE - 2*OUTER_BORDER_SIZE
    board_coord = OUTER_BORDER_SIZE + INNER_BORDER_SIZE
    pygame.draw.rect(
        surface = screen,
        color   = BP.COLOUR_VALS["dark"],
        rect    = pygame.Rect(board_coord, board_coord, board_width, board_width),
        width   = 0
    )
    
    square_width = board_width // 8
    for i in range(8):
        for j in range(4):
            if i % 2 == 0:
                pygame.draw.rect(
                    surface = screen,
                    color   = BP.COLOUR_VALS["light"],
                    rect    = pygame.Rect(board_coord + 2*j*square_width, board_coord + i*square_width, square_width, square_width),
                    width   = 0
                )
            else:
                pygame.draw.rect(
                    surface = screen,
                    color   = BP.COLOUR_VALS["light"],
                    rect    = pygame.Rect(board_coord + (2*j+1)*square_width, board_coord + i*square_width, square_width, square_width),
                    width   = 0
                )


def run_game():
    
    pygame.init()
    
    # Set up the drawing window
    screen = pygame.display.set_mode([1000, 1000])

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        create_board_backround(screen)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()
    
if __name__ == "__main__":
    run_game()