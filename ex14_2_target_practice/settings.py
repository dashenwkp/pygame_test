class Settings:
    '''管理所有设置的类'''

    def __init__(self):
        '''所有的设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 5.0

        # 子弹设置
        self.bullet_speed = 10.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 靶子设置
        self.target_height = 120
        self.target_width = 15
        self.target_color = (180, 60, 10)
        self.target_speed = 1.5

        # 允许没射中的次数
        self.miss_limit = 3