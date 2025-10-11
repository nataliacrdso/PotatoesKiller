import pygame
import sys

def mostrar_creditos(vitoria=True):

    pygame.init()

    WIDTH, HEIGHT = 576, 324
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Créditos")

    font = pygame.font.Font('./assets/fonts/PressStart2P.ttf', 10)
    color = (146, 151, 196)

    if vitoria:
        initial_msg = "You win!!! Thanks for playing!"
    else:
        initial_msg = "Game Over! Try again!"

    credits = [
        initial_msg,
        "Game develop by Natalia Cardoso",
        "Image credits:",
        "Background created by Eder Muniz",
        "https://www.gamedevmarket.net/member/edermuniz14/",
        "https://edermuniz.carrd.co/",
    ]

    credit_surfaces = [font.render(line, True, color) for line in credits]
    y_positions = [HEIGHT + i * 40 for i in range(len(credit_surfaces))]
    speed = 1
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((243, 255, 189))
        for i, surface in enumerate(credit_surfaces):
            y_positions[i] -= speed
            screen.blit(surface, (WIDTH//2 - surface.get_width()//2, y_positions[i]))

        if y_positions[-1] < -50:
            running = False

        pygame.display.flip()
        clock.tick(60)




