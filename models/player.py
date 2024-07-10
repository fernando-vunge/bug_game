import pygame
from models.macros import * 
from pygame.locals import *

vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.position = vector((10, 5))
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)
        self.size = vector(30, 30)
        self.surf = pygame.Surface(self.size)
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=self.position)

    def move(self):
        self.acceleration = vector(0 ,0.49)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] :
            self.acceleration.x = -ACCELERATION
        if pressed_keys[K_RIGHT] :
            self.acceleration.x = ACCELERATION

        self.acceleration.x += self.velocity.x * FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + (0.5 * self.acceleration)
        
        if self.position.x < 16 :
             self.position.x += -self.velocity.x + self.acceleration.x
        if self.position.x > 384 :
             self.position.x += -self.velocity.x + self.acceleration.x

        self.rect.midbottom = self.position
