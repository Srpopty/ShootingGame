class Settings():
    def __init__(self):
        self.screen_width=1200
        self.screen_height=700
        self.bg_color=(230,230,230)
        self.ship_limit=3
        self.bullets_allowed=5
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.fleet_drop_speed=10
        self.speedup_scale=1.2
        self.score_scale=1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.fleet_direction=1
        self.alien_point=50
        self.bullet_speed_factor=2
        self.ship_speed_factor=1.5
        self.alien_speed_factor=1

    def increase_speed(self):
        self.bullet_speed_factor*=self.speedup_scale
        self.ship_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_point=int(self.alien_point*self.score_scale)