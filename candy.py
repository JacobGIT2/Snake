import pygame
from pygame.sprite import Sprite
from random import choice

def _choices(dirc, setting):
        '''help method to return a list of possible position with setting'''
        up_limit = setting.screen_rect[0] if dirc == 'x' else setting.screen_rect[1]
        low_limit = setting.screen_rect[0]/2 if dirc == 'x' else setting.screen_rect[1]/2
        step = setting.candy_size[0] if dirc == 'x' else setting.candy_size[1]
        return_list = []
        while low_limit > 0:
            low_limit -= step
        low_limit += step
        while low_limit < up_limit - step:
            return_list.append(low_limit)
            low_limit += step
        return return_list

def _init_random(dirc, setting, ga_ins):
    '''help method to return a target random position without for candy 
    without overlapping with snake'''
    while True:
        if dirc == 'x':
            temp = choice(_choices(dirc, setting))
            if all(temp!=item.rect.x for item in ga_ins.snake):
                return temp
        elif dirc == 'y':
            temp = choice(_choices(dirc, setting))
            if all(temp!=item.rect.y for item in ga_ins.snake):
                return temp

class Candy(Sprite):
    '''a candy class involve draw method and delete method'''
    def __init__(self, ga_ins):
        super().__init__()
        '''screen, screen_rect, setting, rect, color, size'''
        self.game = ga_ins
        self.screen = ga_ins.screen
        self.screen_rect = ga_ins.screen_rect
        self.settings = ga_ins.settings
        self.size = self.settings.candy_size
        self.color = self.settings.candy_color
        self.x = _init_random('x', self.settings, self.game)
        self.y = _init_random('y', self.settings, self.game)
        self.rect = pygame.rect.Rect((self.x, self.y), self.size)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    # def _choices(self, dirc, setting):
    #     '''help method to return a list of possible position with setting'''
    #     up_limit = setting.screen_rect[0] if dirc == 'x' else setting.screen_rect[1]
    #     low_limit = setting.screen_rect[0]/2 if dirc == 'x' else setting.screen_rect[1]/2
    #     step = setting.candy_size[0] if dirc == 'x' else setting.candy_size[1]
    #     return_list = []
    #     while low_limit > 0:
    #         low_limit -= step
    #     low_limit += step
    #     while low_limit < up_limit - step:
    #         return_list.append(low_limit)
    #         low_limit += step
    #     return return_list

    # def _init_random(self, dirc, setting):
    #     '''help method to return a target random position without for candy 
    #     without overlapping with snake'''
    #     while True:
    #         if dirc == 'x':
    #             temp = choice(self._choices(dirc, setting))
    #             if all(temp!=item.rect.x for item in self.game.snake):
    #                 return temp
    #         elif dirc == 'y':
    #             temp = choice(self._choices(dirc, setting))
    #             if all(temp!=item.rect.y for item in self.game.snake):
    #                 return temp




