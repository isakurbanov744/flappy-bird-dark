import pygame


class Bird:
    velocity = 0
    gravity = 0.25

    def __init__(self, img, x_pos, y_pos):
        """
            :param img: Bird image file
            :param x_pos: x coordinate of the bird
            :param y_pos: y coordinate of the bird
        """
        self.x = x_pos
        self.y = y_pos
        self.bird_img = img
        self.bird_rect = self.bird_img.get_rect(center=(self.x, self.y))
        self.velocity = 0
        self.mass = 1

    def move(self, space_on):
        """
            if space_on == True, move the Bird object up by 6 units
            self.velocity = 0 resets the current speed to 0
            self.gravity is added to self.velocity
            y coordinate of rectange of the object is moved up or down
            :param space_on: Boolean value which is True
            :return: None
        """

        if space_on:
            self.velocity = 0
            self.velocity -= 6

        self.velocity += self.gravity
        self.bird_rect.centery += self.velocity

    def draw(self, window):
        """
            :param window: main game surface
            :return: self.bird_img, self.bird_rect
        """
        window.blit(self.bird_img, self.bird_rect)

    def collision(self, rect):
        """
            :param rect: bird rectangle
            :return: True if bird rectangle collides
        """
        return self.bird_rect.colliderect(rect)
