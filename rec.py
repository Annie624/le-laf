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
    items[i] = [None] * 4

items[0][0] = 40
items[0][1] = 50
items[0][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/004-newspaper.png"), (items[0][0], items[0][1])), 0)
items[0][3] = 0 #Can be recycled

items[1][0] = 40
items[1][1] = 50
items[1][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/005-box.png"), (items[1][0], items[1][1])), 0)
items[1][3] = 0 #Can be recycled

items[2][0] = 40
items[2][1] = 50
items[2][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/006-water-bottle.png"), (items[2][0], items[2][1])), 0)
items[2][3] = 0 #Can be recycled

items[3][0] = 40
items[3][1] = 50
items[3][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/007-bag.png"), (items[3][0], items[3][1])), 0)
items[3][3] = 1 #Thrown away

items[4][0] = 40
items[4][1] = 50
items[4][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/018-food.png"), (items[4][0], items[4][1])), 0)
items[4][3] = 2 #Can be composted

items[5][0] = 40
items[5][1] = 50
items[5][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/017-garbage.png"), (items[5][0], items[5][1])), 0)
items[5][3] = 1 #Thrown away

items[6][0] = 40
items[6][1] = 50
items[6][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/015-smartphone.png"), (items[6][0], items[6][1])), 0)
items[6][3] = 0 #Can be recycled



RECYCLING_BIN_HEIGHT = 50
RECYCLING_BIN_IMAGE = pygame.image.load('./mycollection[6188]/png/001-recycle-bin.png')
RECYCLING_BIN = pygame.transform.rotate(pygame.transform.scale(RECYCLING_BIN_IMAGE, (RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)), 0)

itemRect = [None] * 30
def draw_window(newObjectX):
    
    fall = 1
    
    WIN.fill(WHITE)
    WIN.blit(RECYCLING_BIN, (recycle.x, recycle.y))
    j = 0
    for i in fallingObjects:
    
        
        if j == len(fallingObjects) - 1 and newObjectX != -1:
                print(str(newObjectX))
                print(str(WIDTH - 50))
                print(str(i[0]))
                print(str(i[1]))
                itemRect[j] = pygame.Rect(newObjectX, 350, i[0], i[1])
                print("HELLO WORLD")
        itemRect[j].y += fall
        WIN.blit(i[2], (itemRect[j].x, itemRect[j].y))
        j = j + 1
    pygame.display.update()
    newObjectX = -1
    return newObjectX

recycle = pygame.Rect(300, 300, RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)



clock = pygame.time.Clock()
increment = 6000
timer = 0
run = True
numFallingObjects = 0
fallingObjects = []
newObjectX = -1
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    timer += clock.get_time()
    if timer > increment:
        fallingObjects.append(items[random.randint(0, 6)])
        newObjectX = random.randint(0, 400)
        increment = increment + 5000
    newObjectX = draw_window(newObjectX)