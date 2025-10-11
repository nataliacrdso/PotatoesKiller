import pygame
from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.image.load('./assets/backgrounds/potato.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.hitbox = self.rect.inflate(-60, -60)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        self.hitbox.center = self.rect.center

