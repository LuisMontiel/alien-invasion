import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Una clase que maneja las balas disparadas por la nave """

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Crear una bala/rect en la posicion(0,0) y despues asignar la posicion correcta
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Almacenar la posicion de la nave en un valor float
        self.y = float(self.rect.y)

    def update(self):
        """ Mover la bala arriba de la pantalla """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)