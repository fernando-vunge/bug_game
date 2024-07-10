import pygame
from models.macros import *

vector = pygame.math.Vector2

class Platform(pygame.sprite.Sprite):
    def __init__(self, vector_size, vector_position, color) -> None:
        super().__init__()
        self.size = vector_size
        self.position = vector_position
        self.surf = pygame.Surface(self.size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=self.position)

