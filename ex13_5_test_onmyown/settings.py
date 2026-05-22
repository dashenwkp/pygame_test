class Settings:
    '''管理游戏所有的设置'''

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 火箭设置
        self.rocket_speed = 10.0

        # 子弹设置
        # Bullet settings
        self.bullet_speed = 6.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        # alien_frequency越大, 外星人生成的频率越高
        self.alien_speed = 1.5
        self.alien_frequency = 0.008