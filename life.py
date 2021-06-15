import pygame
import sys
from game_window_class import *

# screen size
WIDTH, HEIGHT = 1000, 700
# background color given as rgb vals
BACKGROUND = (0, 100, 100)
FPS = 60

# returns list of all events since its last call
def get_events():
    global running
    for event in pygame.event.get():
        # equivalent to closing the game
        if event.type == pygame.QUIT:
            running = False

def update():
    game_window.update()

def draw():
    window.fill(BACKGROUND)
    game_window.draw()

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#window to draw on, x, y coords of top left corner
game_window = Game_Window(window, 180, 80)

running = True
while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()