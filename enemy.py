import math

import pygame


class Enemy:
    def __init__(self, surface, player, x, y, bullets):
        self.width = 30
        self.height = 30
        self.x = x
        self.y = y
        self.speed = 150
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.player = player
        self.bullets = bullets
        self.surface = surface
        self.is_active = True

    def draw_enemy(self):
        pygame.draw.rect(self.surface, (255, 0, 0), self.rect)

    def update_enemy(self, dt):
        self.check_hit()
        if self.is_active:
            dx = self.player.x - self.x
            dy = self.player.y - self.y

            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance != 0:
                dx /= distance
                dy /= distance

            self.x += dx * self.speed * dt
            self.y += dy * self.speed * dt

            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def check_hit(self):
        if self.rect.collidelistall(self.bullets):
            self.is_active = False
