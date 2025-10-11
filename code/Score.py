import sys
import pygame
from pygame import Surface
from code.DBproxy import DBproxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/backgrounds/Level1Bg0.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./assets/audio/retroSong.wav')
        pygame.mixer_music.play(-1)
        db_proxy = DBproxy('DBScore')
        name = ''
        while True:
            score = player_score[0]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


