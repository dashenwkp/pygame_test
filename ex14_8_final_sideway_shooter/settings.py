class Settings:
    '''管理游戏所有的设置'''

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_width = 15
        self.bullet_height = 3000
        self.bullet_color = (60, 60, 60)

        # 难度递增设置
        self.speedup_scale = 1.1
        self.frequency_scale = 1.15

        # 默认难度
        self.difficulty = 'medium'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化动态设置，包括火箭，子弹，外星人的速度，拥有的火箭数，
        允许发射的子弹数，以及外星人生成频率'''
        if self.difficulty == 'easy':
            self.rocket_limit = 5
            self.bullets_allowed = 10
            self.rocket_speed = 0.75
            self.bullet_speed = 1.5
            self.alien_speed = 0.5
            self.alien_frequency = 0.005
        elif self.difficulty == 'medium':
            self.rocket_limit = 3
            self.bullets_allowed = 3
            self.rocket_speed = 1.5
            self.bullet_speed = 3.0
            self.alien_speed = 1.0
            self.alien_frequency = 0.01
        elif self.difficulty == 'hard':
            self.rocket_limit = 2
            self.bullets_allowed = 3
            self.rocket_speed = 3.0
            self.bullet_speed = 6.0
            self.alien_speed = 2.0
            self.alien_frequency = 0.02

    def increase_difficulty(self):
        '''增加游戏难度'''
        self.rocket_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_frequency *= self.frequency_scale