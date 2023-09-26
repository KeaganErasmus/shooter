import pygame
from bullet import Bullet


class Player:
    def __init__(self, surface, enemies):
        self.width = 30
        self.height = 30
        self.speed = 500
        self.x = 400
        self.y = 300
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = surface
        self.fire_rate = 500
        self.last_shot = 0
        self.bullets = []
        self.enemies = enemies

    def update_player(self, dt):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        keys = pygame.key.get_pressed()

        self.check_bounds()
        self.player_movement(keys, dt)
        self.player_shoot(keys, dt)

    def draw_player(self):
        for shots in self.bullets:
            shots.draw_bullet(self.surface)
        pygame.draw.rect(self.surface, (0, 255, 0), self.rect)

    def player_shoot(self, keys, dt):
        current_time = pygame.time.get_ticks()
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

            if not shots.is_active:
                self.bullets.remove(shots)

    def player_movement(self, keys, dt):
        if keys[pygame.K_w]:
            self.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.y += self.speed * dt
        if keys[pygame.K_a]:
            self.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.x += self.speed * dt

    def check_bounds(self):
        if self.x + self.width >= self.surface.get_width():
            self.x = self.surface.get_width() - self.width
        if self.x < 0:
            self.x = 0
        if self.y + self.height > self.surface.get_height():
            self.y = self.surface.get_height() - self.height
        if self.y < 0:
            self.y = 0
