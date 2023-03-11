import sys
from random import randint
import pygame

INIT_DIRECTION = 'right'


class Vector2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake(object):
    def __init__(self, head_xy, body):
        self.head = head_xy
        self.body = body

    def draw_snake(self, head_img, color, screen, blocksize):
        for part in self.body[:-1]:
            pygame.draw.rect(screen, color,
                             [part.x * blocksize, part.y * blocksize,
                              blocksize - 1, blocksize - 1])
        screen.blit(head_img, (self.head.x * blocksize, self.head.y * blocksize))


class Gameplay(object):
    def __init__(self, max_step, block_size, game_over=False):
        self.score = 0
        self.level = 0
        self.max_step = max_step
        self.block_size = block_size
        self.game_over = game_over
        head_pos = Vector2(self.max_step[0] // 2, self.max_step[1] // 2)
        self.slither = Snake(head_pos, [head_pos])

        self.velocity = Vector2(1, 0)
        self.direction = INIT_DIRECTION

        self.apple = Vector2(randint(0, self.max_step[0] - 1),
                             randint(0, self.max_step[1] - 1))

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.direction != "right":
                    self.direction = "left"
                    self.velocity = Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT and self.direction != "left":
                    self.direction = "right"
                    self.velocity = Vector2(1, 0)
                elif event.key == pygame.K_UP and self.direction != "down":
                    self.direction = "up"
                    self.velocity = Vector2(0, -1)
                elif event.key == pygame.K_DOWN and self.direction != "up":
                    self.direction = "down"
                    self.velocity = Vector2(0, 1)
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit('you exited the game')

        if self.slither.head.x == self.max_step[0] - 1 and self.direction == "right":
            self.slither.head.x = - 1
        elif self.slither.head.x == 0 and self.direction == "left":
            self.slither.head.x = self.max_step[0]
        elif self.slither.head.y == self.max_step[1] - 1 and self.direction == "down":
            self.slither.head.y = - 1
        elif self.slither.head.y == 0 and self.direction == "up":
            self.slither.head.y = self.max_step[1]

        self.slither.head = Vector2(self.slither.head.x + self.velocity.x,
                                    self.slither.head.y + self.velocity.y)

        self.slither.body.append(Vector2(self.slither.head.x, self.slither.head.y))

        if (self.slither.head.x, self.slither.head.y) \
                == (self.apple.x, self.apple.y):
            self.apple = Vector2(randint(0, self.max_step[0] - 1),
                                 randint(0, self.max_step[1] - 1))

            self.slither.body.insert(0, self.slither.body[0])
            self.score += 1
            if self.score % 10 == 0:
                self.level += 1

        if len(self.slither.body) > 1:
            self.slither.body = self.slither.body[1:]

        for part in self.slither.body[:-1]:
            if (self.slither.head.x, self.slither.head.y) == (part.x, part.y):
                self.game_over = True
                print('Gmae over')

    def draw(self, snake_head, snake_color, apple_img, screen):
        if self.direction == 'right':
            head = pygame.transform.rotate(snake_head, 270)
        if self.direction == 'left':
            head = pygame.transform.rotate(snake_head, 90)
        if self.direction == 'up':
            head = snake_head
        if self.direction == 'down':
            head = pygame.transform.rotate(snake_head, 180)
        self.slither.draw_snake(head, snake_color, screen, self.block_size)
        screen.blit(apple_img, (self.apple.x * self.block_size, self.apple.y * self.block_size))
