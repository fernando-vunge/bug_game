import pygame
from models.macros import *
from pygame.locals import *

vector = pygame.math.Vector2

class Coin(pygame.sprite.Sprite):
    def __init__(self, vector_size, vector_position) -> None:
        super().__init__()

         # animação
        self.num_sprites = 8  # Número total de sprites idle
        self.animation_speed = 0.2
        self.frame = 0

        self.sprite_sheet = pygame.image.load('./assets/animation/coin.png').convert_alpha()
        self.size = vector_size
        self.position = vector((vector_position.x + (vector_size.x / 2)), (vector_position.y + (vector_size.y / 2)))
        self.surf =  self.get_sprite(self.sprite_sheet, self.frame) #pygame.Surface(self.size)
        self.rect = self.surf.get_rect(center=self.position)
       


    def get_sprite(self, sheet, frame):
        x = frame * SPRITE_WIDTH
        y = 0
        sprite = sheet.subsurface((x, y, SPRITE_WIDTH, SPRITE_HEIGHT))
        return sprite

    def animate(self):
        self.frame += self.animation_speed
        if self.frame >= self.num_sprites:
            self.frame = 0
        self.surf = self.get_sprite(self.sprite_sheet, int(self.frame))