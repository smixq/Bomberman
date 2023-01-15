import pygame


class Button:
    def __init__(self, width, height, inactive_color, active_color, screen):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.screen = screen
        self.clicked = False
        self.question = False

    def draw(self, x, y, message, font_size):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))

            if click[0] == 1:
                self.clicked = True
            else:
                self.clicked = False

        else:
            pygame.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height))

        font_type = pygame.font.Font("Font/Text.ttf", font_size)
        text = font_type.render(message, True, (0, 0, 0))
        self.screen.blit(text, (x, y))
