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

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

player = Player()
all_sprites.add(player)


generate_level(LEVEL_ONE ,all_sprites=all_sprites, platforms=platforms)

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

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.update()
    fps.tick(FPS)

