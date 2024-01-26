class Settings:
    '''basic class for snake_eat setting'''
    def __init__(self):
        '''set attribute'''
        # set screen attribute
        self.screen_rect = (1200, 800)
        self.screen_color = (230, 230, 230)
        # set snake attribute
        self.snake_size = (15,15)
        self.snake_colors = [(70, 70, 70), (230, 0, 0)]
        self.snake_length = 7
        # set speed
        self.speed = 10
        # set candy attribute
        self.candy_num = 2
        self.candy_size = (15, 15)
        self.candy_color = (0, 100, 0)

