import pygame, settings

class Ship:
    # Una clase para manejar la nave espacial
    def __init__(self, ai_game):
        # Inicializar la nave y asignarla en la posicion de inicio
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen de la nave y tomar su rect
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        # Empezar cada nave en la parte centroinferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

        # Almacenar un numero float para la posicion horizontal exacta de la nave
        self.x = float(self.rect.x)

        # Flag de movimiento; empieza con una nave sin movimiento
        self.moving_right = False
        self.moving_left = False

    
    def update(self):
        # Actualiza la posicion de la nave basado en el movimiento de la flag
        # Actualizar el valor x de la nave, no del rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        self.rect.x = self.x


    def blitme(self):
        # Dibujar la nave en su locacion actual
        self.screen.blit(self.image, self.rect)