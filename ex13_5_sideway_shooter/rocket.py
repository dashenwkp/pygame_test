import pygame

class Rocket:
    '''表示飞船的类'''

    def __init__(self, ss_game):
        '''初始化飞船并设置其初始位置'''
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(
            r'ex13_5_sideway_shooter\images\rocket_small.png')
        self.rect = self.image.get_rect()
        self.screen_rect = ss_game.screen.get_rect()

        # 将每艘新飞船放在屏幕左边中央
        self.rect.midleft = self.screen_rect.midleft

        # 在飞船的属性y中存储小数值
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动标志调整飞船的位置'''
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # 根据self.y更新rect对象
        self.rect.y = self.y

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)