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
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideway Shooter")
        self.rocket = Rocket(self)
        
    def run_game(self):
        '''游戏主循环'''
        while True:
            self._check_events()
            self.screen.fill(self.settings.bg_color)
            self.rocket.blitme()
            pygame.display.flip()
            self.clock.tick(60)
    
    def _check_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ss = SidewayShooter()
    ss.run_game()