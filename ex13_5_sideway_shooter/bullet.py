import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''一个对飞船发射的子弹进行管理的类'''

    def __init__(self, ss_game):
        '''在飞船所在的位置创建一个子弹对象'''
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bullet_color

        # 在(0, 0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midright = ss_game.rocket.rect.midright

        # 存储用小数表示的子弹位置
        self.x = float(self.rect.x)

    def update(self):
        '''向右移动子弹'''
        # 更新表示子弹位置的小数值
        self.x += self.settings.bullet_speed
        # 更新表示子弹的rect位置
        self.rect.x = self.x

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)