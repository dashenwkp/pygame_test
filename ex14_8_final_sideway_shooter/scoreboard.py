import pygame.font
from pygame.sprite import Group

from rocket import Rocket

class Scoreboard:
    '''显示得分信息的类'''

    def __init__(self, ss_game):
        '''初始化显示得分涉及的属性'''
        self.ss_game = ss_game
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ss_game.settings
        self.stats = ss_game.stats

        # 显示得分信息时使用的字体设置
        self.font = pygame.font.Font(r'C:\Windows\Fonts\arial.ttf', 48)
        self.text_color = (30, 30, 30)

        self.prep_images()

    def prep_images(self):
        '''准备剩余的火箭数量，最高分和初始得分图像'''
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_rockets()

    def prep_score(self):
        '''将得分渲染为图像'''
        rounded_score = round(self.stats.score, -1)
        score_str = f'Score: {rounded_score:,}'
        self.score_image = self.font.render(score_str, True, self.text_color)

        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''将最高分渲染为图像'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = f'High Score: {high_score:,}'
        self.high_score_imgae = self.font.render(high_score_str, True, self.text_color)

        # 在屏幕上方中间显示最高分
        self.high_score_rect = self.high_score_imgae.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        '''检查是否诞生了最高分'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        '''将等级渲染为图像'''
        level_str = str(self.stats.level)
        level = f'Level: {level_str}'
        self.level_image = self.font.render(level, True, self.text_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom - 10

    def prep_rockets(self):
        '''显示还余下多少火箭'''
        self.rockets = Group()
        for rocket_number in range(self.stats.rockets_left):
            rocket = Rocket(self.ss_game)
            rocket.rect.x = 10 + rocket.rect.width * rocket_number
            rocket.rect.y = 10
            self.rockets.add(rocket)

    def show_score(self):
        '''在屏幕上显示剩余的火箭数量，当前得分，最高分和等级'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_imgae, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.rockets.draw(self.screen)