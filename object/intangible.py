import pygame
import os

p_speed = 4
W, H = 1920, 1024
wall_size = 64
player_size = (37, 59)
shift = W // 2 + wall_size


class Player(pygame.sprite.Sprite):
    def __init__(self, image_name_up, image_name_right, image_name_down, image_name_left, x, y, *sprite_group):
        super().__init__(*sprite_group)
        self.frames = []
        self.cut_sheet(load_image(image_name_up), 7, 1)
        self.cut_sheet(load_image(image_name_right), 7, 1)
        self.cut_sheet(load_image(image_name_down), 7, 1)
        self.cut_sheet(load_image(image_name_left), 7, 1)
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
        # self.rect.w = 43

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                # frame_location = (self.rect.w * i, self.rect.h * j)
                frame_location = (80 * i, 0)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, (47, 60))))

    def update(self, result, walls_group):
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
                self.cur_frame = 7
            elif result == 'd':
                self.der = 'd'
                self.cur_frame = 14
            elif result == 'l':
                self.der = 'l'
                self.cur_frame = 21

        if result == 'r':
            self.cur_frame += 1
            if self.cur_frame == 14:
                self.cur_frame = 7
            self.image = self.frames[self.cur_frame]
            self.rect.x += p_speed
            if pygame.sprite.spritecollideany(self, walls_group):
                self.rect.x -= p_speed
            else:
                self.rect.x += p_speed
                if not pygame.sprite.spritecollideany(self, walls_group):
                    if shift + wall_size == self.rect.x and self.wall_site == 'l':
                        self.wall_site = 'r'
                        walls_group.update('move', 'r')
                        self.rect.x = self.pos_one
                self.rect.x -= p_speed

        if result == 'l':
            self.cur_frame += 1
            if self.cur_frame == 28:
                self.cur_frame = 21
            self.image = self.frames[self.cur_frame]
            self.rect.x -= p_speed
            if pygame.sprite.spritecollideany(self, walls_group):
                self.rect.x += p_speed
            else:
                self.rect.x -= p_speed
                if not pygame.sprite.spritecollideany(self, walls_group):
                    if shift - wall_size == self.rect.x and self.wall_site == 'r':
                        self.wall_site = 'l'
                        walls_group.update('move', 'l')
                        self.rect.x = self.pos_two
                self.rect.x += p_speed

        if result == 'u':
            self.cur_frame = (self.cur_frame + 1) % 7
            self.image = self.frames[self.cur_frame]
            self.rect.y -= p_speed
            if pygame.sprite.spritecollideany(self, walls_group):
                self.rect.y += p_speed
            # else:
            #     self.rect.y -= p_speed
            #     if not pygame.sprite.spritecollideany(self, walls_group):
            #         if self.rect.y + 140 <= H - 128 * 3:
            #             walls_group.update('u')
            #     self.rect.y += p_speed
        if result == 'd':
            self.cur_frame += 1
            if self.cur_frame == 21:
                self.cur_frame = 14
            self.image = self.frames[self.cur_frame]
            self.rect.y += p_speed
            if pygame.sprite.spritecollideany(self, walls_group):
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


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
