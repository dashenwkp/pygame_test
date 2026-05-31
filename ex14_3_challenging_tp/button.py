import pygame

class Button:
    '''管理按钮的类'''

    def __init__(self, tp_game, msg):
        '''创建字体和按钮'''
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (100, 5, 5)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(r'C:\Windows\Fonts\arial.ttf', 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''把文字放到按钮矩形中心'''
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)