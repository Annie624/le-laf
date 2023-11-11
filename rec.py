import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recycling Game")
WHITE = (255, 255, 255)
FPS = 60

RECYCLING_BIN_WIDTH = 80
RECYCLING_BIN_HEIGHT = 100
RECYCLING_BIN_IMAGE = pygame.image.load('./mycollection[6188]/png/001-recycle-bin.png')
RECYCLING_BIN = pygame.transform.rotate(pygame.transform.scale(RECYCLING_BIN_IMAGE, (RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)), 0)

items=[None] * 10
for i in range(10):
    items[i] = [None] * 3

items[0][0] = 40
items[0][1] = 50
items[0][2] = pygame.image.load('./mycollection[6188]/png/004-newspaper.png')

RECYCLING_BIN_HEIGHT = 50
RECYCLING_BIN_IMAGE = pygame.image.load('./mycollection[6188]/png/004-newspaper.png')
RECYCLING_BIN = pygame.transform.rotate(pygame.transform.scale(RECYCLING_BIN_IMAGE, (RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)), 0)


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(RECYCLING_BIN, (recycle.x, recycle.y))
    pygame.display.update()

recycle = pygame.Rect(300, 400, RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw_window()