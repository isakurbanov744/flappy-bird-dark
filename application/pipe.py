import pygame
import random
from score import Score

class Pipe:

    def __init__(self, img, x_pos):
        """
          :param img: pipe image
          :param x_pos: x position of the pipe on PyGame graph
          :param self.y: y position of the pipe image on the PyGame graph
          :param self.pipe_top_image: image of the top pipe
          :param self.pipe_bottom_image: image of the bottom pipe
          :param self.pipe_height: length the pipe can take
          :param self.pipe_top_rect: rectangle for the top pipe image
          :param self.pipe_bottom_rect: rectangle for the bottom pipe image
        """
        self.y = 0
        self.pipe_top_image = img
        self.pipe_bottom_image = pygame.transform.flip(img, False, True)
        self.pipe_height = [225, 300, 350, 400]
        self.x = x_pos
        self.pipe_top_rect = self.pipe_top_image.get_rect()
        self.pipe_bottom_rect = self.pipe_bottom_image.get_rect()

    def create(self):
        """
          :return: top rectangle and bottom rectangle
        """
        self.y = random.choice(self.pipe_height)
        self.pipe_top_rect = self.pipe_top_image.get_rect(midbottom=(350, self.y - 150))
        self.pipe_bottom_rect = self.pipe_bottom_image.get_rect(midtop=(350, self.y))
        return self.pipe_top_rect, self.pipe_bottom_rect

    def move(self, pipes):
        """
          :param pipes: list of all the pipes in the current game
          :return: pipes moving to the left by 5 units
        """
        for pipe in pipes:
            pipe.centerx -= 5
        return pipes

    def draw(self, window, pipes):
        """
          :param window: display surface for PyGame
          :param pipes: list of all the pipes in the current game
          :return: None
        """
        for pipe in pipes:
            if pipe.bottom >= 512:
                # if the position of the pipe is above 512
                window.blit(self.pipe_top_image, pipe)
            else:
                # if the position of te pipe is below 512
                window.blit(self.pipe_bottom_image, pipe)

    def get_rect(self):
        """
            :return: rectangle of top and bottom pipe images
        """
        return self.pipe_top_rect, self.pipe_bottom_rect
