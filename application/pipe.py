import pygame
import random


class Pipe:

    def __init__(self, img, x_pos, pipe_list, score_class, score_add):
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
        self.pipe_height = [275, 300, 350]
        self.x = x_pos
        self.pipe_top_rect = self.pipe_top_image.get_rect()
        self.pipe_bottom_rect = self.pipe_bottom_image.get_rect()
        self.pipe_list = pipe_list
        self.score_class = score_class
        self.score_add = score_add
        self._pipe_list = []

    def create(self):
        """
            :return: top rectangle and bottom rectangle
        """
        self.y = random.choice(self.pipe_height)
        self.pipe_top_rect = self.pipe_top_image.get_rect(midbottom=(350, self.y - 150))
        self.pipe_bottom_rect = self.pipe_bottom_image.get_rect(midtop=(350, self.y))
        return self.pipe_top_rect, self.pipe_bottom_rect

    def move(self):
        """
            :var self._pipe_list: list of pipes that are visible in the screen
             this is to improve game performance
            :var self.pipe_list: list of all the pipes in the current game
            :return: pipes moving to the left by 5 units
        """
        for pipe in self.pipe_list:
            pipe.centerx -= 5

        self._pipe_list = [pipe for pipe in self.pipe_list if pipe.right > -50]

        return self._pipe_list

    def draw(self, window):
        """
            :param window: display surface for PyGame
            :param self.pipe_list: list of all the pipes in the current game
            :return: None
        """
        for pipe in self.pipe_list:
            if pipe.bottom >= 512:
                # if the position of the pipe is above 512
                window.blit(self.pipe_top_image, pipe)
            else:
                # if the position of te pipe is below 512
                window.blit(self.pipe_bottom_image, pipe)

    def get_rect(self):
        """
             creates rectangle for the current object
            :return: rectangle of top and bottom pipe images
        """
        return self.pipe_top_rect, self.pipe_bottom_rect

    def score(self):
        if self.pipe_list:
            for self.pipe in self.pipe_list:
                if self.pipe.centerx == 100 and self.score_add:
                    self.score_class.add_score()
                    self.score_add = False

                if self.pipe.centerx < 0:
                    self.score_add = True
