import random
from code.Background import Background
from code.Boss import BossDialogue
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        # Se for background da fase 1
        if entity_name.startswith('Level1Bg'):
            return Background(entity_name, (0, 0))

        # Player
        if entity_name == 'Player1':
            return Player('Player1', (10, WIN_HEIGHT / 2 - 30))

        # Inimigo
        if entity_name == 'potato':
            return Enemy('potato', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

        elif entity_name == 'boss':
            return BossDialogue((300,100))
        else:
            return None

        print(f"[ERRO] Entidade '{entity_name}' não encontrada!")
        return None

