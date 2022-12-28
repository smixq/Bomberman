import pygame
import os

wall_size = 64


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


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
