from pygame.sprite import Sprite
import pygame
class Star(Sprite):
    '''星星类'''

    def __init__(self, st_game):
        super().__init__()
        '''初始化星星, 并将其rect坐标设为左上角'''
        self.image = pygame.image.load(r'ex13_1_stars\images\star.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储水平位置的精确坐标
        self.x = float(self.rect.x)