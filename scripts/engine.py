import pygame, sys

from screen_setup import *
from font_custom import *
from game import Game

# INITIALIZATION THE MIXER
pygame.mixer.pre_init(44100, -16, 2, 512)

# INITIALIZATION THE ENGINE
pygame.init()

# Add more sound channel - set up how much sounds can be played at once
pygame.mixer.set_num_channels(32)

class Engine():

    def __init__(self):


        self.main_display = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE | pygame.SCALED)

        # self.main_display = pygame.display.set_mode((screen_width, screen_height), pygame.OPENGL)
        
        self.clock = pygame.time.Clock()

        self.run = True

        self.game = Game(self)

        self.icon_img = pygame.image.load("sprites/icon.png").convert_alpha()
        pygame.display.set_icon(self.icon_img)
      
    
    def start(self):

        # RUN THE ENGINE
        while self.run:

            # SHOW FPS
            pygame.display.set_caption(f"{game_title}")

            # DELTA TIME    
            dt = self.clock.tick(FPS) / 1000


            for event in pygame.event.get():
                # # Quit event
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    sys.exit()
                
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
                        pygame.quit()
                        sys.exit()
                    
                    if event.key == FULLSCREEN_KEY:
                        self.main_display = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN | pygame.SCALED)

                    if event.key == pygame.K_p:

                        # force reload in game screen 1
                        if self.game.camera.game_path.go_to_game == True and self.game.camera.game_path.in_game.game_screen_counter == 1:
                            self.game.camera.game_path.force_reload_timer = 5

                        # reload music if player presses restart
                        if self.game.camera.game_path.go_to_game == True and self.game.camera.game_path.in_game.pause_counter == 2 and self.game.camera.game_path.in_game.selector_pause_menu_rect.y == 22:
                            self.game.camera.game_path.delay_timer_music = 10
                            self.game.camera.game_path.force_reload_timer = 5
                            self.game.camera.game_path.start_value_track = 0.0
                            self.game.camera.game_path.check_playtime_value = "yes"

                        # reload music if player presses main menu
                        if self.game.camera.game_path.go_to_game == True and self.game.camera.game_path.in_game.pause_counter == 2 and self.game.camera.game_path.in_game.selector_pause_menu_rect.y == 37:
                            self.game.camera.game_path.delay_timer_music = 10
                            self.game.camera.game_path.start_value_track = 0.0
                            

            # fill screen
            self.main_display.fill(("black"))

            # DRAW
            self.game.draw()
    
            # UPDATE
            self.game.update(dt)

            pygame.display.update()
            
