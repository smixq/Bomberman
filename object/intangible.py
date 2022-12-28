import pygame
import os

p_speed = 4
W, H = 1920, 1024
wall_size = 64
player_size = (37, 59)
shift = W // 2 + wall_size


class Player(pygame.sprite.Sprite):
    def __init__(self, image_name, x, y, *sprite_group):
        super().__init__(*sprite_group)
        self.image = load_image(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos_one = shift
        self.pos_two = shift
        self.wall_site = 'l'

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

        if result == 'r':
            self.rect.x += p_speed
            if pygame.sprite.spritecollideany(self, walls_group):
                self.rect.x -= p_speed
            else:
                self.rect.x += p_speed
                if not pygame.sprite.spritecollideany(self, walls_group):
                    if shift + wall_size == self.rect.x and self.wall_site == 'l':
                        self.wall_site = 'r'
                        walls_group.update('r')
                        self.rect.x = self.pos_one
                self.rect.x -= p_speed

        if result == 'l':
            self.rect.x -= p_speed
            if pygame.sprite.spritecollideany(self, walls_group):
                self.rect.x += p_speed
            else:
                self.rect.x -= p_speed
                if not pygame.sprite.spritecollideany(self, walls_group):
                    if shift - wall_size == self.rect.x and self.wall_site == 'r':
                        self.wall_site = 'l'
                        walls_group.update('l')
                        self.rect.x = self.pos_two
                self.rect.x += p_speed

        if result == 'u':
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


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
