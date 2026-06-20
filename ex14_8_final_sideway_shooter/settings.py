class Settings:
    '''管理游戏所有的设置'''

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 火箭设置
        self.rocket_limit = 3

        # 子弹设置
        self.bullet_width = 15
        self.bullet_height = 3000
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20

        # 难度递增设置
        self.speedup_scale = 1.1
        self.frequency_scale = 1.15

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化动态设置'''
        self.rocket_speed = 10.0
        self.bullet_speed = 15.0
        self.alien_speed = 10.0

        # alien_frequency越大, 外星人生成的频率越高
        self.alien_frequency = 0.01

    def increase_difficulty(self):
        '''增加游戏难度'''
        self.rocket_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_frequency *= self.frequency_scale