class Settings():
    def __init__(self) -> None:
        """Setup the game settings"""
        self.bg = (0, 0, 0)
        self.screenWidth = 1200
        self.screenHeight = 800
        self.lives = 3
        self.pelletScore = None
        self.powerPelletScore = None
        self.initialize_pellet_scores()
        self.initialize_speed_settings()

    def initialize_pellet_scores(self) -> None:
        self.pelletScore = 10
        self.powerPelletScore = 100

    def initialize_speed_settings(self) -> None:
        self.playerSpeed = 3
        self.ghostSpeed = 3