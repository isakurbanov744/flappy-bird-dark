import pygame


class Base:
    velocity = 2

    def __init__(self, img, y_pos):
        """
            :param img: Base image
            :param y_pos: y coordinate of base
            :var self.base_rect: rectangle of the base image
            :var velocity: speed at which the base moves
        """
        self.y = y_pos
        self.base_img = img
        self.width = self.base_img.get_width()
        self.x1 = 0
        self.x2 = self.width
        self.base_rect = self.base_img.get_rect(center=(self.x1, self.y))
        self.basex_pos = 0

    def move(self):
        """
             moves the base along the game screen
            :return: None
        """
        self.basex_pos -= 1

        if self.basex_pos <= -288:
            self.basex_pos = 0

    def draw(self, window):
        """
             draws the base along the screen
            :param window: main PyGame surface
            :return: None
        """
        window.blit(self.base_img, (self.basex_pos, 410))
        window.blit(self.base_img, (self.basex_pos + 288, 410))

    def get_rect(self):
        """
            :return: rectangle of the base image
        """
        return self.base_rect
