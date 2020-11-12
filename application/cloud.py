import pygame
import random


class Cloud:

    def __init__(self, cloud_surface, x_pos, y_pos):
        """
            :param cloud_surface: list of cloud images
            :param x_pos: x position of the cloud object
            :param y_pos: y position of the cloud object
        """
        self.x = x_pos
        self.y = y_pos
        self.x2 = 425
        self.y2 = y_pos
        self.cloud_surface = cloud_surface
        self.cloud_height = [70, 100, 20]
        self.cloud_img = self.cloud_surface[0]
        self.cloud_img_two = self.cloud_surface[1]
        self.cloud_rect = self.cloud_img.get_rect(midtop=(self.x, self.y))
        self.pos = random.choice(self.cloud_height)

    def position(self):
        """
             returns a random position for clouds
            :return: random int number
        """
        self.pos = random.choice(self.cloud_height)

        return self.pos

    def move(self):
        """
             keeps drawing clouds on the screen as they move out of the screen
            :var self.cloudx_pos: x position of the cloud
            :return: pipes moving to the left by 5 units
        """
        self.x -= 1
        if self.x <= -288:
            self.x = 350

        self.x2 -= 1
        if self.x2 <= -325:
            self.x2 = 425

    def draw(self, window):
        """
             draws clouds on the screen
            :param window: display surface for PyGame
            :return: None
        """
        # if the cloud is lost from the screen
        # change the position
        if self.x == -50:
            self.y = self.position()

        if self.x2 == -100:
            self.y2 = self.position()
        
        window.blit(self.cloud_img, (self.x, self.y))
        window.blit(self.cloud_img_two, (self.x2, self.y2))
