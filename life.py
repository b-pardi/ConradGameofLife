import pygame
import time
import numpy as np
import screeninfo
import math

clock = pygame.time.Clock()
FPS = 120

# background color given as rgb vals
BACKGROUND = (10, 10, 10)
GRID_CLR = (60, 60, 60)
WILL_LIVE_CLR = (255, 255, 255) 
WILL_DIE_CLR = (150, 150, 150)

CELL_SIZE = 10
SCREEN_SIZE_SCALAR = 0.6

monitor = screeninfo.get_monitors()[0]
screen_width, screen_height = math.floor(SCREEN_SIZE_SCALAR*monitor.width), math.floor(SCREEN_SIZE_SCALAR*monitor.height)

def update(screen, cells, size, next_gen=False):
    # create empty list to update previous generation
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    # iterate through each individual cell in 2d array
    for row, col in np.ndindex(cells.shape):
        # game rules
        # check cells from surrounding current cell to see how many are alive
        # +2 because of how python slices list, first slice ind included, second not
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = BACKGROUND if cells[row, col] == 0 else WILL_LIVE_CLR
        

        # only need to check currently alive cells
        if cells[row, col] == 1:
            # if alone or 1 neighbor, dies of loneliness
            # if 2 or 3 neighbors, lives
            # if 3 neighbors, reproduce
            # if > 3 neighbors, dies from over population
            if alive < 2 or alive > 3:
                if next_gen == True:
                    color = WILL_DIE_CLR
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if next_gen:
                    #maybe doint ned?
                    color = WILL_LIVE_CLR

        # update a currently empty cell with enough alive neighbors
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if next_gen:
                    color = WILL_LIVE_CLR

        pygame.draw.rect(screen, color, (col*size, row*size, size - 1, size - 1))

    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Conrad's Game of LIFE")
    
    # dim of cells flipped from dim of screen
    cells = np.zeros((screen_height // CELL_SIZE, screen_width // CELL_SIZE))
    # initially fill empty cells in screen
    screen.fill(GRID_CLR)
    update(screen, cells, CELL_SIZE)

    pygame.display.flip()
    pygame.display.update()

    # initially not running, key press will start game
    running = False
    while 1:
        for event in pygame.event.get():
            # equivalent to closing the game
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = not running
                    update(screen, cells, CELL_SIZE)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                mpos = pygame.mouse.get_pos()
                cells[mpos[1] // CELL_SIZE, mpos[0] // CELL_SIZE] = 1
                update(screen, cells, CELL_SIZE)
                pygame.display.update()

        screen.fill(GRID_CLR)

        if running:
            cells = update(screen, cells, CELL_SIZE, next_gen=True)
            pygame.display.update()

        clock.tick(FPS)

if __name__ == "__main__":
    main()