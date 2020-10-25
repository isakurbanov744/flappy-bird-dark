import pygame
import sys
import time
import math
import os
from bird import *
from base import *
from pipe import *
from score import *

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
    base_surface = pygame.image.load("../src/sprites/base.png").convert()
    pipe_surface = pygame.image.load("../src/sprites/pipe.png").convert_alpha()
    main_font = pygame.font.Font("../src/fonts/04B_19.TTF", 30)


except Exception as e:
    print("Error parsing:", e)

# game variables
pipe_list = []
bird_surface = [bird_upflap, bird_midflap, bird_downflap]


def collision_detection(bird, base, pipes):
    """
         gets renctangle of bottom and top pipes and of base images
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

    # if bird.collision(col_base, col_top_pipe, col_bottom_pipe):
    if bird.collision(col_base):
        return False

    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    return True


def render_screen(bird, base, pipe, pipe_list, score):
    """
         renders all the surfaces to the screen
        :param bird: Bird class instance
        :param base: Base class instance
        :param pipe: Pipe class instance
        :param pipe_list: list of all pipes in the current game
        :return: None
    """
    window.blit(background, (0, 0))
    bird.draw(window)
    pipe.draw(window, pipe_list)
    score.add_score()
    score.display(window)
    base.draw(window)


def main():
    global game_state
    # class instances
    bird = Bird(100, 256, bird_surface)
    base = Base(base_surface, 460)
    pipe = Pipe(pipe_surface, 350)
    score = Score(main_font, game_state)

    # event variables
    run = True
    space_on = False

    pygame.time.set_timer(spawn_pipe, 1200)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
        render_screen(bird, base, pipe, pipe_list, score)

        if game_state:
            pipe.move(pipe_list)
            bird.move()
            base.move()
            game_state = collision_detection(bird, base, pipe_list)

        else:
            window.blit(game_over, game_over_rect)

        clock.tick(90)
        pygame.display.update()


if __name__ == "__main__":
    main()
