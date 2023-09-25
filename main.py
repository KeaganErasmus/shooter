import random
import pygame

from player import Player
from enemy import Enemy

screen = pygame.display.set_mode((800, 600))

player = Player(screen)
# enemy = Enemy(screen, player, random.randint(0, 800), random.randint(0, 600), player.bullets)

enemies = []
enemy_count = 2
for i in range(enemy_count):
    enemies.append(Enemy(screen, player, random.randint(0, 800), random.randint(0, 600) + i, player.bullets))


def update(dt):
    player.update_player(dt)
    # enemy.update_enemy(dt)
    for enemy in enemies:
        enemy.update_enemy(dt)


def render(_screen):
    _screen.fill((255, 255, 255))
    player.draw_player()
    # enemy.draw_enemy()
    for enemy in enemies:
        enemy.draw_enemy()
        if not enemy.is_active:
            enemies.remove(enemy)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick() / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update(dt)
        render(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
