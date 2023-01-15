import pygame

sprites_group = []
# 0
all_sprites = pygame.sprite.Group()
sprites_group.append(all_sprites)
# 1
intangible_sprites = pygame.sprite.Group()
sprites_group.append(intangible_sprites)
# 2
movable = pygame.sprite.Group()
sprites_group.append(movable)
# 3
destroyed = pygame.sprite.Group()
sprites_group.append(destroyed)
# 4
undestroed = pygame.sprite.Group()
sprites_group.append(undestroed)
# 5
bomb = pygame.sprite.Group()
sprites_group.append(bomb)
# 6
explosive = pygame.sprite.Group()
sprites_group.append(explosive)
# 7
mobs = pygame.sprite.Group()
sprites_group.append(mobs)
