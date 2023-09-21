import pygame

from player import Player
from enemy import Enemy

screen = pygame.display.set_mode((800, 600))

player = Player(30, 30, 500, 400, 300, screen)
enemy = Enemy(30, 30, 250, 100)


def update(dt):
    player.update_player(dt)
    enemy.update_enemy(dt)


def render(_screen):
    _screen.fill((255, 255, 255))
    player.draw_player()
    enemy.draw_enemy(_screen)


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
