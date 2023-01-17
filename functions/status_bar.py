import pygame


def statusbar(screen, text, x, y, type=None):
    if type == 'score':
        font_score = pygame.font.Font('Font/Text.ttf', 64)
        text = font_score.render(f"Score: {text}", True, (255, 255, 255))
        screen.blit(text, (x, y))
    else:
        font_score = pygame.font.Font('Font/Text.ttf', 32)
        text = font_score.render(f"{text}", True, (155, 0, 0))
        screen.blit(text, (x, y))
