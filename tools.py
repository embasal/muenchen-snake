import sys
import pygame


class GAMEPLAY(object):
    def __init__(self, screen_size, colors, fonts, screen):
        self.screen_size = screen_size
        self.colors = colors
        self.fonts = fonts
        self.screen = screen

    def game_intro(self):
        intro = True
        version = None
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit('You exited the game')

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        version = 'simple'
                        intro = False
                    elif event.key == pygame.K_v:
                        version = 'slither_class'
                        intro = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit('You exited the game')

            self.screen.fill(self.colors['white'])
            self.msg2screen("Willkommen zu", self.colors['black'], -120, "large", )
            self.msg2screen("München-Snake", self.colors['black'], -70, "large", )
            self.msg2screen("Je mehr Frauenkirchen du einsammelst, desto größer wird die Schlange",
                            self.colors['black'], 10, "small")
            self.msg2screen("Wenn du dich selbst beißt hast du verloren!",
                            self.colors['black'], 50, "small")
            self.msg2screen("Drücke s um das Spiel zu starten",
                            self.colors['black'], 150, "small", )
            self.msg2screen("Drücke p um das Spiel zu pausieren oder q um es zu beenden.",
                            self.colors['black'], 180, "small")
            pygame.display.update()
        return version

    def text_obj(self, text, color, size):
        text_surf = self.fonts[size].render(text, True, color)
        return text_surf, text_surf.get_rect()

    def msg2screen(self, msg, color, y_displace, size):
        text_surf, text_rect = self.text_obj(msg, color, size)
        text_rect.center = (self.screen_size[0] / 2), (self.screen_size[1] / 2) + y_displace
        self.screen.blit(text_surf, text_rect)

    def pause(self, score):
        paused = True
        switch = True
        self.msg2screen("Pausiert", self.colors['green'], -100, "large")
        self.msg2screen("Drücke C um weiterzumachen or Q um zu verlassen.", self.colors['green'], 25,
                        "medium")
        pygame.display.update()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit('You exited the game')

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        self.game_over(score)
                        switch = False
                        paused = False
        return switch

    def game_over(self, score):
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit('You exited the game')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False

            self.screen.fill(self.colors['white'])
            self.msg2screen("Verloren", self.colors['black'], -120, "large")
            self.msg2screen(f"Du konntest nur {score} Frauenkirchen einsammeln.",
                            self.colors['red'], -30, "medium")

            self.msg2screen("Drücke q um zum Titelbild zurückzukehren",
                            self.colors['black'], 180, "small")

            pygame.display.update()

    def score_menu(self, width, score, level):
        score_text = self.text_obj("Score {0}".format(score),
                                   self.colors['black'], 'medium')
        pygame.draw.lines(self.screen, self.colors['black'], False,
                          [(0, self.screen_size[1] - width), (self.screen_size[0], self.screen_size[1] - width)], 1)
        self.screen.blit(score_text[0], (1, self.screen_size[1] - width + 1))

        level_text = self.text_obj("Level {0}".format(level),
                                   self.colors['black'], 'medium')
        self.screen.blit(level_text[0],
                         (self.screen_size[0] - level_text[1][2], self.screen_size[1] - width + 1))
