import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

# Criando uma função que derá início ao jogo.

def run_game():
    '''Inicia o jogo'''
    pygame.init()  # configurações de fundo que não sei explicar, mas permite o funcionamento do pygame.
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # Cria uma tela com tamanho de 800x600 é uma tupla
    pygame.display.set_caption('Alien Invasion')  # O nome da tela criada em screen.
    ship = Ship(ai_settings, screen)

    while True:
        # Muda a cor do background antes de dar o flip.
        # Fica sempre criando um display novo, dandoa  sensação de movimento.
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        ship.update()
               

run_game()