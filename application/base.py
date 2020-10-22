import pygame


class Base:
    velocity = int(2)

    def __init__(self, img, y_pos):
        """
            :param img: Base image
            :param y_pos: y coordinate of base
            :var self.base_rect: rectangle of the base image
            :var velocity: speed at which the base moves
        """
        # self.x = x_pos
        self.y = y_pos
        self.base_img = img
        self.base_rect = self.base_img.get_rect()
        self.width = self.base_img.get_width()
        self.x1 = 0
        self.x2 = self.width

    def move(self):
        """
         moves the base along the game screen

        :return: None
        """
        self.x1 -= self.velocity
        self.x2 -= self.velocity
        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def draw(self, window):
        """
             draws the base along the screen
            :param window: main PyGame surface
            :return: None
        """
        self.base_rect.centerx = self.x1
        self.base_rect.centery = self.y
        self.base_rect.centerx = self.x2
        self.base_rect.centery = self.y

        window.blit(self.base_img, (self.x1, self.y))
        window.blit(self.base_img, (self.x2, self.y))

    def get_rect(self):
        """
            :return: rectangle of the base image
        """
        return self.base_rect
