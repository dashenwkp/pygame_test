import pygame
import sys
from settings import Settings
from star_class import Star

class Stars:
    '''星星类'''

    def __init__(self):
        '''初始化'''
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('Beautiful Stars')

        self.clock = pygame.time.Clock()
        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        '''游戏主循环'''
        while True:
            self.screen.fill(self.settings.bg_color)
            self._update_rains()
            self.stars.draw(self.screen)
            pygame.display.flip()          
            self._check_events()
            self.clock.tick(60)

    def _check_events(self):
        '''监测事件'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _create_stars(self):
        '''创建所有星星, 其实就是在这里的循环中不断改变星星坐标'''
        star = Star(self) # 这颗星星不会被绘制，因为它没有被加入到编组中
        star_width = star.rect.width
        star_height = star.rect.height
        current_x = star_width
        current_y = star_height
        while current_y < self.settings.screen_height:
            while current_x < (self.settings.screen_width - 2 * star_width):
                # 现在创建的星星才会被绘制
                self._create_single_star(current_x, current_y)
                current_x += 2 * star_width
            current_x = star_width
            current_y += 2 * star_height

    def _create_single_star(self, x_position, y_position):
        '''在这里改变每一个星星的坐标'''
        new_star = Star(self)
        new_star.y = y_position
        new_star.rect.y = new_star.y
        new_star.rect.x = x_position
        self.stars.add(new_star)

    def _update_rains(self):
        '''更新雨滴的坐标'''
        self.stars.update()

if __name__ == '__main__':
    st_game = Stars()
    st_game.run_game()