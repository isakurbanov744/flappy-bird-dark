import pygame
from sound import *


class Score:

    sound = Sound()

    def __init__(self, font, game_run):
        """
            :param font: font of the game
            :param game_run: Bool
            :var self.score: current game score
            :var self.high_score: highest score
        """
        self.font = font
        self.score = 0
        self.high_score = 0
        self.game_state = game_run

    def add_score(self):
        """
             adds 1 to the score
            :var self.game_state: Bool
            :return: None
        """
        if self.game_state:
            self.score += 1
            self.sound.score.play()

        self.update()

    def update(self):
        """
             updates the high score
            :return: self.high_score
        """
        if self.score > self.high_score:
            self.high_score = self.score
        return self.high_score

    def reset(self):
        """
             resets the score to 0
            :return: None
        """
        self.score = 0

    def display(self, window, game_state):
        """
             if self.game_state == True, it only displays the current game score
             if self.game_state != True, it shows both the current game score and high score
            :param window: PyGame window surface
            :param game_state: Bool
            :var score_text: the surface for writing the score
            :return: None
        """
        self.game_state = game_state
        if self.game_state:
            score_text = self.font.render(str(int(self.score)), True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(144, 60))
            window.blit(score_text, score_rect)

        if not self.game_state:
            score_text = self.font.render(f"Score: {int(self.score)}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(144, 60))
            window.blit(score_text, score_rect)

            high_score_text = self.font.render(f"High Score: {int(self.high_score)}", True, (255, 255, 255))
            high_score_rect = high_score_text.get_rect(center=(144, 380))
            window.blit(high_score_text, high_score_rect)
