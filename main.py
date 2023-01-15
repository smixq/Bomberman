import pygame
from random import choice
import sys
from object import intangible, tangible
from functions.start_window import start_menu
from sprites.all_sprites_groups import sprites_group
from functions.generate_level import generate_level
from functions.load_level import load_level
from functions.random_level import random_level
from functions.final_window import final_window

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
run = True
sprites_group = sprites_group

keys_p_one = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]
keys_p_two = [pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT]
wall_size = 64
player_size = (37, 59)

cords = []
for y in range(2, 15):
    for x in range(1, 30):
        if x == 1 and y == 2:
            continue
        elif x == 2 and y == 2:
            continue
        elif x == 1 and y == 3:
            continue
        cords.append((x * wall_size, y * wall_size))



# hor_UP_walls = pygame.sprite.Group()
# vert_LEFT_walls = pygame.sprite.Group()
# hor_DOWN_walls = pygame.sprite.Group()
# vert_RIGHT_walls = pygame.sprite.Group()

# class Player(pygame.sprite.Sprite):
#     def __init__(self, image_name, x, y):
#         super().__init__(all_sprites)
#         self.image = load_image(image_name)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#
#     def update(self, result):
#         # lst_keys = pygame.key.get_pressed()
#         # print(lst_keys)
#         # if lst_keys[pygame.K_RIGHT]:
#         #     self.rect.x += 10
#         # elif args[0] == pygame.K_LEFT:
#         #     self.rect.x -= 10
#         # elif args[0] == pygame.K_UP:
#         #     self.rect.y -= 10
#         # elif args[0] == pygame.K_DOWN:
#         #     self.rect.y += 10
#         if result == 'r':
#             self.rect.x += 5
#         if result == 'l':
#             self.rect.x -= 5
#         if result == 'u':
#             self.rect.y -= 5
#         if result == 'd':
#             self.rect.y += 5

level = load_level('levels/level_clear.txt')
level = random_level(level)
player = generate_level(level)
# player = intangible.Player('Bomberman_up.png', 'Bomberman_right.png', 'Bomberman_down.png',
#                            'Bomberman_left.png',
#                            wall_size, wall_size * 2, sprites_group)
# for i in range(31):
#     tangible.Metallic_wall('Unbr_walls.jpg', wall_size * i, wall_size, sprites_group)
# for i in range(31):
#     tangible.Metallic_wall('Unbr_walls.jpg', wall_size * i, H - wall_size, sprites_group)
# for i in range(1, 15):
#     tangible.Metallic_wall('Unbr_walls.jpg', 0, wall_size * i, sprites_group)
# for i in range(1, 15):
#     tangible.Metallic_wall('Unbr_walls.jpg', W, wall_size * i, sprites_group)
# hoary_cords = []
# for i in range(2, 29, 2):
#     for j in range(3, 14, 2):
#         hoary_cords.append((wall_size * i, wall_size * j))
#         tangible.Metallic_wall('Unbr_walls.jpg', wall_size * i, wall_size * j, sprites_group)
# count_walls = 0
# while count_walls != 100:
#     rand_cords = choice(cords)
#     if rand_cords in hoary_cords:
#         continue
#     hoary_cords.append(rand_cords)
#     tangible.Destructible_wall('wall.jpg', rand_cords[0], rand_cords[1], sprites_group)
#     count_walls += 1
cords.append((64, 128))
cords.append((64, 192))
cords.append((128, 128))
# for i in range(15):
#     tangible.metallic_wall('wall.png', 128 * i, 0, all_sprites, walls_sprites)
# for i in range(1, 10):
#     tangible.metallic_wall('wall.png', 0, 128 * i, all_sprites, walls_sprites)
# for i in range(1, 10):
#     tangible.metallic_wall('wall.png', 1792, 128 * i, all_sprites, walls_sprites)
# for i in range(15):
#     tangible.metallic_wall('wall.png', 128 * i, H + 2 * 128, all_sprites, walls_ssprites)
# for i in range(2, 13, 2):
#     tangible.metallic_wall('wall.png', 128 * i,  128 * 2, all_sprites, walls_sprites)
# for i in range(2, 13, 2):
#     tangible.metallic_wall('wall.png', 128 * i,  128 * 4, all_sprites, walls_sprites)
# for i in range(2, 13, 2):
#     tangible.metallic_wall('wall.png', 128 * i,  128 * 6, all_sprites, walls_sprites)
# for i in range(2, 13, 2):
#     tangible.metallic_wall('wall.png', 128 * i,  128 * 8, all_sprites, walls_sprites)
start_menu(screen)
while run:
    screen.fill(GREEN)
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == MYEVENTTYPE:
            for i in sprites_group[5]:
                i.animation()
            # bomb.update('animation')
            # explosive.update('animation')
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

        #     if event.key == pygame.K_DOWN:
        #         player.update(pygame.K_DOWN)
        #     if event.key == pygame.K_LEFT:
        #         player.update(pygame.K_LEFT)
        #     if event.key == pygame.K_RIGHT:
        #         player.update(pygame.K_RIGHT)w
    # if pygame.sprite.spritecollideany(player, sprites_group[6]):
    #     player.kill()
    if pygame.sprite.spritecollideany(player, sprites_group[6]):
        player.kill()
        final_window(screen)
        sys.exit()
    monsters_collide = pygame.sprite.groupcollide(sprites_group[7], sprites_group[6], True, False)
    if monsters_collide:
        for obj in monsters_collide:
            obj.kill()
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
    pygame.display.flip()
    if len(sprites_group[7]) == 0:

        sys.exit()
pygame.quit()
