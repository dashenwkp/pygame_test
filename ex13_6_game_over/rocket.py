import pygame
from settings import Settings

class Rocket:
    '''管理火箭的类'''

    def __init__(self, ss_game):
        '''加载火箭并将火箭放到屏幕左边的中间'''
        self.screen = ss_game.screen
        self.settings = Settings()
        self.image = pygame.image.load(
            r'ex13_6_game_over\images\rocket_small.png')
        self.rect = self.image.get_rect()
        self.screen_rect = ss_game.screen.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        # 存储精确的火箭y坐标
        self.y = self.rect.y

        # 设置移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动标志移动火箭并不超过屏幕边缘'''
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
            self.rect.y = self.y
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
            self.rect.y = self.y

    def blitme(self):
        '''绘制火箭'''
        self.screen.blit(self.image, self.rect)