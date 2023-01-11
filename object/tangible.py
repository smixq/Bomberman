import pygame
import os
import sys

wall_size = 64
explosive_range = 2


class Metallic_wall(pygame.sprite.Sprite):
    def __init__(self, image_name, x, y, *sprite_group):
        super().__init__(*sprite_group)
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
        # if self.rect.x >= 1980:
        #     self.rect.x = 1980
        # if self.rect.x <= 0:
        #     self.rect.x = 0


class Destructible_wall(pygame.sprite.Sprite):
    def __init__(self, image_name, x, y, *sprite_group):
        super().__init__(*sprite_group)
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
    def __init__(self, image_bomb, x, y, *sprite_group):
        self.sprite_gr = (sprite_group[0], sprite_group[1], sprite_group[3])
        sprite_group = sprite_group[0:3]
        super().__init__(*sprite_group)
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
        # if args[0] == 'animation':
        #     if self.count_anim <= 9:
        #         self.cur_frame += 1
        #         if self.cur_frame == 3:
        #             self.cur_frame = 0
        #         self.count_anim += 1
        #         self.image = self.frames[self.cur_frame]
        #     else:
        #         self.kill()
        #         Explosive(self.rect.x, self.rect.y, 'exp.png', 'small_fire.png', 'midle_fire.png', 'big_fire.png',
        #                   'max_fire.png', self.sprite_gr)

    def animation(self):
        if self.count_anim <= 9:
            self.cur_frame += 1
            if self.cur_frame == 3:
                self.cur_frame = 0
            self.count_anim += 1
            self.image = self.frames[self.cur_frame]
        else:
            self.kill()
            for i in range(1 , explosive_range):
                if i == 1:
                    Explosive(self.rect.x, self.rect.y, 'exp.png', 'horizontal.png', 'vertical_exp.png', 'midle',
                              self.sprite_gr)
                Explosive(self.rect.x - i * 64, self.rect.y, 'exp.png', 'horizontal.png', 'vertical_exp.png', 'horizontal',
                          self.sprite_gr)
                Explosive(self.rect.x + i * 64, self.rect.y, 'exp.png', 'horizontal.png', 'vertical_exp.png', 'horizontal',
                          self.sprite_gr)
                Explosive(self.rect.x, self.rect.y - i * 64, 'exp.png', 'horizontal.png', 'vertical_exp.png', 'vertical',
                          self.sprite_gr)
                Explosive(self.rect.x, self.rect.y + i * 64, 'exp.png', 'horizontal.png', 'vertical_exp.png', 'vertical',
                          self.sprite_gr)


class Explosive(pygame.sprite.Sprite):
    def __init__(self, x, y, exp_image, horizontal_exp_image, vertical_exp_image, exp_position, *sprite_group):
        super().__init__(*sprite_group)
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
