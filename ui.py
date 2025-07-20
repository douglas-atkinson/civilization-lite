import pygame

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, screen):
        pass  # TODO: Draw button

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)