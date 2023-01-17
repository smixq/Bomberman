import sys

import pygame
from functions.terminate import terminate
from functions.status_bar import statusbar


def final_window(screen, score):
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        menu_background = pygame.image.load("data/lose.png")

        screen.blit(menu_background, (0, 0))
        statusbar(screen, score, 850, 200, 'score')
        pygame.display.update()
