import pygame, sys


from screen_setup import *
from colors import color
from font_custom import*

from sound import Sound

class InMenu:

    def __init__(self, camera, game_path):

        self.menu_assets(camera)

        self.game_path = game_path

    def menu_assets(self, camera):

        self.main_display = pygame.display.get_surface()

        self.clock = pygame.time.Clock()

        self.camera = camera

        self.sound = Sound()
        # IN MENU ============================================================================
        
        self.gameboy_image = pygame.image.load("sprites/gameboy_img.png").convert_alpha()

        # avoid text
        self.avoid_text_menu = pygame.image.load("sprites/gui/avoid_text.png").convert_alpha()
        self.avoid_text_menu_rect = self.avoid_text_menu.get_rect(topleft = (0, 16))

        # start text
        self.start_text = pygame.image.load("sprites/gui/start_text.png").convert_alpha()
        self.start_text_rect = self.start_text.get_rect(topleft = (50, 70))

        # options text
        self.options_text = pygame.image.load("sprites/gui/options_text.png").convert_alpha()
        self.options_text_rect = self.options_text.get_rect(topleft = (50, 90))

        # quit text
        self.quit_text = pygame.image.load("sprites/gui/quit.png").convert_alpha()
        self.quit_text_rect = self.quit_text.get_rect(topleft = (50, 110))

        # selector
        # if self.run_menu == True:
        self.selector_menu = pygame.image.load("sprites/gui/selector.png").convert_alpha()
        self.selector_menu_rect = self.selector_menu.get_rect(topleft = (30, 70))


        self.is_pressing_p = False
        self.is_pressing_up = False
        self.is_pressing_down = False


        self.selector_sound_timer_menu = 10
        self.valid_sound_timer_menu = 10

        self.active_input_delay = "yes"
        self.input_delay = 10

        self.select_key = 0
        self.key_up_controls = [pygame.K_z, pygame.K_w]
        

 

    def handle_input(self, dt):
        # sound timer
        if self.selector_sound_timer_menu > 0:
            self.selector_sound_timer_menu -= 1

        if self.valid_sound_timer_menu > 0:
            self.valid_sound_timer_menu -= 1
        

        key = pygame.key.get_pressed()

        # GET THE AZERTY OR QWERTY CONTROLS
        if self.game_path.in_setup_controls.azerty_controls == True:
            self.select_key = 0
            
        else:
            if self.game_path.in_setup_controls.qwerty_controls == True:
                self.select_key = 1

        if self.active_input_delay == "yes":
            if self.input_delay > 0:
                self.input_delay -= 5 * dt

                if self.input_delay < 9:
                    self.input_delay = 8
                    self.active_input_delay = "no"

        # P KEY 
        if key[pygame.K_p] and self.is_pressing_p == False:
            self.is_pressing_p = True

            if self.valid_sound_timer_menu == 0:
                self.valid_sound_timer_menu = 10
                if self.camera.game_path.in_options.stop_sound == "no":
                    self.sound.play("valid_sound")
            
            # in game
            if self.selector_menu_rect.y == 70 and self.input_delay < 9:
                
                # in_menu
                self.game_path.go_to_menu = False
                # in options
                self.game_path.go_to_options = False
                # in how to play
                self.game_path.go_to_how_to_play = False
                # in credits
                self.game_path.go_to_credits = False
                # in game
                self.game_path.go_to_game = True

          
            
            # in options
            if self.selector_menu_rect.y == 90:

                # in menu
                self.game_path.go_to_menu = False
                # in game
                self.game_path.go_to_game = False
                # in how to play
                self.game_path.go_to_how_to_play = False
                # in credits
                self.game_path.go_to_credits = False

                # in options
                self.game_path.go_to_options = True


            # quit
            if self.selector_menu_rect.y == 110:
                self.camera.game.engine.run = False
            


        if not key[pygame.K_p] and self.is_pressing_p == True:
            self.is_pressing_p = False
            self.sound.stop("valid_sound")

        # ====================================================

        # UP KEY
        if key[self.key_up_controls[self.select_key]] and self.is_pressing_up == False:
            self.is_pressing_up = True
            
            self.selector_menu_rect.y -= 20

            if self.is_pressing_up == True:
                if self.selector_sound_timer_menu == 0:
                    self.selector_sound_timer_menu = 10
                    if self.camera.game_path.in_options.stop_sound == "no":
                        self.sound.play("selector_sound")

        if not key[self.key_up_controls[self.select_key]] and self.is_pressing_up == True:
            self.is_pressing_up = False
            self.sound.stop("selector_sound")
        
        # ====================================================

        # DOWN KEY
        if key[pygame.K_s] and self.is_pressing_down == False:
            self.is_pressing_down = True

            self.selector_menu_rect.y += 20

            if self.is_pressing_down == True:
                if self.selector_sound_timer_menu == 0:
                    self.selector_sound_timer_menu = 10
                    if self.camera.game_path.in_options.stop_sound == "no":
                        self.sound.play("selector_sound")
        
        if not key[pygame.K_s] and self.is_pressing_down == True:
            self.is_pressing_down = False
            self.sound.stop("selector_sound")
    
            
    def draw(self):

        # avoid text
        self.camera.display_surface.blit(self.avoid_text_menu, self.avoid_text_menu_rect)

        # start text
        self.camera.display_surface.blit(self.start_text, self.start_text_rect)

        # options text
        self.camera.display_surface.blit(self.options_text, self.options_text_rect)

        # quit text
        self.camera.display_surface.blit(self.quit_text, self.quit_text_rect)

        # selector sprite
        self.camera.display_surface.blit(self.selector_menu, (self.selector_menu_rect.x, self.selector_menu_rect.y))
        

        
    def update(self, dt):
            
        self.handle_input(dt)
        
        if self.game_path.go_to_menu == False: # reset selector
            self.selector_menu_rect.y = 70
            self.active_input_delay = "yes"
            self.input_delay = 10


        if self.selector_menu_rect.y < 70:
            self.selector_menu_rect.y = 110
        
        if self.selector_menu_rect.y > 110:
            self.selector_menu_rect.y = 70
    
        
    