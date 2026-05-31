import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理所有子弹的类'''

    def __init__(self, tp_game):
        '''创建子弹并设置正确的位置'''
        super().__init__()
        self.settings = tp_game.settings
        self.screen = tp_game.screen
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = tp_game.ship.rect.midright

        # 存储精确的x坐标
        self.x = float(self.rect.x)

    def update(self):
        '''更新子弹的位置'''
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        '''绘制子弹'''
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)