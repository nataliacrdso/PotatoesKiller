import pygame

C_LATTE = (247, 243, 227)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_PURPLE = (17, 19, 68)
C_CYAN = (0, 128, 128)
C_GREEN = (39, 64, 41)
C_RED = (150, 2, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level1Bg7': 7,
    'Level1Bg8': 8,
    'Level1Bg9': 9,
    'Level1Bg10': 10,
    'Level1Bg11': 11,
    'Player1': 2,
    'mage': 1,
    'potato': 1,
    'bossB': 2,
    'bossAttack': 1,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Level1Bg8': 999,
    'Level1Bg9': 999,
    'Level1Bg10': 999,
    'Level1Bg11': 999,
    'Player1': 1500,
    'mage': 1,
    'potato': 50,
    'bossB': 2000,
    'bossAttack': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level1Bg8': 0,
    'Level1Bg9': 0,
    'Level1Bg10': 0,
    'Level1Bg11': 0,
    'Player1': 1,
    'mage': 25,
    'potato': 1,
    'bossB': 1,
    'bossAttack': 50,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level1Bg8': 0,
    'Level1Bg9': 0,
    'Level1Bg10': 0,
    'Level1Bg11': 0,
    'Player1': 0,
    'mage': 0,
    'potato': 100,
    'bossB': 0,
    'bossAttack': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 5,
    'bossB': 5,
}

# M
MENU_OPTION = ('Start',
               'Exit')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}

PLAYER_KEY_SHOOT = {'Player1': pygame.K_x}


# S
SPAWN_TIME = 1000

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 500000  # 20s
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }