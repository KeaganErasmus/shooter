import random
import pygame

from player import Player
from enemy import Enemy


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.enemies = []
        self.player = Player(self.screen)
        self.ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ENEMY_SPAWN_EVENT, 2000)

    def update(self, dt):
        self.player.update_player(dt)
        # enemy.update_enemy(dt)

        for enemy in self.enemies:
            enemy.update_enemy(dt)

    def render(self, _screen):
        _screen.fill((255, 255, 255))
        self.player.draw_player()
        # enemy.draw_enemy()
        for enemy in self.enemies:
            enemy.draw_enemy()
            if not enemy.is_active:
                self.enemies.remove(enemy)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == self.ENEMY_SPAWN_EVENT:
                    self.enemies.append(
                        Enemy(self.screen, self.player, random.randint(0, 800), random.randint(0, 600), self.player.bullets))

            self.update(dt)
            self.render(self.screen)
            pygame.display.update()
