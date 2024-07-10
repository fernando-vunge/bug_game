import pygame
import sys
import pymunk


def create_apple(space):
    body = pymunk.Body(1, 100, body_type= pymunk.Body.DYNAMIC) 
    # static
    # dinamic
    # cinematic

    body.position = (300, 0)
    shape = pymunk.Circle(body, 20)
    space.add(body, shape)
    return shape

def create_static_ball(space):
    body = pymunk.Body(body_type= pymunk.Body.STATIC) 
    # static
    # dinamic
    # cinematic

    body.position = (300, 900)
    shape = pymunk.Circle(body, 600)
    space.add(body, shape)
    return shape

def draw_apple(apples, screen):
    for apple in apples:
        int_body_position = (int(apple.body.position.x), int(apple.body.position.y))
        #pygame.draw.circle(screen, (255,0,0), int_body_position, 20)
        apple_rect = apple_surface.get_rect(center  = int_body_position)
        screen.blit(apple_surface, apple_rect)


def draw_static_ball(balls, screen):
    for ball in balls:
        int_ball_position = (int(ball.body.position.x), int(ball.body.position.y))
        pygame.draw.circle(screen, (0,200,50), int_ball_position, 600)

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fisica with clean code")
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 800)

apple_surface = pygame.transform.scale(pygame.image.load('./assets/out.png'), (50, 50))

apples = []
apples.append(create_apple(space))
balls = []
balls.append(create_static_ball(space))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    window.fill((255,255,255))
    draw_apple(apples, window)
    draw_static_ball(balls, window)
    space.step(1 / 50)
    pygame.display.update()
    clock.tick(70)
