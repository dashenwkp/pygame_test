class GameStats:
    '''游戏运行时的统计数据'''

    def __init__(self, ss_game):
        '''初始化统计信息'''
        self.settings = ss_game.settings

        # 在任何情况下都不应重置最高分
        self.contents = ss_game.contents
        self.high_score = int(self.contents)

        self.reset_stats()

    def reset_stats(self):
        '''重置统计信息'''
        self.rockets_left = self.settings.rocket_limit
        self.aliens_hit = 0
        self.level = 1
        self.score = 0