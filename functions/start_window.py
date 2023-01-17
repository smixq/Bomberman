import pygame

from functions.menu_button import MenuButton
from functions.terminate import terminate


def start_menu(screen):
    menu = [True, True, True]
    text_ease = 'ease'
    text_normal = 'normal'
    text_hard = 'hard'
    while False not in menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        menu_background = pygame.image.load("data/background.png")
        screen.blit(menu_background, (0, 0))
        ease = MenuButton(480, 100, (255, 162, 58), (255, 204, 50), screen)
        ease.draw(100, 462, "Легко", 85)
        normal = MenuButton(480, 100, (255, 162, 58), (255, 204, 50), screen)
        normal.draw(720, 462, "Нормально", 85)
        hard = MenuButton(480, 100, (255, 162, 58), (255, 204, 50), screen)
        hard.draw(1300, 462, "Сложно", 85)
        menu[0] = not ease.clicked
        menu[1] = not normal.clicked
        menu[2] = not hard.clicked
        pygame.display.update()
    if not menu[0]:
        return text_ease
    elif not menu[1]:
        return text_normal
    elif not menu[2]:
        return text_hard
