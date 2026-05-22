import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    '''管理外星人的类'''

    def __init__(self, ss_game):
        '''加载图像, 并设置外星人的初始位置'''
        super().__init__()
        self.image = pygame.image.load(
            r'ex13_5_test_onmyown\images\alien_ship.png')
        self.rect = self.image.get_rect()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # 外星人初始刷新在屏幕右侧看不到的地方, y坐标随机但top的最大值等于外星人的高度
        self.rect.left = self.screen.get_rect().right
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.y = randint(0, alien_top_max)

        # 存储精确的x坐标
        self.x = float(self.rect.x)

    def update(self):
        '''更新外星人的x坐标'''
        self.x -= self.settings.alien_speed
        self.rect.x = self.x