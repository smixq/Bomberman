import sys

import pygame
from functions.terminate import terminate


def final_window(screen):
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
        pygame.display.update()
