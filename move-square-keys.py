import pygame
import random

def main():
    #inicia o jogo
    pygame.init()
    # cria o modo de tela
    screen = pygame.display.set_mode([640, 480])
    pygame.display.set_caption("Move square with arrow keys")
    clock = pygame.time.Clock()
    FPS = 30
    endgame = False
    surf01 = pygame.Surface((100,100))
    x = y = 0
    activeEvent = ''
    colorBackground = (128, 128, 128)
    while not endgame:
        # check if has active event
        if activeEvent != '':
            # set up a event to queue
            pygame.event.post(activeEvent)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                endgame = True
            else:
                if event.type == pygame.KEYDOWN:
                    # save the event for continuous control
                    activeEvent = event
                    if event.key == pygame.K_LEFT:
                        # chech if will colide with walls
                        if x - 20 >= 0:
                            # move 20 pixels to left
                            x -= 20

                    if event.key == pygame.K_RIGHT:
                        # chech if will colide with walls
                        if surf01.get_width() + x + 20 <= screen.get_width():
                            # move 20 pixels to right
                            x += 20

                    if event.key == pygame.K_UP:
                        # chech if will colide with walls
                        if y - 20 >= 0:
                            # move 20 pixels to up
                            y -= 20

                    if event.key == pygame.K_DOWN:
                        # chech if will colide with walls
                        if surf01.get_height() + y + 20 <= screen.get_height():
                            # move 20 pixels to down
                            y += 20

                # if key was released, clear the active event
                if event.type == pygame.KEYUP:
                    activeEvent = ''

        clock.tick(FPS)
        screen.fill(colorBackground)
        # draw a surface in the screen
        screen.blit(surf01, (x, y))
        pygame.display.update()
    pygame.quit()

main()