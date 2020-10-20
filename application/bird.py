import pygame


class Bird:
    bird_movement = 0
    gravity = 0.25

    def __init__(self, img, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.bird_img = img
        self.bird_rect = self.bird_img.get_rect(center=(self.x, self.y))
        self.velocity = 0
        self.mass = 1
        self.tick_count = 0

    def move(self, space_on):
        """
        mvoe in terms of x_pos and y_pos
        needs displacement
        :return:
        """

        if space_on == True:
            self.bird_movement = 0
            self.bird_movement -= 6

        self.bird_movement += self.gravity
        self.bird_rect.centery += self.bird_movement

        self.bird_rect.centery += self.bird_movement

    def draw(self, window):
        window.blit(self.bird_img, self.bird_rect)
