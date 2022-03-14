import pygame
import random

def main():
    #inicia o jogo
    pygame.init()
    # cria o modo de tela
    screen = pygame.display.set_mode([640, 480])
    pygame.display.set_caption("Bounce square")
    clock = pygame.time.Clock()
    FPS = 30
    endgame = False
    surf01 = pygame.Surface((100,100))
    x = y = 1
    xDirection = yDirection = 1
    color_random = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
    while not endgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame = True
            else:
                print(event)
        clock.tick(FPS)
        # set a random background color
        screen.fill(color_random)
        # draw a surface in the screen
        screen.blit(surf01, (x, y))

        # if direction is cartesian positive
        if(xDirection > 0 and surf01.get_width() + x + 1 < screen.get_width()):
            x += 1
        else:
            xDirection = -1

        if(xDirection < 0 and x > 0):
            x -= 1
        else:
            xDirection = 1

        # if direction is cartesian positive
        if(yDirection > 0 and surf01.get_height() + y + 1 < screen.get_height()):
            y += 1
        else:
            yDirection = -1

        if(yDirection < 0 and y > 0):
            y -= 1
        else:
            yDirection = 1

        pygame.display.update()
    pygame.quit()

main()