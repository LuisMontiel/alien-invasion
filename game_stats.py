class GameStats:
    """ Estadisticas para el juevo"""
    def __init__(self, ai_game):
        """ Estadisticas iniciales. """
        self.settings = ai_game.settings
        self.reset_stats()
        # Puntuajes altos nunca deberian de ser reseteados.
        self.high_score = 0

    def reset_stats(self):
        """ Inicializar estadisticas que pueden cambiar durante el juego. """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1