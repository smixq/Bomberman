import pygame

from functions.menu_button import MenuButton
from functions.terminate import terminate


def start_menu(screen):
    font = pygame.font.Font(None, 50)
    input_box = pygame.Rect(795, 400, 330, 40)
    color_inactive = pygame.Color('white')
    color_active = pygame.Color('black')
    color = color_inactive
    active = False
    text = ""
    txt_surface = font.render(text, True, color)
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if txt_surface.get_width() < 300:
                            text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
        menu_background = pygame.image.load("data/background.png")
        screen.blit(menu_background, (0, 0))

        start_btn = MenuButton(480, 100, (255, 162, 58), (255, 204, 50), screen)
        start_btn.draw(720, 462, "Начать игру", 85)

        txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        menu = not start_btn.clicked
        pygame.display.update()
