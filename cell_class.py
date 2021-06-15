import pygame

class Cell:
    def __init__(self, surface, gridX, gridY):
        self.alive = False
        self.surface = surface
        self.gridX = gridX
        self.gridY = gridY
        self.cell_size = 20
        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.gridX * self.cell_size, self.gridY * self.cell_size)

    def draw(self):
        if(self.alive == True):
            self.image.fill((0, 0, 0))
        else:
            self.image.fill((0, 0, 0))
            pygame.draw.rect(self.image, (255, 255, 255), (1 ,1, self.cell_size - 2, self.cell_size - 2))

        self.surface.blit(self.image, (self.gridX * self.cell_size, self.gridY * self.cell_size))