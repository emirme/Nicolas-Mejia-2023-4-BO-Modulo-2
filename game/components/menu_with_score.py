import pygame
from game.components.menu import Menu
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE

class MenuWithScore(Menu):
    def __init__(self, message, screen, score, highest_score, total_deaths):
        super().__init__(message, screen)
        self.score = score
        self.highest_score = highest_score
        self.total_deaths = total_deaths

    def draw(self, screen):
        super().draw(screen)
        self.draw_score(screen)
        self.draw_highest_score(screen)
        self.draw_total_deaths(screen)

    def draw_score(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'You score: {self.score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)
        screen.blit(text, text_rect)

    def draw_highest_score(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Highest score: {self.highest_score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)
        screen.blit(text, text_rect)

    def draw_total_deaths(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Total deaths: {self.total_deaths}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)
        screen.blit(text, text_rect)




