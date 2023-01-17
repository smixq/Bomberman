import pygame
import os
import sys

wall_size = 64
explosive_range = 5


class Metallic_wall(pygame.sprite.Sprite):
    def __init__(self, image_name, x, y, sprites_group):
        self.sprites_group = sprites_group
        super().__init__(*(sprites_group[0], sprites_group[2], sprites_group[4]))
        self.image = load_image(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos_one = x
        self.pos_two = x - wall_size

    def update(self, direction):
        if direction == 'r':
            self.rect.x = self.pos_two
        if direction == 'l':
            self.rect.x = self.pos_one


class Destructible_wall(pygame.sprite.Sprite):
    def __init__(self, image_name, x, y, sprites_group):
        self.sprites_group = sprites_group
        super().__init__(*(sprites_group[0], sprites_group[2], sprites_group[3]))
        self.image = load_image(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos_one = x
        self.pos_two = x - wall_size

    def update(self, direction):
        if direction == 'r':
            self.rect.x = self.pos_two
        if direction == 'l':
            self.rect.x = self.pos_one


class Bomb(pygame.sprite.Sprite):
    def __init__(self, image_bomb, x, y, sprites_group):
        self.sprites_group = sprites_group
        super().__init__(*(sprites_group[0], sprites_group[2], sprites_group[5]))
        self.frames = []
        self.cut_sheet(load_image(image_bomb, -1), 3, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos_one = x + wall_size
        self.pos_two = x - wall_size
        self.count_anim = 0

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
            self.rect.x = self.pos_two
        if direction == 'l':
            self.rect.x = self.pos_one

    def animation(self):
        if self.count_anim <= 9:
            self.cur_frame += 1
            if self.cur_frame == 3:
                self.cur_frame = 0
            self.count_anim += 1
            self.image = self.frames[self.cur_frame]
        else:
            self.kill()
            self.explose()

    def explose(self):
        is_faced_left = False
        is_faced_right = False
        is_faced_top = False
        is_faced_bottom = False
        for i in range(1, explosive_range):
            if i == 1:
                Explosive(self.rect.x, self.rect.y, 'exp.png', 'horizontal.png', 'vertical_exp.png', 'midle',
                          self.sprites_group)
            explosive = Explosive(self.rect.x - i * 64, self.rect.y, 'exp.png', 'horizontal.png',
                                  'vertical_exp.png', 'horizontal', self.sprites_group)
            is_faced_left = exp_handling(explosive, is_faced_left, self)

            explosive = Explosive(self.rect.x + i * 64, self.rect.y, 'exp.png', 'horizontal.png',
                                  'vertical_exp.png', 'horizontal', self.sprites_group)
            is_faced_right = exp_handling(explosive, is_faced_right, self)
            explosive = Explosive(self.rect.x, self.rect.y - i * 64, 'exp.png', 'horizontal.png',
                                  'vertical_exp.png', 'vertical', self.sprites_group)
            is_faced_top = exp_handling(explosive, is_faced_top, self)
            explosive = Explosive(self.rect.x, self.rect.y + i * 64, 'exp.png', 'horizontal.png',
                                  'vertical_exp.png', 'vertical', self.sprites_group)
            is_faced_bottom = exp_handling(explosive, is_faced_bottom, self)


class Explosive(pygame.sprite.Sprite):
    def __init__(self, x, y, exp_image, horizontal_exp_image, vertical_exp_image, exp_position, sprites_group):
        self.sprites_group = sprites_group
        super().__init__(*(sprites_group[0], sprites_group[2], sprites_group[6]))
        self.frames = []
        self.cut_sheet(load_image(exp_image, -1), 4, 1)
        self.cut_sheet(load_image(horizontal_exp_image, -1), 4, 1)
        self.cut_sheet(load_image(vertical_exp_image, -1), 4, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos_one = x + wall_size
        self.pos_two = x - wall_size
        self.count_anim = 0
        self.exp_pos = exp_position
        self.is_introduced = False

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (64 * i, 0)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, (64, 64))))

    def update(self, direction):
        if direction == 'r':
            self.rect.x = self.pos_two
        if direction == 'l':
            self.rect.x = self.pos_one

    def animation(self):
        if self.count_anim <= 3:
            if self.exp_pos == 'midle' and not self.is_introduced:
                self.cur_frame = 0
                self.is_introduced = True
            elif self.exp_pos == 'horizontal' and not self.is_introduced:
                self.cur_frame = 4
                self.is_introduced = True
            elif self.exp_pos == 'vertical' and not self.is_introduced:
                self.cur_frame = 8
                self.is_introduced = True
            self.count_anim += 1
            self.image = self.frames[self.cur_frame]
            self.cur_frame += 1
        else:
            self.kill()


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


def exp_handling(explosive, is_faced, bomb):
    collide_met_wall = pygame.sprite.spritecollideany(explosive, bomb.sprites_group[4])
    collide_br_wall = pygame.sprite.spritecollideany(explosive, bomb.sprites_group[3])
    collide_bomb = pygame.sprite.spritecollideany(explosive, bomb.sprites_group[5])
    if is_faced:
        explosive.kill()
    elif collide_met_wall:
        explosive.kill()
        is_faced = True
    elif collide_br_wall:
        collide_br_wall.kill()
        is_faced = True
        explosive.kill()
    elif collide_bomb:
        explosive.kill()
        collide_bomb.kill()
        collide_bomb.explose()
        is_faced = True
    return is_faced
