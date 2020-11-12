import pygame
from sound import Sound
import random


class Bird:
    velocity = 0
    gravity = 0.25
    sound = Sound()

    def __init__(self, x_pos, y_pos, purple_bird_surface, yellow_bird_surface):
        """
            :param bird_surface: list of all bird images
            :param x_pos: x coordinate of the bird
            :param y_pos: y coordinate of the bird
        """
        self.x = x_pos
        self.y = y_pos
        self.purple_bird_surface = purple_bird_surface
        self.yellow_bird_surface = yellow_bird_surface
        self.bird_surface = [self.purple_bird_surface, self.yellow_bird_surface]
        self.velocity = 0
        self.mass = 1
        self.index = 0
        self.bird_img = self.purple_bird_surface[self.index]
        self.bird_rect = self.bird_img.get_rect(center=(self.x, self.y))
        self.bird_rot_img = None
        self.rot_bird = None

    def reset(self):
        self.bird_rect.center = (100, 256)
        self.velocity = 0

    def move(self):
        """
            if space_on == True, move the Bird object up by 6 units
            self.velocity = 0 resets the current speed to 0
            self.gravity is added to self.velocity
            y coordinate of rectangle of the object is moved up or down
            :return: None
        """
        self.velocity += self.gravity
        self.bird_rect.centery += self.velocity

    def jump(self):
        """
             resets the bird velocity to prevent it from jumping to high
             moves the bird up by 6 pixels
            :var self.sound.flap: flap sound file
            :return: None
        """
        self.velocity = 0
        self.velocity -= 6

        # plays flap sound
        self.sound.flap.play()

    def collision(self, base_rect):
        """
            :param base_rect: base rectangle
            :return: True if bird rectangle collides
        """
        if self.bird_rect.colliderect(base_rect):
            return True

        return False

    def animation(self):
        """
             animates the bird wings
            :var self.index: index position for the bird images
            :return: PyGame surface
        """
        self.index += 1

        if self.index > 2:
            self.index = 0

        return self.purple_bird_surface[self.index]

    def rotate(self):
        """
             rotates the bird using rotozoom
            :var self.rot_bird: rotated bird surface
            :return:
        """
        self.rot_bird = pygame.transform.rotozoom(self.purple_bird_surface[self.index], -self.velocity * 5, 1)

        return self.rot_bird

    def surface(self):
        self.purple_bird_surface = random.choice(self.bird_surface)

    def draw(self, window):
        """
            :param window: main game surface
            :return: self.bird_img, self.bird_rect
        """
        self.bird_img = self.animation()
        self.bird_rot_img = self.rotate()

        window.blit(self.bird_rot_img, self.bird_rect)
