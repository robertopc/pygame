import pygame
import random
import sys
from time import sleep

class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=1, color=(255,0,0)):
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

        self.speed = random.randint(1, 3)
        self.rect = self.image.get_rect()
        self.setColor(color)

    def width(self):
        return self.image.get_width()

    def height(self):
        return self.image.get_height()

    def setColor(self, color=(255, 0, 0)):
        self.image.fill(color)


def main():
    FPS = 30
    SQUARES_AMOUNT = 10
    endgame = False
    enemiesGroup = pygame.sprite.Group()
    activeEvent = ''
    # add enemies to array
    for i in range(SQUARES_AMOUNT):
        # sizeCircle = random.randint(3, 9)
        sizeCircle = 5
        enemyObj = Circle(-1, -1)
        enemiesGroup.add(enemyObj)

    # start the engine
    pygame.init()
    # set the mode of the display
    screen = pygame.display.set_mode([640, 480])
    pygame.display.set_caption("Enemies follow player")
    clock = pygame.time.Clock()
    # firstTime = True
    colorBackground = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))

    #create player sprite
    player = Circle(100, 300, color=(0, 0, 0))


    print(enemiesGroup.sprites())

    while not endgame:
        # check if has active event
        if activeEvent != '':
            # set up a event to queue
            pygame.event.post(activeEvent)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame = True
            else:
                if event.type == pygame.KEYDOWN:
                    # save the event for continuous control
                    activeEvent = event
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        # chech if will colide with walls
                        if player.x - 20 >= 0:
                            # move 20 pixels to left
                            player.x -= 20

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        # chech if will colide with walls
                        if player.width() + player.x + 20 <= screen.get_width():
                            # move 20 pixels to right
                            player.x += 20

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        # chech if will colide with walls
                        if player.y - 20 >= 0:
                            # move 20 pixels to up
                            player.y -= 20

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        # chech if will colide with walls
                        if player.height() + player.y + 20 <= screen.get_height():
                            # move 20 pixels to down
                            player.y += 20

                # if key was released, clear the active event
                if event.type == pygame.KEYUP:
                    activeEvent = ''
        # set a color to background
        screen.fill(colorBackground)

        # enemiesCollide = pygame.sprite.groupcollide(enemiesGroup, enemiesGroup, False, False)
        
        enemiesCollided = pygame.sprite.spritecollideany(player, enemiesGroup)

        if(enemiesCollided != None):
            player.setColor((255, 0, 255))
            # sys.exit()
        else:
            player.setColor((0, 0,0))

        for enemy in enemiesGroup.sprites():

            if(enemy.x > player.x):
                enemy.x -= 1 

            if(enemy.x < player.x):
                enemy.x += 1 

            if(enemy.y > player.y):
                enemy.y -= 1 

            if(enemy.y < player.y):
                enemy.y += 1 

            # draw a surface in the screen
            screen.blit(enemy.image, (enemy.x, enemy.y))

        clock.tick(FPS)
        screen.blit(player.image, (player.x, player.y))
        pygame.display.update()
        # wait 3 seconds to start animations
        # if(firstTime):
        #     sleep(3)
        #     firstTime = False
    pygame.quit()
    

main()