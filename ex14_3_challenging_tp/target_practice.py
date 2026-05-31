import pygame
from settings import Settings
from pygame.time import Clock
import sys
from ship import Ship
from bullet import Bullet
from target import Target
from stats import Stats
from button import Button

class TargetPractice:
    '''游戏《射击练习》的总类'''

    def __init__(self):
        '''初始化游戏，创建游戏资源'''
        pygame.init()
        self.settings = Settings()
        self.stats = Stats()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Target Practice')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)
        self.button = Button(self, 'Play')

        self.clock = Clock()
        self.game_active = False

    def run_game(self):
        '''游戏主循环'''
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self.target.update()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, pos):
        '''检测是否点击了按钮'''
        clicked = self.button.rect.collidepoint(pos)
        if clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        '''开始新游戏'''
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.game_active = True
        self.bullets.empty()
        self.ship.center_ship()
        self.target.center_target()
        pygame.mouse.set_visible(False)

    def _check_key_down(self, event):
        '''检测按键按下'''
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_up(self, event):
        '''检测按键松开'''
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        '''发射子弹'''
        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _update_bullets(self):
        '''更新子弹，检测碰撞并删除超出屏幕的子弹，增加miss_shooter'''
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.settings.screen_width:
                self.bullets.remove(bullet)
                self._increment_miss()
        self._check_bullet_target_collison()
        
    def _check_bullet_target_collison(self):
        '''检测子弹和靶子的碰撞'''
        collision = pygame.sprite.spritecollide(
            self.target, self.bullets, True)
        if collision:
            self.stats.num_hits += 1
            if self.stats.num_hits % self.settings.levelup_hits == 0:
                self.settings.increase_difficulty()

    def _increment_miss(self):
        '''增加没击中的子弹数量'''
        self.stats.miss_shooter += 1
        if self.stats.miss_shooter >= self.settings.miss_limit:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        '''更新屏幕'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.target.draw_target()
        if not self.game_active:
            self.button.draw_button()
        pygame.display.flip()

if __name__ == '__main__':
    tp_game = TargetPractice()
    tp_game.run_game()