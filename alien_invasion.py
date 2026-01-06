import sys, pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    # Clase general para gestionar los assets y el comportamiento del juego
    def __init__(self):
    # Inicializa el juego y crea recursos para el juego.
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Resolucion de la ventana
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        """
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        """

        self.background_image = pygame.image.load('images/space_back.png')
        self.background_image = pygame.transform.scale(self.background_image, (self.settings.screen_width, self.settings.screen_height))


        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        # Empieza un bucle principal para el juego
        while True:
        # Esté atento a los eventos del teclado y el mouse
            self.__check__events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self.__update__screen()
            self.clock.tick(60)

    def __check__events(self):
        # Responde al presionar una tecla del teclado o un movimiento del mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # Respuestas al presionar una tecla
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        # Respuestas despues de presionar una tecla
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """Actualizar las posiciones de las balas y desacerse de las balas antiguas"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            
        # Verificar para cada bala que haya tocado a aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _fire_bullet(self):
        # Crear una nueva bala y agregarlo al grupo de balas
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def __update__screen(self):
        # Actualizar imagenes en la pantalla, y ir a la proxima pantalla
        self.screen.blit(self.background_image, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
    
        pygame.display.flip()
    
    def _create_fleet(self):
        """ Create the fleet of aliens. """
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 6 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """ Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _update_aliens(self):
        """ Actualizar las posiciones de todos los aliens de la flota"""
        self._check_fleet_edges()
        self.aliens.update()
    
    def _check_fleet_edges(self):
        """ Responder si cualquier alien ha llegado al borde """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """ Quitar toda la flota y cambia la direccion de la flota. """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
if __name__ == '__main__':
    # Hace una instancia del juego, y corre el juego
    ai = AlienInvasion()
    ai.run_game()