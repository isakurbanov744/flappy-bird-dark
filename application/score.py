import pygame

score = 0


class Score:

    def __init__(self, font, game_run):
        self.font = font
        self.score = score
        self.high_score = 0
        self.game_state = game_run

    def add_score(self):
        self.score += 0.01

    def display(self, window):
        if self.game_state:
            score_text = self.font.render(str(int(self.score)), True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(144, 60))
            window.blit(score_text, score_rect)

        if not self.game_state:
            score_text = self.font.render(f"Score: {int(self.score)}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(144, 60))
            window.blit(score_text, score_rect)

            high_score_text = self.font.render(f"High Score: {int(self.high_score)}", True, (255, 255, 255))
            high_score_rect = high_score_text.get_rect(center=(144, 420))
            window.blit(high_score_text, high_score_rect)

    def update(self):
        if self.score > self.high_score:
            self.high_score = self.score
        return self.high_score
