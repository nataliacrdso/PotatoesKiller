from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.PlayerShoot import PlayerShoot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShoot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        if (isinstance(ent1, Player) and isinstance(ent2, Enemy)) or (
                isinstance(ent2, Player) and isinstance(ent1, Enemy)):

            player = ent1 if isinstance(ent1, Player) else ent2
            enemy = ent2 if isinstance(ent2, Enemy) else ent1

            if (player.hitbox.right >= enemy.hitbox.left and
                    player.hitbox.left <= enemy.hitbox.right and
                    player.hitbox.bottom >= enemy.hitbox.top and
                    player.hitbox.top <= enemy.hitbox.bottom):

                player.health -= 100
                enemy.health = 0
                player.last_dmg = enemy.name
            return

        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShoot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShoot) and isinstance(ent2, Enemy):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name


    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'mage':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:
            if ent is None:
                continue
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
