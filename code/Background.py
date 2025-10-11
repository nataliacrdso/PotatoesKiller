from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity
import pygame


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = self.scale_background(self.surf)

    def scale_background(self, surf):
        return pygame.transform.scale(surf, (WIN_WIDTH, WIN_HEIGHT))

    def move(self):
        if hasattr(self, 'static') and self.static:
            return
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH - 1

