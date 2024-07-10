import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, ) -> None:
        super().__init__()
        self.surf = pygame.Surface((150, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center = (225, 200))

