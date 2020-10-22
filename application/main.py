import pygame
import sys
import time
import math
import os
from bird import *
from base import *
from pipe import *

# global variables
pygame.init()
width = 288
height = 512
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
spawn_pipe = pygame.USEREVENT
game_state = True

# visuals
try:
    background = pygame.image.load("../src/sprites/background.png").convert()
    bird_upflap = pygame.image.load("../src/sprites/bird-up-flap.png").convert_alpha()
    bird_midflap = pygame.image.load("../src/sprites/bird-mid-flap.png").convert_alpha()
    bird_downflap = pygame.image.load("../src/sprites/bird-down-flap.png").convert_alpha()
    base_surface = pygame.image.load("../src/sprites/base.png").convert()
    pipe_surface = pygame.image.load("../src/sprites/pipe.png").convert()
    main_font = pygame.font.Font("../src/fonts/04B_19.TTF", 30)


except Exception as e:
    print("Error parsing:", e)


def collision_detection(bird, base, pipe):
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
    col_top_pipe, col_bottom_pipe = pipe.get_rect()
    col_base = base.get_rect()

    if bird.collision(col_base, col_top_pipe, col_bottom_pipe):
        if col_top_pipe:
            pass


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
    bird = Bird(bird_midflap, 100, 256)
    base = Base(base_surface, 460)
    pipe = Pipe(pipe_surface, 350)
    score = Score(main_font, game_state)

    # event variables
    run = True
    space_on = False
    pipe_list = []

    pygame.time.set_timer(spawn_pipe, 1200)

    while run:
        clock.tick(80)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = True
                    space_on = True
                    bird.move(space_on)
                    space_on = False

            if event.type == spawn_pipe and game_state:
                pipe_list.extend(pipe.create())
                render_screen(bird, base, pipe, pipe_list, score)
                # pipe_list.extend(Pipe.create_pipe(pipe_image, pipe_height))

        # display the screen
        render_screen(bird, base, pipe, pipe_list, score)

        # collision detection
        collision_detection(bird, base, pipe)

        # game functions for objects
        pipe.move(pipe_list)
        bird.move(space_on)
        base.move()

        pygame.display.update()

    # to clear all the pipes as soon as the game ends
    pipe_list.clear()


if __name__ == "__main__":
    main()
