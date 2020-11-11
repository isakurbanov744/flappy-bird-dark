import pygame

pygame.mixer.init()

class Sound():
    def __init__(self):
        self.flap = pygame.mixer.Sound("../src/audio/wing.wav")
        self.death = pygame.mixer.Sound("../src/audio/hit.wav")
        self.score = pygame.mixer.Sound("../src/audio/point.wav")
