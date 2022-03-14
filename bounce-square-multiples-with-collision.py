import pygame
import random
from time import sleep

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, xDirection, yDirection, speed=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        if x < 0:
            self.x = random.randint(0, 630)
        else:
            self.x = x

        if y < 0:
            self.y = random.randint(0, 470)
        else:
            self.y = y

        if xDirection == '':
            self.xDirection = random.randint(0, 1)
        else:
            self.xDirection = xDirection

        if yDirection == '':
            self.yDirection = random.randint(0, 1)
        else:
            self.yDirection = yDirection
        self.speed = speed
        self.rect = self.image.get_rect()
        pass


def main():
    FPS = 30
    SQUARES_AMOUNT = 10
    endgame = False
    squares = []
    squaresGroup = pygame.sprite.Group()
    # add squares to array
    for i in range(SQUARES_AMOUNT):
        # sizeSquare = random.randint(3, 9)
        sizeSquare = 5
        squareObj = Square(-1, -1, '', '')
        squares.append(squareObj)
        squaresGroup.add(squareObj)

    # start the engine
    pygame.init()
    # set the mode of the display
    screen = pygame.display.set_mode([640, 480])
    pygame.display.set_caption("Bounce multiple squares with collission")
    clock = pygame.time.Clock()
    # firstTime = True
    colorBackground = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
    while not endgame:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame = True
        # set a color to background
        screen.fill(colorBackground)

        # squaresCollide = pygame.sprite.groupcollide(squaresGroup, squaresGroup, False, False)

        # for square in squaresCollide:
        #     square.image.fill((255, 255, 0))
        #     # square2.image.fill(random_color)

        for square in squares:

            squaresGroup2 = squaresGroup.copy()
            squaresGroup2.remove(square)

            for square2 in squaresGroup2:
                print((square,square2))
                if pygame.sprite.collide_rect(square, square2):
                    square.image.fill((255, 0, 0))

            squaresGroup2.empty()

            # if direction is cartesian positive
            if(square.xDirection > 0 and square.image.get_width() + square.x + square.speed < screen.get_width()):
                square.x += square.speed
            else:
                square.xDirection = -1

            if(square.xDirection < 0 and square.x > 0):
                square.x -= square.speed
            else:
                square.xDirection = 1

            # if direction is cartesian positive
            if(square.yDirection > 0 and square.image.get_height() + square.y + square.speed < screen.get_height()):
                square.y += square.speed
            else:
                square.yDirection = -1

            if(square.yDirection < 0 and square.y > 0):
                square.y -= square.speed
            else:
                square.yDirection = 1

            # draw a surface in the screen
            screen.blit(square.image, (square.x, square.y))
        pygame.display.update()
        # wait 3 seconds to start animations
        # if(firstTime):
        #     sleep(3)
        #     firstTime = False
    pygame.quit()
    

main()