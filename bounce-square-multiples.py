import pygame
import random
from time import sleep

def main():
    FPS = 30
    SQUARES_AMOUNT = 100
    endgame = False
    squares = []
    # add squares to array
    for i in range(SQUARES_AMOUNT):
        # sizeSquare = random.randint(3, 9)
        sizeSquare = 5
        squares.append({
            "surface": pygame.Surface((sizeSquare, sizeSquare)), 
            "x": random.randint(0, 630),
            "y": random.randint(0, 470),
            "xDirection": random.randint(0, 1),
            "yDirection": random.randint(0, 1),
            "speed": random.randint(1, 3)
        })

    # start the engine
    pygame.init()
    # set the mode of the display
    screen = pygame.display.set_mode([640, 480])
    pygame.display.set_caption("Bounce multiple squares")
    clock = pygame.time.Clock()
    # firstTime = True
    countBackgroundLimit = 1000
    countBackground = countBackgroundLimit
    colorBackground = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
    while not endgame:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame = True
            else:
                print(event)
        if(countBackground % countBackgroundLimit == 0):
            # set a random background color
            colorBackground = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
            countBackground = 1
        else:
            countBackground += 1

        # set a color to background
        screen.fill(colorBackground)

        for square in squares:
            
            # if direction is cartesian positive
            if(square['xDirection'] > 0 and square['surface'].get_width() + square['x'] + square['speed'] < screen.get_width()):
                square['x'] += square['speed']
            else:
                square['xDirection'] = -1

            if(square['xDirection'] < 0 and square['x'] > 0):
                square['x'] -= square['speed']
            else:
                square['xDirection'] = 1

            # if direction is cartesian positive
            if(square['yDirection'] > 0 and square['surface'].get_height() + square['y'] + square['speed'] < screen.get_height()):
                square['y'] += square['speed']
            else:
                square['yDirection'] = -1

            if(square['yDirection'] < 0 and square['y'] > 0):
                square['y'] -= square['speed']
            else:
                square['yDirection'] = 1

            # draw a surface in the screen
            screen.blit(square['surface'], (square['x'], square['y']))
        pygame.display.update()
        # wait 3 seconds to start animations
        # if(firstTime):
        #     sleep(3)
        #     firstTime = False
    pygame.quit()
    

main()