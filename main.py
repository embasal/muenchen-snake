import sys
import pygame
import util_class
from tools import GAMEPLAY

pygame.init()

img_apple = pygame.image.load('images/kirche.bmp')
img_head = pygame.image.load('images/muenchen.bmp')

block_size = img_head.get_width()
menu_width = 2 * block_size
grid = [35, 25]
display_size = grid[0] * block_size, grid[1] * block_size + menu_width

colors = dict(white=(255, 255, 255),
              black=(0, 0, 0),
              red=(255, 0, 0),
              green=(0, 155, 0))

used_fonts = dict(small=pygame.font.SysFont("calibri", 15),
                  medium=pygame.font.SysFont("calibri", 30),
                  large=pygame.font.SysFont("calibri", 50))

level = 0
FPS = 5

screen = pygame.display.set_mode(display_size)
clock = pygame.time.Clock()

gp = GAMEPLAY(display_size, colors, used_fonts, screen)

gui = True
while gui:
    version = gp.game_intro()
    game = util_class.Gameplay(grid, block_size)
    switch = True
    while switch:
        delta_time = clock.tick(FPS + game.level)  # increases the speed as level ups
        events = pygame.event.get()
        game.update(events)
        screen.fill(colors['white'])

        gp.score_menu(menu_width, game.score, game.level)
        game.draw(img_head, colors['black'], img_apple, screen)

        for event in events:
            if event.type == pygame.QUIT:
                switch = False
                pygame.quit()
                sys.exit('you exited the game')
            elif event.type == pygame.mouse.get_focused:
                continue
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    switch = gp.pause(game.score)

        if game.game_over:
            gp.game_over(game.score)
            switch = False

        pygame.display.flip()
