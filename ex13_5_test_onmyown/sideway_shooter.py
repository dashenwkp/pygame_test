import pygame
import sys
from settings import Settings
from rocket import Rocket

class SidewayShooter:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Sideway Shooter')
        self.rocket = Rocket(self)
        self.clock = pygame.time.Clock()

    def run_game(self):
        '''游戏主循环'''
        while True:
            self._update_screen()
            self._check_event()
            self.rocket.update()
            self.clock.tick(60)

    def _check_event(self):
        '''监测事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

    def _check_key_down(self, event):
        '''监测键盘按下'''
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_key_up(self, event):
        '''监测键盘松开'''
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        '''更新屏幕'''
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        
        pygame.display.flip()

if __name__ == '__main__':
    ss_game = SidewayShooter()
    ss_game.run_game()