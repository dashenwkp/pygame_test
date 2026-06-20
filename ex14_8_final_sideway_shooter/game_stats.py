class GameStats:
    '''游戏运行时的统计数据'''

    def __init__(self, ss_game):
        '''初始化统计信息'''
        self.settings = ss_game.settings
        self.reset_stats()

    def reset_stats(self):
        '''重置统计信息'''
        self.rockets_left = self.settings.rocket_limit
        self.aliens_hit = 0
        self.level = 1
        self.score = 0