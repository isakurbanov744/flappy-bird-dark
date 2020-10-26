import pygame


class Bird:
    velocity = 0
    gravity = 0.25

    def __init__(self, x_pos, y_pos, bird_surface):
        """
            :param bird_surface: list of all bird images
            :param x_pos: x coordinate of the bird
            :param y_pos: y coordinate of the bird
        """
        self.x = x_pos
        self.y = y_pos
        self.bird_surface = bird_surface
        self.velocity = 0
        self.mass = 1
        self.index = 0
        self.bird_img = self.bird_surface[self.index]
        self.bird_rect = self.bird_img.get_rect(center=(self.x, self.y))

    def reset(self):
        self.bird_rect.center = (100, 256)
        self.velocity = 0

    def move(self):
        """
            if space_on == True, move the Bird object up by 6 units
            self.velocity = 0 resets the current speed to 0
            self.gravity is added to self.velocity
            y coordinate of rectangle of the object is moved up or down
            :param space_on: Boolean value which is True
            :return: None
        """
        self.velocity += self.gravity
        self.bird_rect.centery += self.velocity

    def jump(self):
        self.velocity = 0
        self.velocity -= 6

    def collision(self, base_rect):
        """
            :param top_pipe_rect: top pipe rectangle object
            :param bottom_pipe_rect: bottom pipe rectangle object
            :param base_rect: base rectangle
            :return: True if bird rectangle collides
        """
        if self.bird_rect.colliderect(base_rect):
            return True

        return False

    def animation(self):
        """
             this animates the bird
            :var self.index: index position for the bird images
            :return: PyGame surface
        """
        self.index += 1

        if self.index > 2:
            self.index = 0

        return self.bird_surface[self.index]

    def draw(self, window):
        """
            :param window: main game surface
            :return: self.bird_img, self.bird_rect
        """
        self.bird_img = self.animation()
        window.blit(self.bird_img, self.bird_rect)
