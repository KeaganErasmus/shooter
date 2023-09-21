import pygame


class Enemy:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_enemy(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def update_enemy(self, dt):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
