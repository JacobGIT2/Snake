# 3 kind of square
# initially 7 square long snake
# generate method(method)
import pygame

class Snake:
    def __init__(self, ga_ins):
        '''initialize a square without color setting'''
        self.screen = ga_ins.screen
        self.screen_rect = ga_ins.screen_rect
        self.settings = ga_ins.settings
        self.rect = pygame.rect.Rect((0, 0), self.settings.snake_size)
        self.x, self.y = self.rect.x, self.rect.y
        self.move_sign = ga_ins.move_sign

    def update(self, ga_ins):
        '''a help method only used in initialization of the snake'''
        if self.num == 0:
            self.x, self.y = self.settings.screen_rect[0]/2, self.settings.screen_rect[1]/2
            self.rect.x, self.rect.y = self.x, self.y
        else:
            self.rect.x = ga_ins.snake[self.num-1].rect.x-self.settings.snake_size[0]
            self.rect.y = ga_ins.snake[self.num-1].rect.y
        
    def draw(self):
        '''draw snake on the screen'''
        self.color = self.settings.snake_colors[1] if self.num == 0 else self.settings.snake_colors[0]
        pygame.draw.rect(self.screen, self.color, self.rect)
