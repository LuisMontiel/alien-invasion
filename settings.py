class Settings:
    # Una clase que almacena todas las configuraciones para Alien Invasion
    def __init__(self):
        # Inicializar las configuraciones del juego
        # Configuraciones de la pantalla
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (41, 12, 7)

        # Configuracion de la nave
        self.ship_limit = 3

        # Configuracion de balas
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = (235, 255, 0)
        self.bullets_allowed = 3

        # Configuracion de los aliens
        self.fleet_drop_speed = 10

        # Que tan rapido el juego acelera
        self.speedup_scale = 1.1
        # Que tan rapido incrementan los valores de los puntos del alien
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """ Inicializa configuraciones que cambia durante el juego """
        self.ship_speed = 10
        self.bullet_speed = 5.0
        self.alien_speed = 5

        # fleet_direction de uno representa derecha; -1 representa izquierda
        self.fleet_direction = 1

        # Configuraciones de puntuaje
        self.alien_points = 50
    
    def increase_speed(self):
        """ Incrementar las configuraciones de la velocidad y los valores de los puntos del alien. """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

