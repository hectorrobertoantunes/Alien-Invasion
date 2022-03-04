import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        '''Inicializa a nave e a posição inicial'''

        self.screen = screen
        #  Carrega a imagem da nave
        self.image = pygame.image.load('images/nave.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #  Inicializa uma nova nave no centro inferior
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #   movement flag
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings
        self.center = float(self.rect.centerx)



    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center


    def blitme(self):
        '''Desenha a nave na localização '''
        self.screen.blit(self.image, self.rect)
