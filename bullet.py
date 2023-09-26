import pygame


class Bullet:
    def __init__(self, width, height, speed, x, y, direction):
        self.width = width
        self.height = height
        self.speed = speed
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (0, 0, 255)
        self.direction = direction
        self.is_active = True

    def update_bullet(self, dt):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.is_active:
            if self.direction == "right":
                self.x += self.speed * dt
            elif self.direction == "left":
                self.x -= self.speed * dt
            elif self.direction == "up":
                self.y -= self.speed * dt
            elif self.direction == "down":
                self.y += self.speed * dt

    def draw_bullet(self, surface):
        if self.is_active:
            pygame.draw.rect(surface, self.color, self.rect)
