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

BACKGROUND_WIDTH = 800
BACKGROUND_HEIGHT = 600
BACKGROUND_IMG = pygame.image.load('./mycollection[6188]/png/GameBackground (2).png')
BACKGROUND = pygame.transform.rotate(pygame.transform.scale(BACKGROUND_IMG, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT)), 0)


RECYCLING_BIN_WIDTH = 50
RECYCLING_BIN_HEIGHT = 100
RECYCLING_BIN_IMAGE = pygame.image.load('./mycollection[6188]/png/001-recycle-bin.png')
RECYCLING_BIN = pygame.transform.rotate(pygame.transform.scale(RECYCLING_BIN_IMAGE, (RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)), 0)


items=[None] * 40
for i in range(40):
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
items[2][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/008-box-1.png"), (items[2][0], items[2][1])), 0)
items[2][3] = 0 #Can be recycled


items[3][0] = 40
items[3][1] = 50
items[3][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/006-water-bottle.png"), (items[3][0], items[3][1])), 0)
items[3][3] = 0 #Can be recycled


items[4][0] = 40
items[4][1] = 50
items[4][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/010-soup.png"), (items[4][0], items[4][1])), 0)
items[4][3] = 0 #Can be recycled


items[5][0] = 40
items[5][1] = 50
items[5][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/011-aluminum.png"), (items[5][0], items[5][1])), 0)
items[5][3] = 0 #Can be recycled


items[6][0] = 40
items[6][1] = 50
items[6][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/012-wine-bottles.png"), (items[6][0], items[6][1])), 0)
items[6][3] = 0 #Can be recycled


items[7][0] = 40
items[7][1] = 50
items[7][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/015-smartphone.png"), (items[7][0], items[7][1])), 0)
items[7][3] = 0 #Can be recycled


items[8][0] = 40
items[8][1] = 50
items[8][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (1)[6189]/png/011-book.png"), (items[8][0], items[8][1])), 0)
items[8][3] = 0 #Can be recycledC:\Users\annie\OneDrive\Documents\Code\Other_projects\le-laf\mycollection (1)[6189]\png\011-book.png


items[9][0] = 40
items[9][1] = 50
items[9][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (1)[6189]/png/012-textbook.png"), (items[9][0], items[9][1])), 0)
items[9][3] = 0 #Can be recycled


items[10][0] = 40
items[10][1] = 50
items[10][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (1)[6189]/png/013-wood.png"), (items[10][0], items[10][1])), 0)
items[10][3] = 0 #Can be recycled


items[11][0] = 40
items[11][1] = 50
items[11][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (1)[6189]/png/014-bubble-wrap.png"), (items[11][0], items[11][1])), 0)
items[11][3] = 0 #Can be recycled


items[12][0] = 40
items[12][1] = 50
items[12][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/007-bag.png"), (items[12][0], items[12][1])), 0)
items[12][3] = 0 #Can be recycled


items[13][0] = 40
items[13][1] = 50
items[13][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (1)[6189]/png/001-broken-glass.png"), (items[13][0], items[13][1])), 0)
items[13][3] = 0 #Can be recycled


items[14][0] = 40
items[14][1] = 50
items[14][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (2)[6190]/png/001-vhs.png"), (items[14][0], items[14][1])), 0)
items[14][3] = 0 #Can be recycled


items[15][0] = 40
items[15][1] = 50
items[15][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (2)[6190]/png/005-cds.png"), (items[15][0], items[15][1])), 0)
items[15][3] = 0 #Can be recycled


items[16][0] = 40
items[16][1] = 50
items[16][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (2)[6190]/png/007-male-clothes.png"), (items[16][0], items[16][1])), 0)
items[16][3] = 0 #Can be recycled


items[17][0] = 40
items[17][1] = 50
items[17][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (2)[6190]/png/004-refridgerator.png"), (items[17][0], items[17][1])), 0)
items[17][3] = 0 #Can be recycled


items[18][0] = 40
items[18][1] = 50
items[18][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/013-battery.png"), (items[18][0], items[18][1])), 0)
items[18][3] = 0 #Can be recycled


items[19][0] = 40
items[19][1] = 50
items[19][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/017-garbage.png"), (items[19][0], items[19][1])), 0)
items[19][3] = 1 #Should be thrown out


items[20][0] = 40
items[20][1] = 50
items[20][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (1)[6189]/png/002-snack.png"), (items[20][0], items[20][1])), 0)
items[20][3] = 1 #Should be thrown out


items[21][0] = 40
items[21][1] = 50
items[21][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (2)[6190]/png/006-broken-wire.png"), (items[21][0], items[21][1])), 0)
items[21][3] = 1 #Should be thrown out


items[22][0] = 40
items[22][1] = 50
items[22][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (2)[6190]/png/003-highlighter.png"), (items[22][0], items[22][1])), 0)
items[22][3] = 1 #Should be thrown out


items[23][0] = 40
items[23][1] = 50
items[23][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/018-food.png"), (items[23][0], items[23][1])), 0)
items[23][3] = 2 #Can be composted


items[24][0] = 40
items[24][1] = 50
items[24][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/019-ground-coffee.png"), (items[24][0], items[24][1])), 0)
items[24][3] = 2 #Can be composted


items[25][0] = 40
items[25][1] = 50
items[25][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (1)[6189]/png/009-worm.png"), (items[25][0], items[25][1])), 0)
items[25][3] = 2 #Can be composted


items[26][0] = 40
items[26][1] = 50
items[26][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (1)[6189]/png/007-coffee-filter.png"), (items[26][0], items[26][1])), 0)
items[26][3] = 2 #Can be composted


items[27][0] = 40
items[27][1] = 50
items[27][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (1)[6189]/png/006-grass.png"), (items[27][0], items[27][1])), 0)
items[27][3] = 2 #Can be composted


items[28][0] = 40
items[28][1] = 50
items[28][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection (1)[6189]/png/010-litter-box.png"), (items[28][0], items[28][1])), 0)
items[28][3] = 2 #Can be composted


items[29][0] = 40
items[29][1] = 50
items[29][2] = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./mycollection[6188]/png/009-beer.png"), (items[29][0], items[29][1])), 0)
items[29][3] = 0 #Can be recycled


RECYCLING_BIN_HEIGHT = 50
RECYCLING_BIN_IMAGE = pygame.image.load('./mycollection[6188]/png/001-recycle-bin.png')
RECYCLING_BIN = pygame.transform.rotate(pygame.transform.scale(RECYCLING_BIN_IMAGE, (RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)), 0)
recycle = pygame.Rect(300, 500, RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)
itemRect = [None] * 500
global points
points = 0
global m 
m = True






def collision(item, bin):
    global points
    if bin == item[3]:
        points = points + 1
    else:
        points = points - 1
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    WIN.blit(img, (x, y))
global textkeeper
textkeeper = 0
def draw_window(newObjectX, direction):
    global points
    global textkeeper
    points2 = points
    fall = 1
    global m
    WIN.fill(WHITE)
    background = pygame.Rect(0, 0, BACKGROUND_WIDTH, BACKGROUND_HEIGHT)
    WIN.blit(BACKGROUND_IMG, (background.x, background.y))

    recycle.x += direction * 5
    WIN.blit(RECYCLING_BIN, (recycle.x, recycle.y))
    boo = -1
    j = 0
    for i in fallingObjects:
        if j == len(fallingObjects) - 1 and newObjectX != -1:
                itemRect[j] = pygame.Rect(newObjectX, 50, i[0], i[1])
        itemRect[j].y += fall
        WIN.blit(i[2], (itemRect[j].x, itemRect[j].y))
        if (((itemRect[j].x-recycle.x)**2 + (itemRect[j].y-recycle.y)**2)**0.5 < 30):
            collision(fallingObjects[j], 0)
            boo = j
        if points2 < points:
            draw_text("Nice one!", pygame.font.SysFont("Arial", 30), (30, 30, 60), 220, 220)
            textkeeper = 10000000
            m = True
        elif points2 > points:
            draw_text("Boo!", pygame.font.SysFont("Arial", 30), (30, 30, 60), 220, 220)
            textkeeper = 1000000
            m = False
        else:
            if points2 == points and textkeeper > 0:
                textkeeper = textkeeper - 1
                if m == True:
                    draw_text("Nice one!", pygame.font.SysFont("Arial", 30), (30, 30, 60), 220, 220)
                if m == False:
                    draw_text("Boo!", pygame.font.SysFont("Arial", 30), (30, 30, 60), 220, 220)


        if itemRect[j].y > 550:
            boo = j
        j = j + 1
    if (boo != -1):
        fallingObjects.pop(boo)
        itemRect.pop(boo)
    pygame.display.update()
    newObjectX = -1
    return newObjectX





clock = pygame.time.Clock()
increment = 4000
run = True
timer = 0
numFallingObjects = 0
fallingObjects = []
newObjectX = -1
direction = 0
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = -1
            if event.key == pygame.K_RIGHT:
                direction = 1
    timer += clock.get_time()
    if timer > increment:
        fallingObjects.append(items[random.randint(0, 29)])
        newObjectX = random.randint(0, 400)
        increment = increment + 1000
    newObjectX = draw_window(newObjectX, direction)