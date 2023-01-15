from random import randint


def random_level(level):
    count_walls = 0
    count_monsters = 0
    while count_walls != 100:
        rand_num_x = randint(0, len(level[0]) - 1)
        rand_num_y = randint(0, len(level) - 1)
        if rand_num_y != 0:
            if rand_num_y != 2 or rand_num_x != 1:
                if rand_num_y != 3 or rand_num_x != 1:
                    if rand_num_y != 2 or rand_num_x != 2:
                        if level[rand_num_y][rand_num_x] == 's':
                            new_level = level[rand_num_y]
                            level[rand_num_y] = new_level[:rand_num_x] + 'b' + new_level[rand_num_x + 1:]
                            count_walls += 1
    while count_monsters != 10:
        rand_num_x = randint(0, len(level[0]) - 1)
        rand_num_y = randint(0, len(level) - 1)
        if rand_num_y != 0:
            if rand_num_y != 2 or rand_num_x != 1:
                if rand_num_y != 3 or rand_num_x != 1:
                    if rand_num_y != 2 or rand_num_x != 2:
                        if level[rand_num_y][rand_num_x] == 's':
                            new_level = level[rand_num_y]
                            level[rand_num_y] = new_level[:rand_num_x] + 'm' + new_level[rand_num_x + 1:]
                            count_monsters += 1
    return level
