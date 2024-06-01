import pygame
import sys
from const import *

# Step 2
from game import Game


# Game variables


class Main:
    def __init__(self):
        # print("Hi from init")4
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess&AI')
        self.game_paused = False
        self.font = pygame.font.SysFont("arialblack", 40)
        self.text_color = (0, 0, 0)

        # step 2
        self.game = Game()

    def _draw_text(self, text, x, y):
        img = self.font.render(text, True, self.text_color)
        self.screen.blit(img, (x, y))

    def mainloop(self):
        # print("Hi from mainloop")
        screen = self.screen
        game = self.game
        while True:
            # step 2
            game.show_bg(screen)
            game.show_pieces(screen)

            # Pause_Menu
            if self.game_paused == True:
                self._draw_text("Main Menu", 280, 300)
            # step 1
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_paused = not self.game_paused
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


main = Main()
main.mainloop()
