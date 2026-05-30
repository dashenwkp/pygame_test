import pygame
from settings import Settings
from pygame.time import Clock
import sys
from ship import Ship

class TargetPractice:
    '''游戏《射击练习》的总类'''

    def __init__(self):
        '''初始化游戏，创建游戏资源'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Target Pratice')

        self.ship = Ship(self)

        self.clock = Clock()

    def run_game(self):
        '''游戏主循环'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        '''检测事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

    def _check_key_down(self, event):
        '''检测按键按下'''
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _check_key_up(self, event):
        '''检测按键松开'''
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        '''更新屏幕'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    tp_game = TargetPractice()
    tp_game.run_game()