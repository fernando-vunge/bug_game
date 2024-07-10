import sys
import pygame
from models.macros import *
from models.player import Player
from models.platform import Platform
from pygame.locals import *

pygame.init()

framepsec = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VPong")
all_sprites = pygame.sprite.Group()
player = Player()
platform = Platform()

all_sprites.add(player)
all_sprites.add(platform)

while (True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    displaysurface.fill((0,0,0))

    player.move()
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    framepsec.tick(FPS)