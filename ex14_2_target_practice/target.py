import pygame

class Target:
    '''管理靶子的类'''

    def __init__(self, tp_game):
        '''创建靶子并放到屏幕右边'''
        self.settings = tp_game.settings
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(
            0, 0, self.settings.target_width, self.settings.target_height)
        self.rect.midright = self.screen.get_rect().midright

        # 存储精确的y坐标
        self.y = float(self.rect.y)

        # 移动方向为1时向下移动，为2时向上移动
        self.direction = 1

    def update(self):
        '''上下移动靶子'''
        self.y += self.direction * self.settings.target_speed
        if self.rect.top < 0:
            self.rect.top = 0
            self.direction = 1
        elif self.rect.bottom > self.screen_rect.bottom:
            self.bottom = self.screen_rect.bottom
            self.direction = -1
        self.rect.y = self.y

    def draw_target(self):
        '''在屏幕上绘制靶子'''
        pygame.draw.rect(self.screen, self.settings.target_color, self.rect)