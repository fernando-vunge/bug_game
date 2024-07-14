import pygame
from models.macros import *
from models.resource import *

vector = pygame.math.Vector2

class Platform(pygame.sprite.Sprite):
    def __init__(self, vector_size, vector_position) -> None:
        super().__init__()
        self.size = vector_size
        self.position = vector((vector_position.x + (vector_size.x / 2)), (vector_position.y + (vector_size.y / 2)))
        self.surf =  get_image('land') #pygame.image.load('./assets/sprites/land.png').convert_alpha()
        self.rect = self.surf.get_rect(center=self.position)

