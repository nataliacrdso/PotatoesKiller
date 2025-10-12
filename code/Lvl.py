import random
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import C_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, C_PURPLE, EVENT_TIMEOUT, TIMEOUT_STEP, \
TIMEOUT_LEVEL, WIN_WIDTH, C_GREEN
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.Boss import BossDialogue, Boss, BossAttack
from code.PlayerShoot import PlayerShoot


class Lvl:
    def __init__(self, window: Surface, name: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []

        static_indices = ['Level1Bg0', 'Level1Bg1', 'Level1Bg9', 'Level1Bg10', 'Level1Bg11']

        for i in range(12):
            bg_name = f'Level1Bg{i}'
            bg = EntityFactory.get_entity(bg_name)
            if bg_name in static_indices:
                self.entity_list.append(bg)
            else:
                self.entity_list.append(bg)
                bg_copy = EntityFactory.get_entity(bg_name)
                bg_copy.rect.left = WIN_WIDTH
                self.entity_list.append(bg_copy)

        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

        self.static_bg_names = static_indices

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font('./assets/fonts/PressStart2P.ttf', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load('./assets/audio/retroSong.wav')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        all_sprites = pygame.sprite.Group()
        boss_group = pygame.sprite.Group()
        boss_attacks = pygame.sprite.Group()

        boss_surf = pygame.image.load('./assets/backgrounds/boss.png').convert_alpha()
        boss_surf = pygame.transform.scale(boss_surf, (100, 100))
        boss_dialogue_start = BossDialogue(boss_surf, "You won't escape my potatoes!!!\n\n\nGet ready!!!",
                                           duration_seconds=5, font_size=9)
        boss_dialogue_start_active = True

        boss_spawned = False
        boss_dialogue_mid = None
        boss_entity = None
        last_boss_attack = 0
        boss_attack_interval = 1000

        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                if hasattr(ent, 'surf'):
                    self.window.blit(ent.surf, ent.rect)

                if isinstance(ent, Entity) and ent.name not in self.static_bg_names:
                    ent.move()
                    if hasattr(ent, 'hitbox'):
                        ent.hitbox.center = ent.rect.center

                if isinstance(ent, Player):
                    shoot = ent.shoot()
                    if shoot:
                        self.entity_list.append(shoot)

                    self.level_text(10, f'Health: {ent.health}', C_GREEN, (10,20))
                    self.level_text(10, f'| Score: {ent.score}', C_PURPLE, (135, 20))
                    self.level_text(10, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
                    self.level_text(10, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 15))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY and not boss_spawned:
                    self.entity_list.append(EntityFactory.get_entity('potato'))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player):
                                player_score[0] = ent.score
                        return True

            if not any(isinstance(ent, Player) for ent in self.entity_list):
                return False

            if boss_dialogue_start_active:
                boss_dialogue_start.update(self.window, position=(100, WIN_HEIGHT - 80), size=(300, 70))
                if not boss_dialogue_start.active:
                    boss_dialogue_start_active = False

            if not boss_spawned:
                player = next((p for p in self.entity_list if isinstance(p, Player)), None)
                if player and player.score >= 3000:
                if player and player.score >= 5000:
                    boss_spawned = True
                    self.entity_list = [ent for ent in self.entity_list if not isinstance(ent, Enemy)]

                    boss_dialogue_mid = BossDialogue(
                        boss_surf,
                        "You escaped my potatoes, but\n you won't escape me!!!\n\n YOU WILL NEVER BEAT\n THE KING OF POTATOES!!!",
                        duration_seconds=10,
                        font_size=9
                    )

                    boss_entity = Boss()
                    boss_entity.rect.topleft = (WIN_WIDTH, 150)
                    boss_entity.life = 2000
                    boss_entity.speed_x = -3
                    boss_entity.target_x = WIN_WIDTH // 2

                    boss_group.add(boss_entity)
                    all_sprites.add(boss_entity)

            if boss_dialogue_mid and boss_dialogue_mid.active:
                boss_dialogue_mid.update(self.window, position=(100, WIN_HEIGHT - 80), size=(300, 70))
            else:
                if boss_entity:
                    if not boss_entity.active:
                        if boss_entity.rect.x > boss_entity.target_x:
                            boss_entity.rect.x += boss_entity.speed_x
                        else:
                            boss_entity.rect.x = boss_entity.target_x
                            boss_entity.active = True
                            boss_entity.vertical_timer = pygame.time.get_ticks()


                    else:
                        now = pygame.time.get_ticks()
                        if now - getattr(boss_entity, 'vertical_timer', 0) > 1000:
                            boss_entity.rect.y += random.randint(-50, 50)
                            boss_entity.rect.y = max(50, min(WIN_HEIGHT - 150, boss_entity.rect.y))
                            boss_entity.vertical_timer = now

                        if now - last_boss_attack > boss_attack_interval:
                            attack_y = boss_entity.rect.centery + random.randint(-20, 20)
                            attack = BossAttack(boss_entity.rect.left, attack_y)
                            boss_attacks.add(attack)
                            all_sprites.add(attack)
                            last_boss_attack = now


                        if hasattr(boss_entity, 'update'):
                            boss_entity.update()

                    self.window.blit(boss_entity.image, boss_entity.rect)

                    if boss_entity:
                        font = pygame.font.Font('./assets/fonts/PressStart2P.ttf', 10)  # você pode trocar 36 pelo tamanho que quiser
                        life_text = font.render(f"King of Potatoes: {int(boss_entity.life)}", True, (150, 2, 0))
                        self.window.blit(life_text, (10, 35))

            if boss_entity and boss_entity.active:
                now = pygame.time.get_ticks()
                if now - boss_entity.last_move_time > boss_entity.move_interval:
                    boss_entity.rect.y = random.randint(50, WIN_HEIGHT - 150)
                    boss_entity.last_move_time = now

                if boss_entity and boss_entity.active:
                    now = pygame.time.get_ticks()
                    if now - last_boss_attack > boss_attack_interval:
                        attack_y = boss_entity.rect.centery + random.randint(-20, 20)
                        boss_attacks.add(BossAttack(boss_entity.rect.left, attack_y))
                        last_boss_attack = now

            boss_group.update()
            boss_attacks.update()
            boss_group.draw(self.window)
            boss_attacks.draw(self.window)

            if boss_entity:
                player_shots = [e for e in self.entity_list if isinstance(e, PlayerShoot)]

                for shot in player_shots:
                    if boss_entity.rect.colliderect(shot.rect):
                        boss_entity.life -= shot.damage
                        self.entity_list.remove(shot)
                        if boss_entity.life <= 0:
                            return True

            if boss_attacks:
                for attack in boss_attacks:
                    if player.rect.colliderect(attack.rect):
                        player.health -= 50
                        boss_attacks.remove(attack)
                        if player.health <= 0:
                            return False

            pygame.display.flip()
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)
