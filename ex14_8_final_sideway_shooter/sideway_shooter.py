import pygame
import sys
from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien
from random import random
from time import sleep
from game_stats import GameStats
from button import Button

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
        self.stats = GameStats(self)
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

        # 表示游戏运行的值
        self.game_active = False

        self.play_button = Button(self, 'Play')

    def run_game(self):
        '''游戏主循环'''
        while True:
            self._check_event()
            if self.game_active:
                self._create_alien()
                self.rocket.update()
                self._update_bullet()
                self._update_aliens()
            self._update_screen()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        '''单击play按钮时开始新游戏'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        '''开始新游戏'''
        # 重置游戏的统计信息
        self.stats.reset_stats()
        self.game_active = True

        # 删除子弹和外星人
        self.bullets.empty()
        self.aliens.empty()

        # 使飞船居中
        self.rocket.rocket_center()

        # 隐藏光标
        pygame.mouse.set_visible(False)

    def _check_key_down(self, event):
        '''监测键盘按下'''
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_key_up(self, event):
        '''监测键盘松开'''
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _fire_bullet(self):
        '''在不超过限制的情况下, 创建一颗子弹, 并将其加入编组中'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        '''更新子弹的位置, 并删除飞出屏幕外面的子弹'''
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _update_aliens(self):
        '''更新外星人的位置'''
        self.aliens.update()

        # 检测外星人和火箭的碰撞
        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self._rocket_hit()

        # 检测外星人是否到达屏幕左边缘
        self._aliens_bottom()

    def _rocket_hit(self):
        '''火箭被撞后'''
        if self.stats.rockets_left > 0:
            self.stats.rockets_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            sleep(0.5)
            self._create_alien()
            self.rocket.rocket_center()
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _aliens_bottom(self):
        '''检测外星人是否到达屏幕左边缘'''
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                self._rocket_hit()
                break

    def _check_bullet_alien_collisions(self):
        '''检测子弹和外星人的碰撞'''
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _create_alien(self):
        '''满足条件时创建外星人实例, 并加入到编组中'''
        if random() < self.settings.alien_frequency:
            new_alien = Alien(self)
            self.aliens.add(new_alien)

    def _update_screen(self):
        '''更新屏幕'''
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        # 绘制每一颗子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 绘制外星人
        self.aliens.draw(self.screen)

        # 如果游戏处于非活动状态，就绘制play按钮
        if not self.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()

if __name__ == '__main__':
    ss_game = SidewayShooter()
    ss_game.run_game()