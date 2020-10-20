import pygame


class Bird:

    def __init__(self, img, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.bird_img = img
        self.bird_rect = self.bird_img.get_rect(center=(self.x, self.y))

    def move(self):
        """
        mvoe in terms of x_pos and y_pos
        needs displacement
        :return:
        """
        pass

    def jump(self):
        """
        jump with velocity
        :return: None
        """
        pass

    def draw(self, window):

        window.blit(self.bird_img, self.bird_rect)
