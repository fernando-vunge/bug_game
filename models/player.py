import pygame
import os
from models.macros import *
from pygame.locals import *
import pymunk

vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        # Carrega a imagem para o Surface
        self.idle_images = self.load_images('./assets/animation/idle')
        self.walk_images = self.load_images('./assets/animation/walk')
        self.current_images = self.idle_images

        self.image_index = 0
        self.animation_speed = 0.2
        self.player_image = self.current_images[self.image_index]
        self.isright = True
        self.isleft = False

        # Inicialização das variáveis do Pygame
        self.jumps = 0
        self.position = vector((10, HEIGHT - 30))
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)
        self.size = vector(30, 30)
        self.surf =  self.player_image #pygame.Surface(self.size)
        self.surf.blit(self.player_image, (0, 0))
        self.rect = self.surf.get_rect(center=self.position)

    def load_images(self, path):
        images = []
        for file_name in sorted(os.listdir(path)):
            img_path = os.path.join(path, file_name)
            image = pygame.image.load(img_path)
            scaled_image = pygame.transform.scale(image, (30, 50))
            images.append(scaled_image)
        return images

    def animate(self):
        self.image_index += self.animation_speed
        if self.image_index >= len(self.current_images):
            self.image_index = 0
        self.surf = self.current_images[int(self.image_index)]

        if self.isleft:
            self.surf = pygame.transform.flip(self.surf, True, False)

    def move(self):
        self.acceleration = vector(0 ,0.49)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_RIGHT] :
            self.isright = True
            self.isleft = False
            self.current_images = self.walk_images
            self.acceleration.x = ACCELERATION
        elif pressed_keys[K_LEFT] :
            self.isleft = True
            self.isright = False
            self.current_images = self.walk_images
            self.acceleration.x = -ACCELERATION
        else:
            self.current_images = self.idle_images

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
