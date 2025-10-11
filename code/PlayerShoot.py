import pygame
from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShoot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.image.load('./assets/backgrounds/mage.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (40, 40))
        self.rect = self.surf.get_rect(center=position)

    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name]