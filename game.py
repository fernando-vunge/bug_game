import sys
import pygame
from models.macros import *
from models.player import Player
from models.platform import Platform
from models.level import generate_level
from pygame.locals import *

pygame.init()
pygame.display.set_caption("VORLD")
fps = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
vector = pygame.math.Vector2
font = pygame.font.Font("assets/fonts/font.ttf", 12)


points = 0
lifes  = "# # #"
levels = [LEVEL_ONE, LEVEL_TWO, LEVEL_THREE]
id_level = 0

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
objects = pygame.sprite.Group()


generate_level(levels[id_level], all_sprites=all_sprites, platforms=platforms, objects=objects)
id_level += 1

player = Player()
all_sprites.add(player)


while (True):
    for event in pygame.event.get():
        if event.type == QUIT:
            print(len(LEVEL_ONE[0]))
            pygame.quit()
            sys.exit()
     
    screen.fill((0,191,255))

    player.move()
    player.jump()
    player.update(platforms)


    hits_on_coins = pygame.sprite.spritecollide(player, objects, True)
    if hits_on_coins:
        points += 1
        for s in range(len(hits_on_coins)):
            hits_on_coins[s].kill()

    for entity in objects:
        entity.animate()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    screen.blit(font.render(f"Pontucao {points}", True, (0,0,0)), (WIDTH - 400, HEIGHT - 24))
    screen.blit(font.render(f"Vida {lifes}", True, (0,0,0)), (WIDTH - 200, HEIGHT - 24))

    if points == 5:
        player.position = vector((30, HEIGHT - 60))
        points = 0
        generate_level(levels[id_level], all_sprites=all_sprites, platforms=platforms, objects=objects)
        id_level += 1

    pygame.display.update()
    fps.tick(FPS)

