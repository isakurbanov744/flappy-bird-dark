import pygame
import sys, time, math, os
from bird import *
from base import *

# global varaibles
width = 288
height = 512
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# visuals
try:
    background = pygame.image.load("../src/sprites/background.png").convert()
    bird_upflap = pygame.image.load("../src/sprites/bird-up-flap.png").convert_alpha()
    bird_midflap = pygame.image.load("../src/sprites/bird-mid-flap.png").convert_alpha()
    bird_downflap = pygame.image.load("../src/sprites/bird-down-flap.png").convert_alpha()
    base_surface = pygame.image.load("../src/sprites/base.png").convert()
    pipe_surface = pygame.image.load("../src/sprites/pipe.png").convert()

except Exception as e:
    print("Error parsing:", e)


def render_screen(bird, base):
    window.blit(background, (0, 0))
    bird.draw(window)
    base.draw(window)


def main():
    pygame.init()

    bird = Bird(bird_midflap, 100, 256)
    base = Base(base_surface, 460)
    run = True
    space_on = False

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    space_on = True
                    bird.move(space_on)
                    space_on = False

        render_screen(bird, base)

        bird.move(space_on)
        base.move()

        pygame.display.update()


if __name__ == "__main__":
    main()
