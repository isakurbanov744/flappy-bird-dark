import pygame
import sys
import time
import math
import os
from bird import *
from base import *
from pipe import *
from score import *
from cloud import *

# global variables
pygame.init()
width = 288
height = 512
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
spawn_pipe = pygame.USEREVENT
game_state = False

# visuals
try:
    background = pygame.image.load("../src/sprites/background.png").convert()
    game_over = pygame.image.load("../src/sprites/gameover.png").convert_alpha()
    game_over_rect = game_over.get_rect(center=(144, 256))
    bird_upflap = pygame.image.load("../src/sprites/bird-up-flap.png").convert_alpha()
    bird_midflap = pygame.image.load("../src/sprites/bird-mid-flap.png").convert_alpha()
    bird_downflap = pygame.image.load("../src/sprites/bird-down-flap.png").convert_alpha()
    cloud_one = pygame.image.load("../src/sprites/cloud-1.png")
    cloud_two = pygame.image.load("../src/sprites/cloud-2.png")
    base_surface = pygame.image.load("../src/sprites/base.png").convert()
    pipe_surface = pygame.image.load("../src/sprites/pipe.png").convert_alpha()
    main_font = pygame.font.Font("../src/fonts/04B_19.TTF", 30)
    window_icon = pygame.image.load("../src/icons/favicon.ico").convert_alpha()
    pygame.display.set_caption("Flappy Bird")
    pygame.display.set_icon(window_icon)

except Exception as e:
    print("Error parsing:", e)

# game variables
pipe_list = []
bird_surface = [bird_upflap, bird_midflap, bird_downflap]
cloud_surface = [cloud_one, cloud_two]
score_add = True


def collision_detection(bird, base, pipes, score_add):
    """
         gets rectangle of bottom and top pipes and of base images
         sends the variables to collision method of Bird class
         the method returns True if there has been a collision
         and False if not
        :param bird: Bird class instance
        :param base: Base class instance
        :param pipe: Pipe class instance
        :var col_top_pipe: top pipe rectangle
        :var col_bottom_pipe: bottom pipe rectangle
        :return: None
    """
    col_base = base.get_rect()
    bird_rect = bird.bird_rect

    if bird.collision(col_base):
        score_add = True
        return False

    if bird_rect.centery <= 0:
        score_add = True
        return False

    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            score_add = True
            return False

    return True


def render_screen(bird, base, pipe, score, cloud):
    """
         renders all the surfaces to the screen
        :param bird: Bird class instance
        :param base: Base class instance
        :param pipe: Pipe class instance
        :return: None
    """
    window.blit(background, (0, 0))
    cloud.draw(window)
    bird.draw(window)
    pipe.draw(window)
    pipe.score()
    score.display(window, game_state)
    base.draw(window)


def main():
    global game_state

    # class instances
    bird = Bird(100, 256, bird_surface)
    base = Base(base_surface, 460)
    score = Score(main_font, game_state)
    pipe = Pipe(pipe_surface, 350, pipe_list, score, score_add)
    cloud = Cloud(cloud_surface, 350, 70)

    # event variables
    run = True

    pygame.time.set_timer(spawn_pipe, 1200)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

                if event.key == pygame.K_SPACE and not game_state:
                    game_state = True
                    pipe_list.clear()
                    bird.reset()
                    score.reset()

            if event.type == spawn_pipe and game_state:
                pipe_list.extend(pipe.create())

        # display the screen
        render_screen(bird, base, pipe, score, cloud)

        if game_state:
            pipe.move()
            bird.move()
            base.move()
            cloud.move()
            game_state = collision_detection(bird, base, pipe_list, score_add)

        else:
            window.blit(game_over, game_over_rect)

        clock.tick(90)
        pygame.display.update()


if __name__ == "__main__":
    main()
