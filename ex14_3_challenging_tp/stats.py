class Stats:
    '''管理游戏数据的类'''

    def __init__(self):
        '''初始化游戏运行时会变化的数据'''
        self.reset_stats()

    def reset_stats(self):
        '''重置统计数据'''
        self.miss_shooter = 0
        self.num_hits = 0 # 击中的次数