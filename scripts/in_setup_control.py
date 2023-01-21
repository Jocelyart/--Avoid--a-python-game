import pygame

from sound import Sound

class InSetupControl:

    def __init__(self, camera, game_path):

        self.camera = camera
        self.game_path = game_path
        self.sound = Sound()

        # controls image
        self.controls_img = pygame.image.load("sprites/gui/controls.png").convert_alpha()
        self.controls_img_rect = self.controls_img.get_rect(topleft = (0, 0))

        # selector
        self.selector_img = pygame.image.load("sprites/gui/selector.png").convert_alpha()
        self.selector_img_rect = self.selector_img.get_rect(topleft = (20, 48))

        self.is_pressing_enter = False
        self.is_pressing_up = False
        self.is_pressing_down = False

        self.azerty_controls = False
        self.qwerty_controls = False

    def handle_inputs(self):
        key = pygame.key.get_pressed()

        # press Enter
        if key[pygame.K_RETURN] and self.is_pressing_enter == False:
            self.is_pressing_enter = True
            
            # AZERTY CONTROLS
            if self.selector_img_rect.y == 48:
                self.azerty_controls = True
                self.game_path.go_to_setup_controls = False
                self.game_path.go_to_intro_1 = True
                self.sound.play("valid_sound")
                
            # QWERTY CONTROLS
            if self.selector_img_rect.y == 76:
                self.qwerty_controls = True
                self.game_path.go_to_setup_controls = False
                self.game_path.go_to_intro_1 = True
                self.sound.play("valid_sound")
                

        if not key[pygame.K_RETURN] and self.is_pressing_enter == True:
            self.is_pressing_enter = False

        # press Up
        if key[pygame.K_UP] and self.is_pressing_up == False:
            self.is_pressing_up = True
            self.selector_img_rect.y -= 28
            self.sound.play("selector_sound")

        else:
            if not key[pygame.K_UP] and self.is_pressing_up == True:
                self.is_pressing_up = False

        # press Down
        if key[pygame.K_DOWN] and self.is_pressing_down == False:
            self.is_pressing_down = True
            self.selector_img_rect.y += 28
            self.sound.play("selector_sound")

        else:
            if not key[pygame.K_DOWN] and self.is_pressing_down == True:
                self.is_pressing_down = False
        
        # selector restriction
        if self.selector_img_rect.y < 48:
            self.selector_img_rect.y = 76

        if self.selector_img_rect.y > 76:
            self.selector_img_rect.y = 48
            
    def update(self, dt):
        self.handle_inputs()

    def draw(self):
        
        self.camera.display_surface.blit(self.controls_img, self.controls_img_rect)

        self.camera.display_surface.blit(self.selector_img, self.selector_img_rect)
