import sys
import random
import pygame
import pymunk
from models.macros import *
from models.player import Player
from models.platform import Platform
from pygame.locals import *

pygame.init()
pygame.display.set_caption("VORLD")

fps = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

space = pymunk.Space()
space.gravity = (0, 800)
vector = pygame.math.Vector2

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

player = Player()
all_sprites.add(player)


land = Platform(vector(WIDTH, 40), vector(WIDTH / 2 ,HEIGHT - 20), (208, 191, 0))
all_sprites.add(land)
platforms.add(land)

def generate_palform(hight_initial ,hight_limit):
    for x in range(random.randint(14, 18)):
        platform = Platform( vector(random.randint(50,100), 10) , vector(random.randint(0, WIDTH-10) ,random.randint(hight_initial, hight_limit)), (random.randint(0,2), random.randint(0,50) , random.randint(0,2)))
        if pygame.sprite.spritecollide(platform, platforms, False) :
            continue
        all_sprites.add(platform)
        platforms.add(platform)
   


generate_palform(int(HEIGHT / 3) - 50, HEIGHT - 10)

while (True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    screen.fill((0,191,255))

    player.move()
    player.animate()
    player.jump()
    player.update(platforms)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if player.rect.top <= HEIGHT / 3 + 50 :
        player.position.y += abs(player.velocity.y)
        for platform in platforms:
            platform.rect.y += abs(player.velocity.y)
            if platform.rect.top >= HEIGHT:
                platform.kill()
    
    if player.position.y < HEIGHT / 2 - 50 :
        generate_palform(20 , int(HEIGHT / 3) - 50)

    pygame.display.update()
    fps.tick(FPS)