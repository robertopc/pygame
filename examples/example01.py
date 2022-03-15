"""
Example extracted from stackoverflow
https://stackoverflow.com/questions/46613533/pygame-sprite-spritecollide-doesnt-work-with-moving-sprite-group
"""
import pygame as pg
import random
import sys

a_white = (245, 245, 245)
a_red = (10, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
blue_grey = (51, 93, 127)
dark_red = (85, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
bg_color = dark_red

width = 600
height = 500
FPS = 60

p_width = 70
p_height = 70
c_width = 35
c_height = 35
score = 0
level = 0
lives = 3

cwd = sys.path[0]
title = 'This Is My Game!'
pg.init()
pg.mixer.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((width, height))
pg.display.set_caption(title)
font_name = pg.font.match_font("arial")
coin_img = pg.image.load(cwd+'/assets/coin3.png').convert()
player_img = pg.image.load(cwd+'/assets/smiley.png').convert_alpha()
gegner_1 = pg.image.load(cwd+'/assets/gegner_black.png').convert_alpha()
coin_snd = pg.mixer.Sound(cwd+'/assets/coin_snd_2.ogg')


def new_coin():
    x = random.randrange(c_width, width - c_width)
    y = random.randrange(c_height, height - c_height)
    coins = Coin(x, y)
    all_sprites.add(player, coins)
    coin_group.add(coins)


def draw_text(screen, text, t_color, size, t_x, t_y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, t_color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (t_x, t_y)
    screen.blit(text_surface, text_rect)


def start_screen():
    screen.fill(bg_color)
    draw_text(screen, 'Welcome... !', white, 75, width / 2, height / 4 - 100)
    draw_text(screen, 'ready to play my game*?', white, 24, width - 150, height / 4 - 20)
    draw_text(screen, "Press any key to begin", white, 20, width / 2 + 60, height / 4 + 10)
    draw_text(screen, "*The  name of the game is \'MY GAME\'  but  that ",
              white, 16, width / 2, height - 150)
    draw_text(screen, " has nothing to do  with the fact, that the game is", white, 16, width / 2, height - 130)
    draw_text(screen, "  my  game. Yes, the  game is actually  my game, ", white, 16, width / 2, height - 110)
    draw_text(screen, " but  that\'s not the reason I named  it  my  game. ", white, 16, width / 2, height - 90)
    draw_text(screen, "...or is it?", white, 13, width - 28, height - 20)
    pg.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYUP:
                waiting = False


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_orig = pg.transform.scale(player_img, (p_width, p_height))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2), (height / 2)
        self.radius = 35

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.rect.x += 5
        if keys[pg.K_LEFT]:
            self.rect.x -= 5
        if keys[pg.K_UP]:
            self.rect.y -= 5
        if keys[pg.K_DOWN]:
            self.rect.y += 5

        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height


class Coin(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(coin_img, (c_width, c_height))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = 18


class Gegner_1(pg.sprite.Sprite):
    def __init__(self, x, y, yon):
        super().__init__()
        self.image_orig = pg.transform.scale(gegner_1, (p_width, p_height))
        self.image_orig.set_colorkey(white)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = 35
        self.yon = yon
        if yon == 'yes':
            self.speedx = 5
            self.speed = self.speedx
        elif yon == 'no':
            self.speedy = 5
            self.speed = self.speedy

    def update(self):
        if self.yon == 'yes':
            self.rect.x += self.speed
        if self.yon == 'no':
            self.rect.y += self.speed
        if self.rect.right > width:
            self.speed = -5
        if self.rect.left == 0:
            self.speed = 5
        if self.rect.bottom > height:
            self.speed = -5
        if self.rect.top < 0:
            self.speed = 5


all_sprites = pg.sprite.Group()
coin_group = pg.sprite.Group()
enemys_group = pg.sprite.Group()
player = Player()
gegner1 = Gegner_1(0, 60, 'yes')
gegner2 = Gegner_1(width, 350, 'yes')
gegner3 = Gegner_1(50, p_height, 'no')
gegner4 = Gegner_1(width - p_width - 20, p_height, 'no')

enemys_group.add(gegner1, gegner2, gegner3, gegner4)
all_sprites.add(player)

for c in range(3):
    new_coin()

start_game = True
game_over = False
done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    if start_game:
        start_screen()
        start_game = False

    screen.fill(bg_color)
    if score >= 5:
        all_sprites.add(gegner1)
        if score >= 10:
            all_sprites.add(gegner2)
            if score >= 15:
                all_sprites.add(gegner3)
                if score >= 20:
                    all_sprites.add(gegner4)

    all_sprites.draw(screen)
    all_sprites.update()

    draw_text(screen, 'SCORE: ' + str(score), white, 20, 55, 10)

    hits = pg.sprite.spritecollide(player, coin_group, True, pg.sprite.collide_circle)
    for hit in hits:
        score += 1
        coin_snd.play()
        new_coin()

    hits = pg.sprite.spritecollide(player, enemys_group, True, pg.sprite.collide_circle)
    for hit in hits:
        lives -= 1

    pg.display.update()
    clock.tick(FPS)

pg.quit()