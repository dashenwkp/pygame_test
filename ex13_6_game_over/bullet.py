import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理子弹的类'''

    def __init__(self, ss_game):
        super().__init__()
        '''初始化子弹并设置子弹的位置'''
        self.settings = ss_game.settings
        self.screen = ss_game.screen
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ss_game.rocket.rect.midright

        # 存储精确的x坐标
        self.x = float(self.rect.x)

    def update(self):
        '''更新子弹的位置'''
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        '''绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)