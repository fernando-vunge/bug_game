import io
import pygame

images = {}

images_path = {
    'icon' : 'icon.bin',
    'idle' : 'assets/sprites/idle.bin',
    'coin' : 'assets/sprites/coin.bin',
    'land' : 'assets/sprites/land.bin',
    'walk' : 'assets/sprites/walk.bin'
}
size = {
    'icon' : (64, 64),
    'idle' : (32 * 4, 32),
    'coin' : (512, 64),
    'land' : (32, 32),
    'walk' : (320, 32)
}

for key, path in images_path.items():
    with open(path, 'rb') as f:
        image_data = f.read()
    images[key] = pygame.image.frombuffer(image_data, size[key], 'RGBA')


def get_image(key):
    return images[key]