import pygame
import pymunk
import pymunk.pygame_util

# Inicializa o pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

# Inicializa o espaço de física do pymunk
space = pymunk.Space()
space.gravity = (0, 900)  # Gravidade

# Função para adicionar um círculo
def add_ball(space, position):
    mass = 1
    radius = 14
    inertia = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, inertia)
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.95
    space.add(body, shape)

# Adiciona um chão
def add_static_line(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (300, 580)
    shape = pymunk.Segment(body, (-300, 0), (300, 0), 5)
    shape.elasticity = 0.9
    space.add(body, shape)

add_static_line(space)
add_ball(space, (300, 50))

draw_options = pymunk.pygame_util.DrawOptions(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            add_ball(space, event.pos)

    # Atualiza a física
    space.step(1 / 60.0)

    # Desenha tudo
    screen.fill((255, 255, 255))
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
