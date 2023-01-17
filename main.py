import pygame
import sys
from object import tangible
from functions.start_window import start_menu
from sprites.all_sprites_groups import sprites_group
from functions.generate_level import generate_level
from functions.load_level import load_level
from functions.random_level import random_level
from functions.final_window import final_window
from functions.status_bar import statusbar
from moviepy.editor import VideoFileClip
from pygame.display import Info

pygame.init()
SIZE = W, H = 1920, 1024
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('chumba, двигайся!')
clock = pygame.time.Clock()
MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 475)
BLACK = pygame.Color('#000000')
WHITE = pygame.Color('white')
GREEN = pygame.Color('#008635')
COMPUTER_INFO = Info()
FINAL_VIDEO = VideoFileClip('data/FINAL_VIDEO.mp4')
RESIZED_FINAL_VIDEO = FINAL_VIDEO.resize((COMPUTER_INFO.current_w, COMPUTER_INFO.current_h))
run = True
sprites_group = sprites_group
score = 0
factor_score = 1

keys_p_one = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]
keys_p_two = [pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT]
wall_size = 64
player_size = (37, 59)

cords = []
for y in range(2, 15):
    for x in range(1, 30):
        cords.append((x * wall_size, y * wall_size))

difficulty = start_menu(screen)
level = load_level('levels/level_clear.txt')
level = random_level(level, difficulty)
player = generate_level(level)
while run:
    screen.fill(GREEN)
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == MYEVENTTYPE:
            for i in sprites_group[5]:
                i.animation()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_SPACE:
                bomb_cords = 0
                player_cords = player.get_pos()
                for i in cords:
                    if player_cords[0] // 64 == i[0] // 64 and player_cords[1] // 64 == i[1] // 64:
                        bomb_cords = i
                        break
                is_not_new = True
                for i in sprites_group[5]:
                    if i.rect.topleft == bomb_cords:
                        is_not_new = False
                if is_not_new:
                    new_bomb = tangible.Bomb('Bomb_sheet.png', bomb_cords[0], bomb_cords[1],
                                             sprites_group)
    if pygame.sprite.spritecollideany(player, sprites_group[6]):
        player.kill()
        final_window(screen)
        sys.exit()
    monsters_collide = pygame.sprite.groupcollide(sprites_group[7], sprites_group[6], True, False)
    if monsters_collide:
        for obj in monsters_collide:
            obj.kill()
            score += factor_score * 100
        factor_score = 1
    if pygame.sprite.spritecollideany(player, sprites_group[7]):
        player.kill()
        final_window(screen)
        sys.exit()
    lst_keys = pygame.key.get_pressed()
    if lst_keys[keys_p_one[3]]:
        player.update('r')
    if lst_keys[keys_p_one[1]]:
        player.update('l')
    if lst_keys[keys_p_one[0]]:
        player.update('u')
    if lst_keys[keys_p_one[2]]:
        player.update('d')
    for i in sprites_group[6]:
        i.animation()
    for mobs in sprites_group[7]:
        mobs.move()
    sprites_group[0].draw(screen)
    statusbar(screen, score, 750, 0, 'score')
    statusbar(screen, 'wasd - двигаться  |', 50, 16)
    statusbar(screen, 'space - бомбы', 350, 16)
    pygame.display.flip()
    if len(sprites_group[7]) == 0:
        RESIZED_FINAL_VIDEO.preview()
        sys.exit()
pygame.quit()
