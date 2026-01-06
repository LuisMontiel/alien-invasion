class Settings:
    # Una clase que almacena todas las configuraciones para Alien Invasion
    def __init__(self):
        # Inicializar las configuraciones del juego
        # Configuraciones de la pantalla
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (41, 12, 7)

        # Configuracion de la nave
        self.ship_speed = 10

        # Configuracion de balas
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (235, 255, 0)
        self.bullets_allowed = 3

        # Configuracion de los aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction de uno representa derecha; -1 representa izquierda
        self.fleet_direction  =1