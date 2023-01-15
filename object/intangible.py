import pygame
import os
import sys
from random import choice
from random import randint

p_speed = 4
m_speed = 2
W, H = 1920, 1024
wall_size = 64
player_size = (37, 59)
shift = W // 2 + wall_size
rand_direction = ['r', 'l', 'u', 'd']


class Player(pygame.sprite.Sprite):
    def __init__(self, image_name_up, image_name_right, image_name_down, image_name_left, x, y, sprites_group):
        self.sprites_group = sprites_group
        super().__init__(*sprites_group[0:2])
        self.frames = []
        self.cut_sheet(load_image(image_name_up, -1), 3, 1)
        self.cut_sheet(load_image(image_name_right, -1), 3, 1)
        self.cut_sheet(load_image(image_name_down, -1), 3, 1)
        self.cut_sheet(load_image(image_name_left, -1), 3, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.der = 'u'
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos_one = shift
        self.pos_two = shift
        self.wall_site = 'l'

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                # frame_location = (self.rect.w * i, self.rect.h * j)
                frame_location = (77 * i, 0)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, (42, 55))))

    def update(self, result):
        # lst_keys = pygame.key.get_pressed()
        # print(lst_keys)
        # if lst_keys[pygame.K_RIGHT]:
        #     self.rect.x += 10
        # elif args[0] == pygame.K_LEFT:
        #     self.rect.x -= 10
        # elif args[0] == pygame.K_UP:
        #     self.rect.y -= 10
        # elif args[0] == pygame.K_DOWN:
        #     self.rect.y += 10
        if self.der != result:
            if result == 'u':
                self.cur_frame = 0
                self.der = 'u'
            elif result == 'r':
                self.der = 'r'
                self.cur_frame = 3
            elif result == 'd':
                self.der = 'd'
                self.cur_frame = 7
            elif result == 'l':
                self.der = 'l'
                self.cur_frame = 9

        if result == 'r':
            self.cur_frame += 1
            if self.cur_frame == 6:
                self.cur_frame = 3
            self.image = self.frames[self.cur_frame]
            self.rect.x += p_speed
            if pygame.sprite.spritecollideany(self, self.sprites_group[3]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[4]):
                self.rect.x -= p_speed
            else:
                self.rect.x += p_speed
                if not pygame.sprite.spritecollideany(self, self.sprites_group[3]) \
                        or pygame.sprite.spritecollideany(self, self.sprites_group[4]):
                    if shift + wall_size == self.rect.x and self.wall_site == 'l':
                        self.wall_site = 'r'

                        self.sprites_group[2].update('r')
                        self.rect.x = self.pos_one
                self.rect.x -= p_speed

        if result == 'l':
            self.cur_frame += 1
            if self.cur_frame == 12:
                self.cur_frame = 9
            self.image = self.frames[self.cur_frame]
            self.rect.x -= p_speed
            if pygame.sprite.spritecollideany(self, self.sprites_group[3]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[4]):
                self.rect.x += p_speed
            else:
                self.rect.x -= p_speed
                if not pygame.sprite.spritecollideany(self, self.sprites_group[3]) \
                        or pygame.sprite.spritecollideany(self, self.sprites_group[4]):
                    if shift - wall_size == self.rect.x and self.wall_site == 'r':
                        self.wall_site = 'l'
                        self.sprites_group[2].update('l')
                        self.rect.x = self.pos_two
                self.rect.x += p_speed

        if result == 'u':
            self.cur_frame = (self.cur_frame + 1) % 3
            self.image = self.frames[self.cur_frame]
            self.rect.y -= p_speed
            if pygame.sprite.spritecollideany(self, self.sprites_group[3]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[4]):
                self.rect.y += p_speed
            # else:
            #     self.rect.y -= p_speed
            #     if not pygame.sprite.spritecollideany(self, walls_group):
            #         if self.rect.y + 140 <= H - 128 * 3:
            #             walls_group.update('u')
            #     self.rect.y += p_speed
        if result == 'd':
            self.cur_frame += 1
            if self.cur_frame == 9:
                self.cur_frame = 6
            self.image = self.frames[self.cur_frame]
            self.rect.y += p_speed
            if pygame.sprite.spritecollideany(self, self.sprites_group[3]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[4]):
                self.rect.y -= p_speed
        # if pygame.sprite.spritecollideany(self, walls_group[0]):
        #     self.rect.y += p_speed
        # if pygame.sprite.spritecollideany(self, walls_group[1]):
        #     self.rect.x += p_speed
        # if pygame.sprite.spritecollideany(self, walls_group[2]):
        #     self.rect.y -= p_speed
        # if pygame.sprite.spritecollideany(self, walls_group[3]):
        #     self.rect.x -= p_speed

    def get_pos(self):
        return self.rect.center


class Monster(pygame.sprite.Sprite):
    def __init__(self, image_name_left, image_name_right, x, y, sprites_group):
        self.sprites_group = sprites_group
        super().__init__(*sprites_group[0:2], sprites_group[2], sprites_group[7])
        self.frames = []
        self.cut_sheet(load_image(image_name_right, -1), 3, 1)
        self.cut_sheet(load_image(image_name_left, -1), 3, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.der = 'u'
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos_one = x
        self.pos_two = x - wall_size
        self.wall_site = 'l'
        self.direction = 'u'
        self.count_steps = 0

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                # frame_location = (self.rect.w * i, self.rect.h * j)
                frame_location = (64 * i, 0)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, (64, 64))))

    def update(self, direction):
        if direction == 'r':
            self.rect.x -= 64
        if direction == 'l':
            self.rect.x += 64

    def move(self):
        if self.count_steps <= 0:
            if self.rect.x % 64 == 0 and self.rect.y % 64 == 0:
                new_direction = choice(rand_direction)
                self.count_steps = randint(32, 128)
            else:
                new_direction = self.direction
        else:
            new_direction = self.direction
        if new_direction == 'r':
            self.rect.x += m_speed
            if pygame.sprite.spritecollideany(self, self.sprites_group[3]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[4]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[5]):
                self.rect.x -= m_speed
                self.count_steps = 1
        elif new_direction == 'l':
            self.rect.x -= m_speed
            if pygame.sprite.spritecollideany(self, self.sprites_group[3]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[4]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[5]):
                self.rect.x += m_speed
                self.count_steps = 1
        elif new_direction == 'u':
            self.rect.y += m_speed
            if pygame.sprite.spritecollideany(self, self.sprites_group[3]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[4]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[5]):
                self.rect.y -= m_speed
                self.count_steps = 1
        elif new_direction == 'd':
            self.rect.y -= m_speed
            if pygame.sprite.spritecollideany(self, self.sprites_group[3]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[4]) \
                    or pygame.sprite.spritecollideany(self, self.sprites_group[5]):
                self.rect.y += m_speed
                self.count_steps = 1
        self.animation(new_direction)
        self.count_steps -= 1

    def animation(self, new_direction):
        if new_direction != self.direction:
            if new_direction == 'r' or new_direction == 'u':
                self.cur_frame = 0
            else:
                self.cur_frame = 3
            self.direction = new_direction
        if new_direction == 'r' or new_direction == 'u':
            self.cur_frame += 1
            if self.cur_frame == 3:
                self.cur_frame = 0
        elif new_direction == 'l' or new_direction == 'd':
            self.cur_frame += 1
            if self.cur_frame == 6:
                self.cur_frame = 3
        self.image = self.frames[self.cur_frame]


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
