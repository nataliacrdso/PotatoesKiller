import pygame.key
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShoot import PlayerShoot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        spritesheet = pygame.image.load('./assets/backgrounds/Player1.png').convert_alpha()
        frame_width = spritesheet.get_width() // 6
        frame_height = spritesheet.get_height()
        self.frames = []
        for i in range(6):
            frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frame = pygame.transform.flip(frame, True, False)
            self.frames.append(frame)

        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        self.animation_speed = 0.05
        self.animation_timer = 0
        self.facing_right = True
        self.hitbox = self.rect.inflate(-50, -50)

    def update_animation(self):
        self.animation_timer += self.animation_speed
        if self.animation_timer >= 1:
            self.animation_timer = 0
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.frame_index = 0
            self.surf = self.frames[self.frame_index]
            if self.facing_right:
                self.surf = self.frames[self.frame_index]
            else:
                self.surf = pygame.transform.flip(self.frames[self.frame_index], True, False)

    def move(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            self.facing_right = False

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
            self.facing_right = True

        self.update_animation()
        self.hitbox.center = self.rect.center

        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShoot('mage', self.rect.center)
            else:
                return None
