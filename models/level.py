import pygame
from models.macros import *
from models.objects import Coin
from models.platform import Platform

vector = pygame.math.Vector2

def generate_level(level, all_sprites, platforms, objects):
    for h in range (len(level)):
        for w in range(len(level[h])):
            if level[h][w]  == "L":
                platform = Platform(vector(32, 32) , vector((w * SPRITE_WIDTH), h * SPRITE_HEIGHT))
                all_sprites.add(platform)
                platforms.add(platform)
            #elif level[h][w] == "C" :
            #    coin = Coin(vector(64, 64) , vector((w * SPRITE_WIDTH), h * SPRITE_HEIGHT))
            #    all_sprites.add(coin)
            #    objects.add(coin)
    