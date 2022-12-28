import pygame

import sys
from object import intangible, tangible

pygame.init()
SIZE = W, H = 1920, 1024
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('chumba, двигайся!')
clock = pygame.time.Clock()
BLACK = pygame.Color('#000000')
WHITE = pygame.Color('white')
GREEN = pygame.Color('green')
run = True

keys_p_one = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]
keys_p_two = [pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT]
wall_size = 64
player_size = (37, 59)

all_sprites = pygame.sprite.Group()
intangible_sprites = pygame.sprite.Group()
walls_sprites = pygame.sprite.Group()
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


player = intangible.Player('player.png', wall_size, wall_size * 2, all_sprites, intangible_sprites)
for i in range(31):
    tangible.metallic_wall('wall.png', wall_size * i, wall_size, all_sprites, walls_sprites)
for i in range(31):
    tangible.metallic_wall('wall.png', wall_size * i, H - wall_size, all_sprites, walls_sprites)
for i in range(1, 15):
    tangible.metallic_wall('wall.png', 0, wall_size * i, all_sprites, walls_sprites)
for i in range(1, 15):
    tangible.metallic_wall('wall.png', W, wall_size * i, all_sprites, walls_sprites)
for i in range(2, 29, 2):
    for j in range(3, 14, 2):
        tangible.metallic_wall('wall.png', wall_size * i, wall_size * j, all_sprites, walls_sprites)
# for i in range(15):
#     tangible.metallic_wall('wall.png', 128 * i, 0, all_sprites, walls_sprites)
# for i in range(1, 10):
#     tangible.metallic_wall('wall.png', 0, 128 * i, all_sprites, walls_sprites)
# for i in range(1, 10):
#     tangible.metallic_wall('wall.png', 1792, 128 * i, all_sprites, walls_sprites)
# for i in range(15):
#     tangible.metallic_wall('wall.png', 128 * i, H + 2 * 128, all_sprites, walls_sprites)
# for i in range(2, 13, 2):
#     tangible.metallic_wall('wall.png', 128 * i,  128 * 2, all_sprites, walls_sprites)
# for i in range(2, 13, 2):
#     tangible.metallic_wall('wall.png', 128 * i,  128 * 4, all_sprites, walls_sprites)
# for i in range(2, 13, 2):
#     tangible.metallic_wall('wall.png', 128 * i,  128 * 6, all_sprites, walls_sprites)
# for i in range(2, 13, 2):
#     tangible.metallic_wall('wall.png', 128 * i,  128 * 8, all_sprites, walls_sprites)
while run:
    screen.fill(GREEN)
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         player.update(pygame.K_UP)
        #     if event.key == pygame.K_DOWN:
        #         player.update(pygame.K_DOWN)
        #     if event.key == pygame.K_LEFT:
        #         player.update(pygame.K_LEFT)
        #     if event.key == pygame.K_RIGHT:
        #         player.update(pygame.K_RIGHT)
    lst_keys = pygame.key.get_pressed()
    if lst_keys[keys_p_one[3]]:
        player.update('r', walls_sprites)
    if lst_keys[keys_p_one[1]]:
        player.update('l', walls_sprites)
    if lst_keys[keys_p_one[0]]:
        player.update('u', walls_sprites)
    if lst_keys[keys_p_one[2]]:
        player.update('d', walls_sprites)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
