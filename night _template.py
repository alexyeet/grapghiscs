# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# imports
import pygame
import random
from random import randint

# initialize game engine
pygame.init()

# window
SIZE = (800, 600)
TITLE = "Night"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# timer
clock = pygame.time.Clock()
refresh_rate = 60

# colors
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 200)
DARK_GREEN = (38, 66, 33)
DARK_GREY = (40, 40, 40)
MED_GREY = (150, 150, 150)
LIGHT_GREY = (225, 225, 225)
ORANGE = (232, 145, 53)

#make snow
snow_dark = []
for i in range (100):
    x = random.randrange(0, 800)
    y = random.randrange(0, 150)
    r = random.randrange(1, 3)
    sd = [x, y, r, r]
    snow_dark.append(sd)

snow_med = []
for i in range (100):
    x = random.randrange(0, 800)
    y = random.randrange(140, 300)
    r = random.randrange(1, 3)
    sm = [x, y, r, r]
    snow_med.append(sm)

snow_light = []
for i in range (100):
    x = random.randrange(0, 800)
    y = random.randrange(290, 400)
    r = random.randrange(1, 3)
    sl = [x, y, r, r]
    snow_light.append(sl)

#make snowman
def draw_snowman(x, y):
    pygame.draw.ellipse(screen, LIGHT_GREY, [x, y, 30, 30])
    pygame.draw.ellipse(screen, LIGHT_GREY, [x+4, y-20, 25, 25])
    pygame.draw.ellipse(screen, LIGHT_GREY, [x+7, y-35, 20, 20])
    pygame.draw.ellipse(screen, BLACK, [x+14, y-5, 2, 1])
    pygame.draw.ellipse(screen, BLACK, [x+14, y-10, 2, 1])
    pygame.draw.ellipse(screen, BLACK, [x+14, y-15, 2, 1])
    pygame.draw.polygon(screen, ORANGE, [[x+15, y-25], [x+20, y-23], [x+15, y-21]])
    pygame.draw.ellipse(screen, BLACK, [x+12, y-28, 2, 1])
    pygame.draw.ellipse(screen, BLACK, [x+18, y-28, 2, 1])

    

# game loop
done = False

while not done:
    # event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # drawing code
    ''' sky '''
    screen.fill(BLACK)

    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, WHITE, [0, 400, 800, 200])

    ''' snow '''

    for sd in snow_dark:
        pygame.draw.ellipse(screen, DARK_GREY, sd)
    for sm in snow_med:
        pygame.draw.ellipse(screen, MED_GREY, sm)
    for sl in snow_light:
        pygame.draw.ellipse(screen, LIGHT_GREY, sl)

    ''' draw house '''
    pygame.draw.rect(screen, DARK_GREEN, [450, 300, 200, 120])
    pygame.draw.polygon(screen, DARK_GREY, [(420, 300), (550, 250), (670, 300)])
    pygame.draw.rect(screen, DARK_GREY, [530, 350, 40, 70])
    pygame.draw.ellipse(screen, LIGHT_GREY, [560, 380, 5, 5])
        
 
    draw_snowman(200, 400)
    draw_snowman(400, 500)
    draw_snowman(250, 460)



    # update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# close window on quit
pygame.quit()
