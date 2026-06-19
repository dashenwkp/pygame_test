import pygame.font

class Button:
    '''管理按钮的类'''

    def __init__(self, ss_game, msg):
        '''初始化按钮'''
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮和文字的一些属性
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(r'C:\Windows\Fonts\arial.ttf', 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''渲染文字，并放到按钮的中间'''
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''绘制按钮和文字'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)