class Settings:
    '''管理游戏所有的设置'''

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 火箭设置
        self.rocket_speed = 10.0