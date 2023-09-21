import pygame
from bullet import Bullet


class Player:
    def __init__(self, width, height, speed, x, y, surface):
        self.width = width
        self.height = height
        self.speed = speed
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = surface

        self.fire_rate = 500
        self.last_shot = 0
        self.bullets = []

    def update_player(self, dt):
        current_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.y += self.speed * dt
        if keys[pygame.K_a]:
            self.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.x += self.speed * dt

        if keys[pygame.K_RIGHT] and current_time - self.last_shot >= self.fire_rate:
            bullet = Bullet(10, 10, 1000, self.x + 5, self.y + 10, "right")
            self.bullets.append(bullet)
            self.last_shot = current_time

        if keys[pygame.K_LEFT] and current_time - self.last_shot >= self.fire_rate:
            bullet = Bullet(10, 10, 1000, self.x + 5, self.y + 10, "left")
            self.bullets.append(bullet)
            self.last_shot = current_time

        if keys[pygame.K_UP] and current_time - self.last_shot >= self.fire_rate:
            bullet = Bullet(10, 10, 1000, self.x + 10, self.y + 5, "up")
            self.bullets.append(bullet)
            self.last_shot = current_time

        if keys[pygame.K_DOWN] and current_time - self.last_shot >= self.fire_rate:
            bullet = Bullet(10, 10, 1000, self.x + 10, self.y + 5, "down")
            self.bullets.append(bullet)
            self.last_shot = current_time

        for shots in self.bullets:
            shots.update_bullet(dt)
            shots.draw_bullet(self.surface)
            # delete bullet when it goes out of the screen
            if (shots.x > self.surface.get_width()
                    or shots.x < 0
                    or shots.y > self.surface.get_height()
                    or shots.y < 0):
                self.bullets.remove(shots)

    def draw_player(self):
        for shots in self.bullets:
            shots.draw_bullet(self.surface)
        pygame.draw.rect(self.surface, (0, 255, 0), self.rect)
