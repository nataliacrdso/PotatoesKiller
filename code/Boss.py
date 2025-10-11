import pygame
from pygame import Surface, Rect
import random
from code.Const import WIN_WIDTH
from code.Entity import Entity


class BossDialogue:
    def __init__(self, boss_surf: Surface, text: str, duration_seconds: float = 10, font_size: int = 10):
        self.boss_surf = boss_surf
        self.text = text
        self.duration = duration_seconds * 1000
        self.font_size = font_size
        self.active = True
        self.start_time = pygame.time.get_ticks()
        self.current_text = ""
        self.text_index = 0
        self.last_update = pygame.time.get_ticks()
        self.typing_speed = 50

        self.font = pygame.font.Font('./assets/fonts/PressStart2P.ttf', self.font_size)

    def update(self, screen: Surface, position=(100, 200), size=(250, 70)):
        now = pygame.time.get_ticks()

        if self.text_index < len(self.text):
            if now - self.last_update > self.typing_speed:
                self.current_text += self.text[self.text_index]
                self.text_index += 1
                self.last_update = now

        dialogue_rect = Rect(position, size)
        pygame.draw.rect(screen, (255, 255, 255), dialogue_rect)

        boss_pos = (position[0] - self.boss_surf.get_width() - 5, position[1] - 15)
        screen.blit(self.boss_surf, boss_pos)

        lines = self.current_text.split("\n")
        for i, line in enumerate(lines):
            text_surf = self.font.render(line, True, (0, 0, 0))
            text_rect = text_surf.get_rect(left=position[0] + 10, top=position[1] + 5 + i * (self.font_size + 2))
            screen.blit(text_surf, text_rect)

        if now - self.start_time > self.duration:
            self.active = False


class Boss(Entity, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(name='bossB', position=(WIN_WIDTH, 150))
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/backgrounds/bossB.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.rect.x = 576
        self.rect.y = 150

        self.speed_x = -2
        self.speed_y = 1
        self.active = False
        self.stopped = False
        self.stop_x = 245

        self.life = 2000
        self.last_move_time = pygame.time.get_ticks()
        self.move_interval = 1000
        self.damage = 50

    def move(self):
        if self.active:
            self.rect.y += random.randint(-5, 5)

class BossAttack(Entity, pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(name='bossAttack', position=(x, y))
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load("assets/backgrounds/bossAttack.png").convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -5
        self.angle = 0
        self.rotation_speed = 5

    def update(self):
        self.rect.x += self.speed
        self.angle = (self.angle + self.rotation_speed) % 360
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        self.rect = self.image.get_rect(center=self.rect.center)

        if self.rect.right < 0:
            self.kill()

    def move(self):
        self.rect.x += self.speed
