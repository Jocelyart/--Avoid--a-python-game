import pygame, sys

from screen_setup import *


from sound import Sound

class InCredits:

    def __init__(self, camera, game_path):

        self.game_path = game_path


        self.sound = Sound()

        self.in_credits_assets(camera)

    def in_credits_assets(self, camera):

        self.main_display = pygame.display.get_surface()

        self.clock = pygame.time.Clock()

        self.camera = camera

        self.run = True

        # credits text
        self.created_by_text = pygame.image.load("sprites/gui/credits/created_by.png").convert_alpha()
        self.created_by_text_rect = self.created_by_text.get_rect(topleft = (0, 0))

        # selector
        self.selector_in_credits = pygame.image.load("sprites/gui/selector.png").convert_alpha()
        self.selector_in_credits_rect = self.selector_in_credits.get_rect(topleft = (20, 126))

        # exit
        self.exit_text_in_credits = pygame.image.load("sprites/gui/exit_text.png").convert_alpha()
        self.exit_text_in_credits_rect = self.exit_text_in_credits.get_rect(topleft = (45, 120))

        # gameboy image
        self.gameboy_image = pygame.image.load("sprites/gameboy_img.png").convert_alpha()

        self.is_pressing_p = False

        self.valid_sound_timer_credits = 10

        self.active_input_delay = "yes"
        self.input_delay = 10


    def handle_inputs(self, dt):

        key = pygame.key.get_pressed()

        if self.active_input_delay == "yes":
            if self.input_delay > 0:
                self.input_delay -= 5 * dt

                if self.input_delay < 9:
                    self.input_delay = 8
                    self.active_input_delay = "no"

        if key[pygame.K_p] and self.is_pressing_p == False:
            self.is_pressing_p = True

            if self.camera.game_path.in_options.stop_sound == "no":
                self.sound.play("valid_sound")

            if self.selector_in_credits_rect.y == 126 and self.input_delay < 9:
                self.game_path.go_to_credits = False
                self.game_path.go_to_options = True
               
        else:
            if not key[pygame.K_p] and self.is_pressing_p == True:
                self.is_pressing_p = False
   
    def draw(self):

        # credits text
        self.camera.display_surface.blit(self.created_by_text, self.created_by_text_rect)

        # selector
        self.camera.display_surface.blit(self.selector_in_credits, self.selector_in_credits_rect)

        # exit
        self.camera.display_surface.blit(self.exit_text_in_credits, self.exit_text_in_credits_rect)


    def update(self, dt):
        
        self.handle_inputs(dt)

        if self.game_path.go_to_credits == False:
            self.selector_in_credits_rect.y = 126
            self.active_input_delay = "yes"
            self.input_delay = 10

   
