import pygame
import sys
from settings import Settings
from snake import Snake
from candy import Candy
from random import choice

class Snake_eat():
    '''game class'''
    def __init__(self):
        '''method to design game attribute'''
        # import setting object
        self.settings = Settings()
        # screen object
        self.screen = pygame.display.set_mode(self.settings.screen_rect)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("HUNGRY SNAKE")
        # clock module
        self.time = pygame.time.Clock()
        # moving sign
        self.move_sign = 'up'
        # assign snake group
        self.snake = []
        self._snake_init()
        # a value represent snake has eaten the candy
        self.eaten = False 
        # assign candy group
        self.candies = pygame.sprite.Group()
        # score
        self.score = 0
        
    def _snake_init(self):
        '''help method to generate initial snake'''
        while len(self.snake) < self.settings.snake_length:
            new_snake = Snake(self)
            new_snake.num = len(self.snake)
            new_snake.update(self)
            self.snake.append(new_snake)

    
    def _move_snake(self):
        '''help method to move snake'''
        self._del_tail()
        self._add_head()
        self._border_check()
        self._self_eat_check()

    def _del_tail(self):
        '''sub method of move snake: to delete the tail'''
        self.new_head = self.snake.pop()
        for element in self.snake:
            element.num += 1

    def _add_head(self):
        '''sub method of move snake: to add the head'''
        self.new_head.num = 0
        if self.move_sign == 'up':
            self.new_head.rect.x = self.snake[0].rect.x
            self.new_head.rect.y = self.snake[0].rect.y - self.settings.snake_size[0]
        if self.move_sign == 'down':
            self.new_head.rect.x = self.snake[0].rect.x
            self.new_head.rect.y = self.snake[0].rect.y + self.settings.snake_size[0]
        if self.move_sign == 'left':
            self.new_head.rect.x = self.snake[0].rect.x - self.settings.snake_size[0]
            self.new_head.rect.y = self.snake[0].rect.y
        if self.move_sign == 'right':
            self.new_head.rect.x = self.snake[0].rect.x + self.settings.snake_size[0]
            self.new_head.rect.y = self.snake[0].rect.y
        self.snake.insert(0, self.new_head)

    def _border_check(self):
        '''help method to move snake to the other side when it hits the border'''
        for element in self.snake:
            if element.rect.x == -self.settings.snake_size[0]:
                element.rect.x = self.settings.screen_rect[0] - self.settings.snake_size[0]
            elif element.rect.x == self.settings.screen_rect[0]:
                element.rect.x = 0
            if element.rect.y == -5-self.settings.snake_size[1]:
                element.rect.y = self.settings.screen_rect[1] - self.settings.snake_size[1] + 5
            if element.rect.y == self.settings.screen_rect[1]+5:
                element.rect.y = -5
            
    def _self_eat_check(self):
        '''help method to stop game when snake eat itself'''
        for i in range(len(self.snake)):
            temp = self.snake[:]
            test = temp.pop(i)
            if any(test.rect.x == item.rect.x and test.rect.y == item.rect.y for item in temp):
                sys.exit()

    def _make_candy(self):
        '''help method to maintain certain amount of candy'''
        while len(self.candies) < self.settings.candy_num:
            new_candy = Candy(self)
            self.candies.add(new_candy)


    def run_game(self):
        '''method to run game with main loop'''
        while True:
            self.screen.fill(self.settings.screen_color)
            self._check_events()
            self._move_snake()
            self._eat_candy()
            self._make_candy()
            self._update_screen()
            pygame.display.set_caption("HUNGRY SNAKE"+" "*10+f"Your score: {self.score}")
            pygame.display.flip()
            self.time.tick(self.settings.speed)

    def _update_screen(self):
        '''help method to gather operations on snake'''
        for num in range(len(self.snake), 0, -1):
            self.snake[num-1].draw()
        for candy in self.candies:
            candy.draw()
        

    def _eat_candy(self):
        '''help method to handle candy eaten event'''
        temp = self._check_eat_valid()
        if temp:
            self.candies.remove(temp)
            self._add_tail()
    
    def _check_eat_valid(self):
        '''sub method of _eat_candy; take in a move sign; return the touched candy if there is any'''
        for element in self.candies:
            x, y = self.snake[0].rect.x, self.snake[0].rect.y
            xmin, xmax, ymin, ymax = element.rect.x, element.rect.x+self.settings.candy_size[0], element.rect.y, element.rect.y+self.settings.candy_size[1]
            if ((2*xmin < 2*x+self.settings.snake_size[0] < 2*xmax) and (2*ymin < (2*y+self.settings.snake_size[1]) < 2*ymax)):
                self.score += 1
                self.speed_up()
                return element 
            continue
        return False

    def speed_up(self):
        '''sub method of _check_eat_valid; to accelerate game speed'''
        if self.settings.speed <= 30:
            self.settings.speed += 1
        # print(self.settings.speed)

    def _add_tail(self):
        '''sub method of _check_eat_valid; to add a tail'''
        new_tail = Snake(self)
        new_tail.num = len(self.snake)
        self.snake.append(new_tail)


    def _change_head_valid(self, position):
        '''to check whether the snake's neck is on target position'''
        if position == 'up' and self.snake[1].rect.y < self.snake[0].rect.y:
            return False
        elif position == 'down' and self.snake[1].rect.y > self.snake[0].rect.y:
            return False
        elif position == 'left' and self.snake[1].rect.x < self.snake[0].rect.x:
            return False
        elif position == 'right' and self.snake[1].rect.x > self.snake[0].rect.x:
            return False
        return True
            


    def _check_events(self):
        '''help method to handle event type'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''help method to handle keydown event key'''
        if event.key == pygame.K_UP and self._change_head_valid('up'):
            self.move_sign = 'up'
        if event.key == pygame.K_DOWN and self._change_head_valid('down'):
            self.move_sign = 'down'
        if event.key == pygame.K_LEFT and self._change_head_valid('left'):
            self.move_sign = 'left'
        if event.key == pygame.K_RIGHT and self._change_head_valid('right'):
            self.move_sign = 'right'

    def _check_keyup_events(self, event):
        '''help method to handle key up event key'''
        if event.key == pygame.K_w:
            pass
        if event.key == pygame.K_s:
            pass
        if event.key == pygame.K_a:
            pass
        if event.key == pygame.K_d:
            pass

if __name__ == '__main__':
    rungame = Snake_eat()
    rungame.run_game()