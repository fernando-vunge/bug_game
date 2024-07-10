import pygame
from models.macros import *

vector = pygame.math.Vector2

class Platform(pygame.sprite.Sprite):
    def __init__(self, ) -> None:
        super().__init__()
        self.size = vector(WIDTH, 40)
        self.position = vector(WIDTH / 2 ,HEIGHT - int(self.size.y / 2))
        self.surf = pygame.Surface(self.size)
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = (225, 200))

