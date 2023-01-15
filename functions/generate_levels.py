from functions.load_image import load_image

from data import block, door, player, road
from data.all_sprites_groups.spritres_groups import all_sprites, doors, roads, blocks


def generate_level(level, level_number):
    new_player, x, y = None, None, None
    px, py = 0, 0
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                road.Road(load_image(f'lvl{level_number}/road.png'), x, y, roads, all_sprites)
            elif level[y][x] == 'x':
                block.Block(load_image(f'lvl{level_number}/block.png'), x, y, blocks, all_sprites)
            elif level[y][x] == 'd':
                road.Road(load_image(f'lvl{level_number}/road.png'), x, y, roads, all_sprites)
                door.Door(load_image("door.png"), x, y, doors, all_sprites)
            elif level[y][x] == '@':
                road.Road(load_image(f'lvl{level_number}/road.png'), x, y, roads, all_sprites)
                px, py = x, y

    new_player = player.Player(load_image(f'lvl{level_number}/player.png'), px, py, all_sprites)
    return new_player, x, y