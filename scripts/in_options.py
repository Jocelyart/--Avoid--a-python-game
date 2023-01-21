import pygame, sys

from screen_setup import *
from colors import color
from sound import Sound

class InOptions:

    def __init__(self, camera, game_path):
        self.assets(camera)
        self.game_path = game_path

    def assets(self, camera):

        self.main_display = pygame.display.get_surface()

        self.clock = pygame.time.Clock()

        self.camera = camera

        self.sound = Sound()
        
        # IN OPTIONS =========================================================================
    
        # options image
        self.option_img = pygame.image.load("sprites/gui/options_img.png").convert_alpha()
        self.option_img_rect = self.option_img.get_rect(topleft = (0, 0))

        # on_text
        self.on_text = pygame.image.load("sprites/gui/on_text.png").convert_alpha()
        self.on_text_rect = self.on_text.get_rect(topleft = (110, 57))
        self.show_on_text = "show"

        # off_text
        self.off_text = pygame.image.load("sprites/gui/off_text.png").convert_alpha()
        self.off_text_rect = self.off_text.get_rect(topleft = (110, 57))
        self.show_off_text = "show"

        # selector
        self.selector_options = pygame.image.load("sprites/gui/selector.png").convert_alpha()
        self.selector_options_rect = self.selector_options.get_rect(topleft = (20, 40))

        self.music_on_off_state = 0
        self.sfx_on_off_state = 0
        

        self.is_pressing_p_options = False
        self.is_pressing_up_options = False
        self.is_pressing_down_options = False

        self.selector_sound_timer_options = 10
        self.valid_sound_timer_options = 10

        self.stop_sound = "no"

        self.active_input_delay = "yes"
        self.input_delay = 10

        self.select_key = 0
        self.key_up_controls = [pygame.K_z, pygame.K_w]


 

    def handle_inputs(self, dt):
      
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

        if key[pygame.K_p] and self.is_pressing_p_options == False:

            self.is_pressing_p_options = True

            if self.stop_sound == "no":
                self.sound.play("valid_sound")

            if self.selector_options_rect.y == 40 and self.input_delay < 9:
                self.game_path.go_to_options = False
                self.game_path.go_to_credits = False
                self.game_path.go_to_how_to_play = True
                # how to play


            if self.selector_options_rect.y == 60:
                self.music_on_off_state += 1

                if self.music_on_off_state > 1:
                    self.music_on_off_state = 0
                # music
                

            if self.selector_options_rect.y == 80:
                self.sfx_on_off_state += 1

                if self.sfx_on_off_state > 1:
                    self.sfx_on_off_state = 0
                # sfx


            if self.selector_options_rect.y == 100:
                self.game_path.go_to_options = False
                self.game_path.go_to_how_to_play = False
                self.game_path.go_to_credits = True
                # credits

            if self.selector_options_rect.y == 120:
                self.game_path.go_to_options = False
                self.game_path.go_to_how_to_play = False
                self.game_path.go_to_credits = False

                self.game_path.go_to_menu = True
                # exit
        else:
            if not key[pygame.K_p] and self.is_pressing_p_options == True:
                self.is_pressing_p_options = False

        # UP KEY
        if key[self.key_up_controls[self.select_key]] and self.is_pressing_up_options == False :
            self.is_pressing_up_options = True
            
            self.selector_options_rect.y -= 20

            if self.stop_sound == "no":
                self.sound.play("selector_sound")

        if not key[self.key_up_controls[self.select_key]] and self.is_pressing_up_options == True:
            self.is_pressing_up_options = False
            self.sound.stop("selector_sound")
        
        # ====================================================

        # DOWN KEY
        if key[pygame.K_s] and self.is_pressing_down_options == False :
            self.is_pressing_down_options = True

            self.selector_options_rect.y += 20

            if self.stop_sound == "no":
                self.sound.play("selector_sound")
        
        if not key[pygame.K_s] and self.is_pressing_down_options == True:
            self.is_pressing_down_options = False
            self.sound.stop("selector_sound")
        
    def draw(self):

        # option image
        self.camera.display_surface.blit(self.option_img, self.option_img_rect)

        # selector
        self.camera.display_surface.blit(self.selector_options, self.selector_options_rect)

        # on text
        for on_index in range(2):

            if on_index == 0:
                if self.music_on_off_state == 0: # play musics
                    x = self.on_text_rect.x
                    y = self.on_text_rect.y - 2
                    self.show_on_text = "show"
        
                    
                else:
                    self.show_on_text = "hide"

            if on_index == 1:
                if self.sfx_on_off_state == 0: # play sounds
                    x = self.on_text_rect.x
                    y = self.on_text_rect.y + 18
                    self.show_on_text = "show"
                    self.stop_sound = "no"

                else:
                    self.show_on_text = "hide"

            if self.show_on_text == "show":
                self.camera.display_surface.blit(self.on_text, (x, y))
            
            else:
                self.show_on_text = "hide"
                
            

        # off text
        for off_index in range(2):

            if off_index == 0:
                if self.music_on_off_state == 1: # stop musics
                    x = self.off_text_rect.x + 1
                    y = self.off_text_rect.y - 2
                    self.show_off_text = "show"
                    
                
                else:
                    self.show_off_text = "hide"
                    
            if off_index == 1:
                if self.sfx_on_off_state == 1: # stop sounds
                    x = self.off_text_rect.x + 1
                    y = self.off_text_rect.y + 18
                    self.show_off_text = "show"
                    self.stop_sound = "yes"
                
                else:
                    self.show_off_text = "hide"

            if self.show_off_text == "show":
                self.camera.display_surface.blit(self.off_text, (x, y))
            else:
                self.show_off_text = "hide"
            


    def update(self, dt):

        self.handle_inputs(dt)
            
        if self.game_path.go_to_options == False:
            self.selector_options_rect.y = 40
            self.active_input_delay = "yes"
            self.input_delay = 10

        # selector
        if self.selector_options_rect.y < 40:
            self.selector_options_rect.y = 120
        
        if self.selector_options_rect.y > 120:
            self.selector_options_rect.y = 40