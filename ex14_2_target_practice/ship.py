import pygame

class Ship:
    '''管理飞船的类'''

    def __init__(self, tp_game):
        '''加载飞船并设置正确的位置'''
        self.settings = tp_game.settings
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(
            r'ex14_2_target_practice\images\rocket.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        # 移动标志
        self.moving_up = False
        self.moving_down = False

        # 存储精确的y坐标
        self.y = float(self.rect.y)

    def update(self):
        '''更新飞船的位置'''
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
            self.rect.y = self.y
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            self.rect.y = self.y

    def blitme(self):
        '''绘制飞船'''
        self.screen.blit(self.image, self.rect)