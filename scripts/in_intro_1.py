import pygame, sys

from screen_setup import *
from colors import color
from font_custom import*
from music import Music
from sound import Sound


class InIntro1:

    def __init__(self, camera, game_path):

        self.intro_1_assets(camera)
        self.game_path = game_path

    def intro_1_assets(self, camera):

        self.main_display = pygame.display.get_surface()

        self.clock = pygame.time.Clock()

        self.camera = camera

        self.music = Music()
        self.sound = Sound()
        
        self.run = True

        # avoid text
        self.avoid_text_intro_1 = pygame.image.load("sprites/gui/avoid_text.png").convert_alpha()
        self.avoid_text_intro_1_rect = self.avoid_text_intro_1.get_rect(topleft = (0, -50))

        # copyright text
        self.copyright_text = pygame.image.load("sprites/gui/copyright_text.png").convert_alpha()
        self.copyright_text_rect = self.copyright_text.get_rect(topleft = (30, 140))

        # press start
        self.press_start_select_opacity = 0
        self.press_start_text_opacity_value = [-200, 200]
        self.press_start_text_opacity = 0
        self.press_start_text = pygame.image.load("sprites/gui/press_start_text.png").convert_alpha()
        self.press_start_text_rect = self.press_start_text.get_rect(topleft = (30, 65))

        # dark green screen
        self.dark_green_screen_opacity = 255
        self.dark_green_screen = pygame.image.load("sprites/black_screen.png").convert_alpha()
        self.dark_green_screen_rect = self.dark_green_screen.get_rect(topleft = (0, 0))

        # gameboy image
        self.gameboy_image = pygame.image.load("sprites/gameboy_img.png").convert_alpha()

        self.is_pressing_enter = False
        self.transition_state = "intro-1"

        self.avoid_title_sound_timer = 10
        self.avoid_title_sound_counter = 0
    

    def handle_input(self):

        key = pygame.key.get_pressed()
        # START KEY
        if key[pygame.K_n] and self.is_pressing_enter == False:
            self.is_pressing_enter = True
            
            if self.copyright_text_rect.y <= 95:
                # go to the main menu
                self.game_path.go_to_menu = True
                self.game_path.go_to_intro_1 = False
        
        if not key[pygame.K_n] and self.is_pressing_enter == True:
            self.is_pressing_enter = False
    
    def draw(self):
        
        self.camera.display_surface.blit(self.avoid_text_intro_1, self.avoid_text_intro_1_rect)

        self.camera.display_surface.blit(self.copyright_text, self.copyright_text_rect)
    
        
    def update(self, dt):
        
        self.handle_input()

        if self.dark_green_screen_opacity <= 0:
            self.dark_green_screen_opacity = 0
            
            if self.avoid_text_intro_1_rect.y > 15:
                self.avoid_text_intro_1_rect.y = 15

                # play sound
                self.avoid_title_sound_timer, self.avoid_title_sound_counter = self.sound.handle_repeat_sound(self.avoid_title_sound_timer, 10, 10, self.avoid_title_sound_counter, 1, self.sound.avoid_title_sound_path, dt)
        

                if self.copyright_text_rect.y <= 95:
                    self.copyright_text_rect.y = 95

                    # press start
                    if self.press_start_text_opacity <= 0:
                        self.press_start_select_opacity = 1
                    
                    if self.press_start_text_opacity >= 255:
                        self.press_start_select_opacity = 0

                    self.press_start_text_opacity += self.press_start_text_opacity_value[self.press_start_select_opacity] * dt
                    self.press_start_text.set_alpha(self.press_start_text_opacity)
                    self.camera.display_surface.blit(self.press_start_text, self.press_start_text_rect)

                self.copyright_text_rect.y -= 80 * dt

            self.avoid_text_intro_1_rect.y += 125 * dt
                

        # dark green screen
        self.dark_green_screen_opacity -= 255 * dt
        self.dark_green_screen.set_alpha(self.dark_green_screen_opacity)
        self.camera.display_surface.blit(self.dark_green_screen, self.dark_green_screen_rect)
