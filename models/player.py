import pygame
from models.macros import * 
from pygame.locals import *

vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.jumps = 0
        self.position = vector((10, HEIGHT - 30))
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)
        self.size = vector(30, 30)
        self.surf = pygame.Surface(self.size)
        self.surf.fill((20, 20, 0))
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
        
        if self.position.x < (self.size.x / 2) + 1 :
             self.position.x += -self.velocity.x + self.acceleration.x
        if self.position.x > WIDTH - (self.size.x / 2) + 1  :
             self.position.x += -self.velocity.x + self.acceleration.x

        self.rect.midbottom = self.position
    
    def jump(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] and self.jumps < 10:
            self.velocity.y = -5
            self.jumps += 1
        


    def update(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.velocity.y > 0:
            if hits :
                self.position.y = hits[0].rect.top + 1
                self.velocity.y = 0
                self.jumps = 0