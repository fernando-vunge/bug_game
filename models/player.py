import pygame
import os
from models.macros import *
from pygame.locals import *

vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

         # Configurações da animação
        self.num_idle_sprites = 5  # Número total de sprites idle
        self.num_walk_sprites = 2  # Número total de sprites walk
        self.animation_speed = 0.2
        self.idle_frame = 0
        self.walk_frame = 0

        # Carrega as imagens de spritesheets
        self.idle_sprite_sheet = pygame.image.load('./assets/animation/idle.png').convert_alpha()
        self.walk_sprite_sheet = pygame.image.load('./assets/animation/walk.png').convert_alpha()
        self.current_sprite_sheet = self.idle_sprite_sheet
        self.current_num_sprites = self.num_idle_sprites

        self.isright = True
        self.isleft = False

        # Inicialização das variáveis do Pygame
        self.jumps = 0
        self.position = vector((30, HEIGHT - 30))
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)
        self.size = vector(50, 64)
        self.surf =  self.get_sprite(self.current_sprite_sheet, self.idle_frame) #pygame.Surface(self.size)
        self.rect = self.surf.get_rect(center=self.position)


    def get_sprite(self, sheet, frame):
        x = frame * SPRITE_WIDTH
        y = 0
        sprite = sheet.subsurface((x, y, SPRITE_WIDTH, SPRITE_HEIGHT))
        return sprite

    def animate(self):
        if self.current_sprite_sheet == self.idle_sprite_sheet:
            self.idle_frame += self.animation_speed
            if self.idle_frame >= self.num_idle_sprites:
                self.idle_frame = 0
            self.surf = self.get_sprite(self.current_sprite_sheet, int(self.idle_frame))
        elif self.current_sprite_sheet == self.walk_sprite_sheet:
            self.walk_frame += self.animation_speed
            if self.walk_frame >= self.num_walk_sprites:
                self.walk_frame = 0
            self.surf = self.get_sprite(self.current_sprite_sheet, int(self.walk_frame))

        if self.isleft:
            self.surf = pygame.transform.flip(self.surf, True, False)

    def move(self):
        self.acceleration = vector(0, 0.49)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_RIGHT]:
            self.isright = True
            self.isleft = False
            self.current_sprite_sheet = self.walk_sprite_sheet
            self.current_num_sprites = self.num_walk_sprites
            self.acceleration.x = ACCELERATION
        elif pressed_keys[K_LEFT]:
            self.isleft = True
            self.isright = False
            self.current_sprite_sheet = self.walk_sprite_sheet
            self.current_num_sprites = self.num_walk_sprites
            self.acceleration.x = -ACCELERATION
        else:
            self.current_sprite_sheet = self.idle_sprite_sheet
            self.current_num_sprites = self.num_idle_sprites

        self.acceleration.x += self.velocity.x * FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + (0.5 * self.acceleration)
        
        if self.position.x < (self.size.x / 2) + 1:
            self.position.x += -self.velocity.x + self.acceleration.x
        if self.position.x > WIDTH - (self.size.x / 2) + 1:
            self.position.x += -self.velocity.x + self.acceleration.x

        self.rect.midbottom = self.position
    
    def jump(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] and self.jumps < 10:
            self.velocity.y = -6
            self.jumps += 1

    def update(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.velocity.y > 0:
            if hits:
                self.position.y = hits[0].rect.top + 1
                self.velocity.y = 0
                self.jumps = 0
        self.animate()