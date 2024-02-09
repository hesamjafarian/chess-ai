import pygame
import sys
from const import *

#Step 2
from game import Game

# Game variables

class Main:
    def __init__(self):
        #print("Hi from init")
        self.game_paused = False
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess&AI')
        #step 2
        self.game = Game()
    def _draw_pause_menu(self,):
        pass
    def mainloop(self):
        #print("Hi from mainloop")
        screen = self.screen
        game = self.game
        while True:
            #step 2
            game.show_bg(screen)
            game.show_pieces(screen)

            # Pause_Menu
            if self.game_paused == True:
                print("Space key pressed!")
            #step 1
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