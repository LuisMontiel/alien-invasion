import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Una clase que representa un alien en una flota de aliens"""
    def __init__(self, ai_game):
        """ Inicializacion del alien y asignacion de la posicion de inicio """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        """ Cargar la imagen del alien y asignar el atributo del rectangulo """
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (75, 50))
        self.rect = self.image.get_rect()

        """ Iniciar cada alien en la parte superior a la izquierda de la pantalla """
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """ Almacenar la posicion exacta horizontal del alien """
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Regresar True si el alien esta al borde de la pantalla """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """ Mover el alien a la derecha """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    
    