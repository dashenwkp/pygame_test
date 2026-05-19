import pygame
import sys
from settings import Settings
from rocket import Rocket
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        '''游戏主循环'''
        while True:
            self._check_events()
            self.update_screen()
            self.rocket.update()
            self._update_bullets()
            self.clock.tick(60)
    
    def _check_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''响应按键'''
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        '''响应松开'''
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def update_screen(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        # 遍历编组中的每颗子弹，并绘制它们
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

    def _fire_bullet(self):
        '''如果还没有达到限制，就发射一颗子弹'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''更新子弹的位置，并删除已消失的子弹'''
        self.bullets.update()

        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ss = SidewayShooter()
    ss.run_game()