import pygame
from pygame import mixer
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recycling Game")
WHITE = (255, 255, 255)
FPS = 45

BACKGROUND_WIDTH = 800
BACKGROUND_HEIGHT = 600
BACKGROUND_IMG = pygame.image.load('./mycollection[6188]/png/GameBackground (2).png')
BACKGROUND = pygame.transform.rotate(pygame.transform.scale(BACKGROUND_IMG, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT)), 0)

RECYCLING_BIN_WIDTH = 50
RECYCLING_BIN_HEIGHT = 100
RECYCLING_BIN_IMAGE = pygame.image.load('./mycollection[6188]/png/001-recycle-bin.png')
RECYCLING_BIN = pygame.transform.rotate(pygame.transform.scale(RECYCLING_BIN_IMAGE, (RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)), 0)
BACKGROUND_WIDTH2 = 800
BACKGROUND_HEIGHT2 = 600
BACKGROUND_IMG2 = pygame.image.load('./mycollection[6188]/png/GameBackground (2).png')
BACKGROUND2 = pygame.transform.rotate(pygame.transform.scale(BACKGROUND_IMG2, (BACKGROUND_WIDTH2, BACKGROUND_HEIGHT2)), 0)




RECYCLING_BIN_WIDTH = 50
RECYCLING_BIN_HEIGHT = 100
RECYCLING_BIN_IMAGE = pygame.image.load('./mycollection[6188]/png/001-recycle-bin.png')
RECYCLING_BIN = pygame.transform.rotate(pygame.transform.scale(RECYCLING_BIN_IMAGE, (RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)), 0)


TRASH_BIN_WIDTH = 50
TRASH_BIN_HEIGHT = 100
TRASH_BIN_IMAGE = pygame.image.load('./mycollection[6188]/png/002-trash.png')
TRASH_BIN = pygame.transform.rotate(pygame.transform.scale(TRASH_BIN_IMAGE, (TRASH_BIN_WIDTH, TRASH_BIN_HEIGHT)), 0)


COMPOST_WIDTH = 50
COMPOST_HEIGHT = 100
COMPOST_IMAGE = pygame.image.load('./mycollection[6188]/png/003-composting.png')
COMPOST= pygame.transform.rotate(pygame.transform.scale(COMPOST_IMAGE, (COMPOST_WIDTH, COMPOST_HEIGHT)), 0)




items=[None] * 40
for i in range(40):
   items[i] = [None] * 5

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

for j in range(0, len(items)):
    items[j][4] = j

RECYCLING_BIN_WIDTH = 50
RECYCLING_BIN_HEIGHT = 50
RECYCLING_BIN_IMAGE = pygame.image.load('./mycollection[6188]/png/001-recycle-bin.png')
RECYCLING_BIN = pygame.transform.rotate(pygame.transform.scale(RECYCLING_BIN_IMAGE, (RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)), 0)
recycle = pygame.Rect(300, 500, RECYCLING_BIN_WIDTH, RECYCLING_BIN_HEIGHT)


TRASH_BIN_HEIGHT = 50
TRASH_BIN_IMAGE = pygame.image.load('./mycollection[6188]/png/002-trash.png')
TRASH_BIN = pygame.transform.rotate(pygame.transform.scale(TRASH_BIN_IMAGE, (TRASH_BIN_WIDTH, TRASH_BIN_HEIGHT)), 0)
trash = pygame.Rect(300, 500, TRASH_BIN_WIDTH, TRASH_BIN_HEIGHT)


COMPOST_HEIGHT = 50
COMPOST_IMAGE = pygame.image.load('./mycollection[6188]/png/003-composting.png')
COMPOST = pygame.transform.rotate(pygame.transform.scale(COMPOST_IMAGE, (COMPOST_WIDTH, COMPOST_HEIGHT)), 0)
compost = pygame.Rect(300, 500, COMPOST_WIDTH, COMPOST_HEIGHT)

itemRect = [None] * 500
global points
points = 0
global m
m = True








global life
life = 3
EARTH_WIDTH = 50
EARTH_HEIGHT = 50
EARTH_IMAGE = pygame.image.load('./mycollection[6188]/png/earth.png')
EARTH = pygame.transform.rotate(pygame.transform.scale(EARTH_IMAGE, (EARTH_WIDTH, EARTH_HEIGHT)), 0)
earth1 = pygame.Rect(5, 5, EARTH_WIDTH, EARTH_HEIGHT)
earth2 = pygame.Rect(65, 5, EARTH_WIDTH, EARTH_HEIGHT)
earth3 = pygame.Rect(125, 5, EARTH_WIDTH, EARTH_HEIGHT)


messages = {
0:"Newspaper: Easily recyclable in standard bins, newspapers contribute#to a sustainable cycle when disposed of properly.",
1:"Cardboard boxes: Place these in regular recycling bins to transform#them into new products and minimize environmental impact.",
2:"Plastic Containers: Conveniently recyclable in standard bins, these#containers can be transformed into new items.",
3:"Water bottle: Dispose of in a regular recycling bin to give plastic#bottles a chance to be repurposed.",
4:"Soup Can: Recycle in a standard bin to support the recycling process#and reduce the need for new materials.",
5:"Aluminum: Place aluminum items in regular recycling bins to contribute#to the recycling loop.",
6:"Wine Bottle: Recyclable in regular bins, wine bottles can be#transformed into new glass products.",
7:"Smartphone: While not recyclable in regular bins, consider donating or#selling old smartphones to reduce electronic waste.",
8:"Notebooks: Recyclable in standard bins, notebooks contribute to#sustainable paper usage.",
9:"Textbooks: Place old textbooks in regular recycling bins to promote#responsible disposal.",
10:"Wood: Take wood to recycling centers or repurpose it for building,#as it can't be put in household recycling bins.",
11:"Bubble Wrap: Specific bins at grocery stores are designed for plastic#bag and bubble wrap recycling, ensuring responsible disposal.",
12:"Plastic Bag: Utilize designated bins for plastic bags, as they can't#be recycled in standard recycling bins.",
13:"Broken Glass: Separate broken glass from other recyclables and place#it in a designated box for safe collection.",
14:"VHS Tape: While it cannot be placed in a recycling bin, consider#donating or selling old VHS tapes to reduce waste, as they can't#be recycled in regular bins.",
15:"CDs: Donate or sell old CDs to minimize waste, as they are not#recyclable in regular bins.",
16:"Clothing: Instead of discarding, donate or sell clothing to extend its#use and reduce overall waste.",
17:"Refrigerators: Contact a household waste recycling center for proper#disposal, as refrigerators can't be recycled in standard bins.",
18:"Batteries: Take batteries to designated collection points, like local#Lowes or Home Depot, to ensure safe disposal. Avoid throwing#them in regular bins.",
19:"Full Garbage Bag: Unfortunately, full garbage bags cannot be recycled#and should be disposed of in regular trash bins.",
20:"Chip Bags/Snack Wrappers: Chip bags and snack wrappers cannot be#recycled and should be thrown away in regular trash bins.",
21:"Broken Cables/Cords: Broken cables and cords are not recyclable and#should be disposed of in regular trash bins.",
22:"Markers: Used markers cannot be recycled and should be thrown away#in regular trash bins. Consider looking into marker recycling#programs if available in your area.",
23:"Leftover Food: Instead of discarding, leftover food can be composted,#contributing valuable nutrients to soil.",
24:"Coffee Grounds: After brewing, coffee grounds are excellent for #composting, enriching the compost with organic matter.",
25:"Worms: Live worms can be introduced to a compost bin, aiding in the#decomposition process and enhancing nutrient content.",
26:"Coffee Filter: Compost coffee filters along with coffee grounds,as#they are biodegradable and contribute to compost quality.",
27:"Grass: Grass clippings from lawn maintenance can be composted,#adding a green component to the compost mix.",
28:"Cat Litter: Some types of cat litter, particularly those made from#natural materials like wood or corn, can be composted. However, be#cautious and check for specific guidelines, as some cat litters may#contain materials that are not suitable for composting.",
29:"Soda Can: Easily recyclable in standard bins, soda cans can be turned#into new products.",
}



def endScreen():
   WIN.fill(WHITE)
   background = pygame.Rect(0, 0, BACKGROUND_WIDTH2, BACKGROUND_HEIGHT2)
   WIN.blit(BACKGROUND_IMG2, (background.x, background.y))
   surface = BACKGROUND_IMG2
   color = (102, 186, 109)
   tex = "Score: "+str(points)
   draw_text(tex, pygame.font.SysFont("Roboto", 30), (30, 30, 60), 700, 15)
   draw_text("BETTER LUCK NEXT TIME! ", pygame.font.SysFont("Roboto", 40), (30, 30, 60), 218, 110)
   draw_text("Here are the items you missed: ", pygame.font.SysFont("Roboto", 35), (30, 30, 60), 218, 160)
   pygame.draw.rect(surface, color, pygame.Rect(100, 100, 600, 400))
   d = -20
   
   for i in range(0, 3):
       d += 20
       split = messages[itemsMiss[i]].split('#')
       for j in range(0, len(split)):
           draw_text(split[j], pygame.font.SysFont("Roboto", 25), (30, 30, 60), 110, 200+d)
           d += 20
   draw_text("Press ENTER to restart ", pygame.font.SysFont("Roboto", 30), (30, 30, 60), 280, 460)
   pygame.display.update()






itemsMiss = [None] * 3
def collision(item, bin):
    global points
    global life
   
    if bin == item[3]:
        ping = mixer.Sound("sounds/coin.wav")
        mixer.Sound.play(ping)
        ping.set_volume(0.2)
        points = points + 1
        return False
    else:
        crash = mixer.Sound("sounds/crash.wav")
        mixer.Sound.play(crash)
        life -= 1
        return True
        
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    WIN.blit(img, (x, y))
global textkeeper
textkeeper = 0
global background
background =  background = pygame.Rect(0, 0, BACKGROUND_WIDTH, 1000)

def introScreen():
  WIN.fill(WHITE)
  background = pygame.Rect(0, 0, BACKGROUND_WIDTH2, BACKGROUND_HEIGHT2)
  WIN.blit(BACKGROUND_IMG2, (background.x, background.y))
  surface = BACKGROUND_IMG2
  color = (102, 186, 109)
  pygame.draw.rect(surface, color, pygame.Rect(100, 100, 600, 400))
  draw_text("WELCOME TO ECOSORT! ", pygame.font.SysFont("Roboto", 40), (30, 30, 60), 250, 110)
  draw_text("Your mission is to guide our eco-hero through various levels, sorting waste into the", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 150)
  draw_text("correct bins - Recyclable, Compostable, and Trash. Each correct descision helps protect the", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 165)
  draw_text("environment and earns you points, but beware of any sorting mistakes that could destroy ", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 180)
  draw_text("your 3 Earth lives!", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 195)
  draw_text("SORTING GUIDLINES", pygame.font.SysFont("Roboto", 25), (30, 30, 60), 320, 225)
  draw_text("Recyclables:", pygame.font.SysFont("Roboto", 23), (30, 30, 60), 110, 245)
  draw_text("Items in this category consist of plastics, paper, and cardboard. Some other items may not", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 265)
  draw_text("be any of those, but can be “upcycled”, or donated. Put these in recycling.", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 280)
  draw_text("Compost:", pygame.font.SysFont("Roboto", 23), (30, 30, 60), 110, 300)
  draw_text("Food scraps, yard waste, and other objects that are able to break down into organic ", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 320)
  draw_text("materials fit in this category", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 335)
  draw_text("Trash:", pygame.font.SysFont("Roboto", 23), (30, 30, 60), 110, 355)
  draw_text("Some plastics, such as food wrappers cannot be recycled and must be thrown away. Also", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 375)
  draw_text("consider items that are broken or too mixed together to be recycled or composted.", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 390)
  draw_text("CONTROLS", pygame.font.SysFont("Roboto", 25), (30, 30, 60), 350, 420)
  draw_text("Use the left and right arrow keys to catch the item in their respective can. To switch bins,", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 445)
  draw_text("1 = recycling, 2 = trash, and 3 = compost. Press ENTER to begin!", pygame.font.SysFont("Roboto", 20), (30, 30, 60), 110, 460)
  pygame.display.update()




def draw_window(newObjectX, direction, binType):
    global points
    global textkeeper
    global life
    global fallingObjects
    fall = 1
    global m
    global background
    WIN.fill(WHITE)
    background = pygame.Rect(0, 0, BACKGROUND_WIDTH, BACKGROUND_HEIGHT)
    WIN.blit(BACKGROUND_IMG, (background.x, background.y))
    if not((recycle.x > 740 and direction == 1) or (recycle.x < 10 and direction == -1)):
        recycle.x += direction * 6
    if binType == 0:
       WIN.blit(RECYCLING_BIN, (recycle.x, recycle.y))
       boo = -1
    elif binType == 1:
       WIN.blit(TRASH_BIN, (recycle.x, recycle.y))
       boo = -1
    else:
       WIN.blit(COMPOST, (recycle.x, recycle.y))
       boo = -1


    if life == 3:
        WIN.blit(EARTH, (earth1.x, earth1.y))
        WIN.blit(EARTH, (earth2.x, earth2.y))
        WIN.blit(EARTH, (earth3.x, earth3.y))
    elif life == 2:
        WIN.blit(EARTH, (earth1.x, earth1.y))
        WIN.blit(EARTH, (earth2.x, earth2.y))
    elif life == 1:
        WIN.blit(EARTH, (earth1.x, earth1.y))
        
    boo = -1
    j = 0
    for i in fallingObjects:
        points2 = points
        if j == len(fallingObjects) - 1 and newObjectX != -1:
                itemRect[j] = pygame.Rect(newObjectX, 50, i[0], i[1])
        itemRect[j].y += fall
        WIN.blit(i[2], (itemRect[j].x, itemRect[j].y))
        boo3 = False
        if (((itemRect[j].x-recycle.x)**2 + (itemRect[j].y-recycle.y)**2)**0.5 < 30):
                boo3 = collision(fallingObjects[j], binType)
                boo = j
        if points2 < points:
            draw_text("Nice one!", pygame.font.SysFont("Arial", 30), (30, 30, 60), 220, 220)
            textkeeper = 10000000
            m = True
        elif boo3 == True:
            draw_text("Boo!", pygame.font.SysFont("Arial", 30), (30, 30, 60), 220, 220)
            textkeeper = 1000000
            m = False
            if (life < 0):
                life = 0
            itemsMiss[life - 1] = i[4]
        else:
            if points2 == points and textkeeper > 0:
                textkeeper = textkeeper - 1
                if m == True:
                    draw_text("Nice one!", pygame.font.SysFont("Arial", 30), (30, 30, 60), 220, 220)
                if m == False:
                    draw_text("Boo!", pygame.font.SysFont("Arial", 30), (30, 30, 60), 220, 220)


        if itemRect[j].y > 550:
            boo = j
            life -= 1
            itemsMiss[life - 1] = i[4]
            crash = mixer.Sound("sounds/crash.wav")
            mixer.Sound.play(crash)
        j = j + 1
    if (boo != -1):
        fallingObjects.pop(boo)
        itemRect.pop(boo)
    tex = "Score: "+str(points)
    r = 200
    g = 100
    b = 100
    if (points < 51):
        r = r - points * 4
        g = g + points * 3
        b = b - points * 2
    else:
        r = r - 50 * 4
        g = g + 50 * 3
        b = b - 50 * 2
    draw_text(tex, pygame.font.SysFont("Roboto", 30), (r, g, b), 700, 15)
    pygame.display.update()
    newObjectX = -1
    return newObjectX


def fail():
    global textkeeper
    textkeeper = 0
    mixer.music.stop()
    failure = mixer.Sound("sounds/lose.wav")
    failure.set_volume(0.3)
    mixer.Sound.play(failure)
    global background
    global fallingObjects
    fallingObjects = []
    WIN.fill(WHITE)
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 0 
        endScreen()

        


global fallingObjects
fallingObjects = []

clock2 = pygame.time.Clock()

def loop():
    global points
    points = 0
    global fallingObjects
    increment = 4000
    timer = 0
    intro = True
    newObjectX = -1
    direction = 0
    binType = 0
    global life

    while intro:
        global life
        life = 3
        introScreen()
        clock2.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    WIN.fill(WHITE)
                    pygame.display.update()
                    intro = False
            if event.type == pygame.QUIT:
                exit(99)
    mixer.init()
    mixer.music.load('sounds/song.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = -1
                if event.key == pygame.K_RIGHT:
                    direction = 1
                if event.key == pygame.K_1:
                    binType = 0
                if event.key == pygame.K_2:
                    binType = 1
                if event.key == pygame.K_3:
                    binType = 2
        if life <= 0:
            return 0
        timer += clock.get_time()
        if timer > increment:
            fallingObjects.append(items[random.randint(0, 29)])
            newObjectX = random.randint(0, 740)
            increment = increment + 2100
        draw_window(newObjectX, direction, binType)


while True:
    a = loop()
    if a == 1:
        exit(0)
    elif a == 0:
        b = fail()
        if b == 1:
            exit(0)
        a = 1
