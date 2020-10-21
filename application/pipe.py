import pygame
import random

class Pipe:

  def __init__(self, img, x_pos):
    self.pipe_top_image = img
    self.pipe_bottom_image = pygame.transform.flip(img, False, True)
    self.pipe_height = [225, 300, 350, 400]
    self.x = x_pos
    self.y = random.choice(self.pipe_height)
    self.pipe_top_rect = self.pipe_top_image.get_rect(midbottom=(350, self.y - 150))
    self.pipe_bottom_rect = self.pipe_bottom_image.get_rect(midtop=(350, self.y))

  def create(self):
    return self.pipe_top_rect, self.pipe_bottom_rect

  def move(self, pipes):
        for pipe in pipes:
            pipe.centerx -= 5
        return pipes


  def draw(self, window, pipes):
    for pipe in pipes:
      if pipe.bottom >= 512:
        window.blit(self.pipe_top_image, pipe)
      else:
        window.blit(self.pipe_bottom_image, pipe)

