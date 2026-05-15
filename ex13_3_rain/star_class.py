from pygame.sprite import Sprite
import pygame
class Star(Sprite):
    '''星星类'''

    def __init__(self, st_game):
        super().__init__()
        '''初始化星星, 并将其rect坐标设为左上角'''
        self.image = pygame.image.load(r'ex13_3_rain\images\raindrop.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.settings = st_game.settings

        # 存储水平位置的精确坐标
        self.y = float(self.rect.y)

    def update(self):
        '''增大雨滴的y坐标'''
        self.y += self.settings.rain_speed
        self.rect.y = self.y