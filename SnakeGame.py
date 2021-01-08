import pygame
import sys
import random
from pygame.math import Vector2


class Fruit:

    def __init__(self):
        self.randomise()

    def randomise(self):
        self.x = random.randint(0, cell_no - 1)
        self.y = random.randint(0, cell_no - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


pygame.init()
cell_size = 40
cell_no = 20
screen = pygame.display.set_mode((cell_size*cell_no, cell_size*cell_no))
clock = pygame.time.Clock()
fruit = Fruit()

while(True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)
