import pygame, sys


from screen_setup import *
from font_custom import*

from sound import Sound


class InIntro0:

    def __init__(self, camera, game_path):
        self.intro_0_assets(camera)
        self.game_path = game_path

    def intro_0_assets(self, camera):

        self.main_display = pygame.display.get_surface()
        self.sound = Sound()
        self.camera = camera
        self.clock = pygame.time.Clock()
        

        # game stuff logo
        self.game_stuff_logo_intro_0 = pygame.image.load("sprites/gui/game_stuff_logo_text.png").convert_alpha()
        self.game_stuff_logo_intro_0_rect = self.game_stuff_logo_intro_0.get_rect(topleft = (14, -50))

        # dark green screen
        self.dark_green_screen_opacity_intro_0 = 0
        self.dark_green_screen_intro_0 = pygame.image.load("sprites/grey_screen.png").convert_alpha()
        self.dark_green_screen_intro_0_rect= self.dark_green_screen_intro_0.get_rect(topleft = (0, 0))

        # gameboy image
        self.gameboy_image = pygame.image.load("sprites/gameboy_img.png").convert_alpha()

        # timer
        self.timer_state_intro_0 = "run"
        self.transition_state = "None"
        self.transition_timer = 0

        self.game_stuff_sound_timer = 10
        self.game_stuff_sound_counter = 0

    
    def draw(self):

        self.camera.display_surface.blit(self.game_stuff_logo_intro_0, self.game_stuff_logo_intro_0_rect)
    
    def update(self, dt):

        if self.game_stuff_logo_intro_0_rect.y > 60:
            self.game_stuff_logo_intro_0_rect.y = 60    

            # play sound
            self.game_stuff_sound_timer, self.game_stuff_sound_counter = self.sound.handle_repeat_sound(self.game_stuff_sound_timer, 10, 10, self.game_stuff_sound_counter, 1, self.sound.game_stuff_sound_path, dt)

            # self.transition_state = True
            
            if self.timer_state_intro_0 == "run":
                self.transition_timer += 1 * dt
                
            # print(self.transition_timer)

            if self.transition_timer > 2:

                if self.dark_green_screen_opacity_intro_0 >= 255:
                    self.dark_green_screen_opacity_intro_0 = 255
    
                self.dark_green_screen_opacity_intro_0 += 200 * dt

                self.dark_green_screen_intro_0.set_alpha(self.dark_green_screen_opacity_intro_0)
                self.camera.display_surface.blit(self.dark_green_screen_intro_0, self.dark_green_screen_intro_0_rect)
            
        

        self.game_stuff_logo_intro_0_rect.y += 125 * dt

        if self.transition_timer > 3:
            self.timer_state_intro_0 = "stop"
            self.game_path.go_to_intro_0 = False
            self.game_path.go_to_setup_controls = True
        
        
