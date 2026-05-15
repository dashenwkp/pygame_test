from pygame.sprite import Sprite
import pygame
class Star(Sprite):
    '''星星类'''

    def __init__(self, st_game):
        super().__init__()
        '''初始化星星, 并将其rect坐标设为左上角'''
        self.image = pygame.image.load(r'ex13_4_permanent_rain\images\raindrop.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.settings = st_game.settings
        self.screen = st_game.screen

        # 存储竖直位置的精确坐标
        self.y = float(self.rect.y)

    def check_edge(self):
        '''雨滴碰到屏幕下边缘时, 返回True'''
        screen_rect = self.screen.get_rect()
        return self.rect.top >= screen_rect.bottom

    def update(self):
        '''增大雨滴的y坐标'''
        self.y += self.settings.rain_speed
        self.rect.y = self.y