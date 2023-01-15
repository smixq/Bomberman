from functions.button import Button


class MenuButton(Button):
    def __init__(self, width, height, inactive_color, active_color, screen):
        super().__init__(width, height, inactive_color, active_color, screen)