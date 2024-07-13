import pygame
from models.macros import *
from models.player import Player
from models.platform import Platform

vector = pygame.math.Vector2

def generate_level(level, all_sprites, platforms):
    for h in range (len(level)):
        for w in range(len(level[h])):
            if level[h][w]  == "L":
                platform = Platform(vector(64, 64) , vector((w * SPRITE_WIDTH), h * SPRITE_HEIGHT))
                all_sprites.add(platform)
                platforms.add(platform)
    