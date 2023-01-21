import pygame

from screen_setup import *
from colors import color

from sound import Sound

class InHowToPlay:

    def __init__(self, camera, game_path):
        self.how_to_play_assets(camera)
        self.game_path = game_path

    def how_to_play_assets(self, camera):

        self.camera = camera

        self.main_display = pygame.display.get_surface()

        self.clock = pygame.time.Clock()



        self.sound = Sound()
        
        self.run = True

        self.instructions_assets()

        self.instructions_display_surface = pygame.Surface((screen_width, screen_height - 160))
        self.instructions_display_surface_rect = self.instructions_display_surface.get_rect(topleft = (0, 28))

        self.instructions_frame_move = 0
        self.instructions_frame_crouch = 0
        self.instructions_frame_roll = 0
        self.instructions_frame_jump = 0
        self.instructions_frame_dance = 0


        # gameboy image
        self.gameboy_image = pygame.image.load("sprites/gameboy_img.png").convert_alpha()

        # movement instruction
        self.movement_how_to_play_img = self.instructions_move_list[self.instructions_frame_move]
        self.movement_how_to_play_img_rect = self.movement_how_to_play_img.get_rect(topleft = (0, 0))

        # crouch instruction
        self.crouch_how_to_play_img = self.instructions_crouch_list[self.instructions_frame_crouch]
        self.crouch_how_to_play_img_rect = self.crouch_how_to_play_img.get_rect(topleft = (0, 48))

        # jump instruction
        self.jump_how_to_play_img = self.instructions_jump_list[self.instructions_frame_jump]
        self.jump_how_to_play_img_rect = self.jump_how_to_play_img.get_rect(topleft = (0, 96))

        # roll instruction
        self.roll_how_to_play_img = self.instructions_roll_list[self.instructions_frame_roll]
        self.roll_how_to_play_img_rect = self.roll_how_to_play_img.get_rect(topleft = (0, 144))

        # dance instruction
        self.dance_how_to_play_img = self.instructions_dance_list[self.instructions_frame_dance]
        self.dance_how_to_play_img_rect = self.dance_how_to_play_img.get_rect(topleft = (0, 192))

        # how to play title
        self.in_how_to_play_text = pygame.image.load("sprites/gui/in_how_to_play.png").convert_alpha()
        self.in_how_to_play_text_rect = self.in_how_to_play_text.get_rect(topleft = (-3, 0))

        # exit
        self.exit_text_how_to_play = pygame.image.load("sprites/gui/exit_text.png").convert_alpha()
        self.exit_text_how_to_play_rect = self.exit_text_how_to_play.get_rect(topleft = (45, 120))

        # selector
        self.selector_how_to_play = pygame.image.load("sprites/gui/selector.png").convert_alpha()
        self.selector_how_to_play_rect = self.selector_how_to_play.get_rect(topleft = (20, 126))

        # button move left
        self.button_move_left_frame = 0
        self.button_move_left_img = self.button_move_left_list[self.button_move_left_frame]
        self.button_move_left_img_rect = self.button_move_left_img.get_rect(topleft = (0, 0))

        # button move right
        self.button_move_right_frame = 0
        self.button_move_right_img = self.button_move_right_list[self.button_move_right_frame]
        self.button_move_right_img_rect = self.button_move_right_img.get_rect(topleft = (0, 0))

        # button move down
        self.button_move_down_frame = 0
        self.button_move_down_img = self.button_move_right_list[self.button_move_down_frame]
        self.button_move_down_img_rect = self.button_move_down_img.get_rect(topleft = (0, 48))

        # button A
        self.button_a_frame = 0
        self.button_a_img = self.button_a_list[self.button_a_frame]
        self.button_a_img_rect = self.button_a_img.get_rect(topleft = (0, 96))

        # button B
        self.button_b_frame = 0
        self.button_b_img = self.button_b_list[self.button_b_frame]
        self.button_b_img_rect = self.button_b_img.get_rect(topleft = (0, 144))

        # button select
        self.button_select_frame = 0
        self.button_select_img = self.button_select_list[self.button_select_frame]
        self.button_select_img_rect = self.button_select_img.get_rect(topleft = (0, 192))


        self.up_down_instructions_scrolling_speed = 85

        self.is_pressing_p_how_to_play = False

        self.valid_sound_timer_how_to_play = 10

        self.select_key = 0
        self.key_up_controls = [pygame.K_z, pygame.K_w]


    def instructions_assets(self):

        # movement instructions
        self.instructions_move_list = []
        for i in range(71 + 1):
            img_movement = pygame.image.load(f"sprites/gui/options/movement/movement_{i}.png").convert_alpha()
            self.instructions_move_list.append(img_movement)
        
        # crouch instructions
        self.instructions_crouch_list = []
        for i in range(3 + 1):
            img_crouch = pygame.image.load(f"sprites/gui/options/crouch/crouch_{i}.png").convert_alpha()
            self.instructions_crouch_list.append(img_crouch)
        
        # jump instructions
        self.instructions_jump_list = []
        for i in range(7 + 1):
            img_jump = pygame.image.load(f"sprites/gui/options/jump/jump_{i}.png").convert_alpha()
            self.instructions_jump_list.append(img_jump)
        
        # roll instructions
        self.instructions_roll_list = []
        for i in range(18 + 1):
            img_roll = pygame.image.load(f"sprites/gui/options/rolling/rolling_{i}.png").convert_alpha()
            self.instructions_roll_list.append(img_roll)
        
        # dance instructions
        self.instructions_dance_list = []
        for i in range(11 + 1):
            img_dance = pygame.image.load(f"sprites/gui/options/dance/dance_{i}.png").convert_alpha()
            self.instructions_dance_list.append(img_dance)
        
        # button move left
        self.button_move_left_list = []
        for i in range(1 + 1):
            img_move_left = pygame.image.load(f"sprites/gui/options/move_left_{i}.png").convert_alpha()
            self.button_move_left_list.append(img_move_left)
        
        # button move right
        self.button_move_right_list = []
        for i in range(1 + 1):
            img_move_right = pygame.image.load(f"sprites/gui/options/move_right_{i}.png").convert_alpha()
            self.button_move_right_list.append(img_move_right)
        
        # button move down
        self.button_move_down_list = []
        for i in range(1 + 1):
            img_move_down = pygame.image.load(f"sprites/gui/options/move_down_{i}.png").convert_alpha()
            self.button_move_down_list.append(img_move_down)

        # button A
        self.button_a_list = []
        for i in range(1 + 1):
            img_button_a = pygame.image.load(f"sprites/gui/options/press_a_{i}.png").convert_alpha()
            self.button_a_list.append(img_button_a)
        
        # button B
        self.button_b_list = []
        for i in range(1 + 1):
            img_button_b = pygame.image.load(f"sprites/gui/options/press_b_{i}.png").convert_alpha()
            self.button_b_list.append(img_button_b)
        
        # button select
        self.button_select_list = []
        for i in range(1 + 1):
            img_button_select = pygame.image.load(f"sprites/gui/options/press_select_{i}.png").convert_alpha()
            self.button_select_list.append(img_button_select)
      


    def handle_input_how_to_play(self, dt):

        key = pygame.key.get_pressed()

        # GET THE AZERTY OR QWERTY CONTROLS
        if self.game_path.in_setup_controls.azerty_controls == True:
            self.select_key = 0
            
        else:
            if self.game_path.in_setup_controls.qwerty_controls == True:
                self.select_key = 1

        if self.valid_sound_timer_how_to_play > 0:
            self.valid_sound_timer_how_to_play -= 1

        if key[pygame.K_p] and self.is_pressing_p_how_to_play == False:
            self.is_pressing_p_how_to_play = True


            # exit how to play
            if self.dance_how_to_play_img_rect.y <= 48:
               
                self.game_path.go_to_how_to_play = False
                self.game_path.go_to_credits = False
                
                self.game_path.go_to_options = True
                
                if self.valid_sound_timer_how_to_play == 0:
                    self.valid_sound_timer_how_to_play = 10
                    if self.camera.game_path.in_options.stop_sound == "no":
                        self.sound.play("valid_sound")
        
        if not key[pygame.K_p] and self.is_pressing_p_how_to_play == True:
            self.is_pressing_p_how_to_play = False
            self.sound.stop("valid_sound")

        if key[pygame.K_s]:

            self.movement_how_to_play_img_rect.y -= round(self.up_down_instructions_scrolling_speed * dt)
            self.crouch_how_to_play_img_rect.y -= round(self.up_down_instructions_scrolling_speed * dt)
            self.jump_how_to_play_img_rect.y -= round(self.up_down_instructions_scrolling_speed * dt)
            self.roll_how_to_play_img_rect.y -= round(self.up_down_instructions_scrolling_speed * dt)
            self.dance_how_to_play_img_rect.y -= round(self.up_down_instructions_scrolling_speed * dt)

            # button move_left
            self.button_move_left_img_rect.y -= round(self.up_down_instructions_scrolling_speed * dt)

            # button move_right
            self.button_move_right_img_rect.y -= round(self.up_down_instructions_scrolling_speed * dt)

            # button move_down
            self.button_move_down_img_rect.y -= round(self.up_down_instructions_scrolling_speed * dt)

            # button A
            self.button_a_img_rect.y -= round(self.up_down_instructions_scrolling_speed * dt)

            # button B
            self.button_b_img_rect.y -= round(self.up_down_instructions_scrolling_speed * dt)

            # button select
            self.button_select_img_rect.y -= round(self.up_down_instructions_scrolling_speed * dt)
        
        if key[self.key_up_controls[self.select_key]]:

            self.movement_how_to_play_img_rect.y += round(self.up_down_instructions_scrolling_speed * dt)
            self.crouch_how_to_play_img_rect.y += round(self.up_down_instructions_scrolling_speed * dt)
            self.jump_how_to_play_img_rect.y += round(self.up_down_instructions_scrolling_speed * dt)
            self.roll_how_to_play_img_rect.y += round(self.up_down_instructions_scrolling_speed * dt)
            self.dance_how_to_play_img_rect.y += round(self.up_down_instructions_scrolling_speed * dt)

            # button move_left
            self.button_move_left_img_rect.y += round(self.up_down_instructions_scrolling_speed * dt)

            # button move_right
            self.button_move_right_img_rect.y += round(self.up_down_instructions_scrolling_speed * dt)

            # button move_down
            self.button_move_down_img_rect.y += round(self.up_down_instructions_scrolling_speed * dt)

            # button A
            self.button_a_img_rect.y += round(self.up_down_instructions_scrolling_speed * dt)

            # button B
            self.button_b_img_rect.y += round(self.up_down_instructions_scrolling_speed * dt)

            # button select
            self.button_select_img_rect.y += round(self.up_down_instructions_scrolling_speed * dt)
        
       
        # stop scrolling
        # movement
        if self.movement_how_to_play_img_rect.y <= -144:
            self.movement_how_to_play_img_rect.y = -144

        if self.movement_how_to_play_img_rect.y >= 0:
            self.movement_how_to_play_img_rect.y = 0

        # crouch
        if self.crouch_how_to_play_img_rect.y <= -96:
            self.crouch_how_to_play_img_rect.y = -96
        
        if self.crouch_how_to_play_img_rect.y >= 48:
            self.crouch_how_to_play_img_rect.y = 48

        # jump
        if self.jump_how_to_play_img_rect.y <= -48:
            self.jump_how_to_play_img_rect.y = -48
        
        if self.jump_how_to_play_img_rect.y >= 96:
            self.jump_how_to_play_img_rect.y = 96
        
        # roll
        if self.roll_how_to_play_img_rect.y <= 0:
            self.roll_how_to_play_img_rect.y = 0
        
        if self.roll_how_to_play_img_rect.y >= 144:
            self.roll_how_to_play_img_rect.y = 144
        
        # dance
        if self.dance_how_to_play_img_rect.y <= 48:
            self.dance_how_to_play_img_rect.y = 48
        
        if self.dance_how_to_play_img_rect.y >= 192:
            self.dance_how_to_play_img_rect.y = 192

        # button_move_left
        if self.button_move_left_img_rect.y <= -144:
            self.button_move_left_img_rect.y = -144
        
        if self.button_move_left_img_rect.y >= 0:
            self.button_move_left_img_rect.y = 0
        
        # button_move_right
        if self.button_move_right_img_rect.y <= -144:
            self.button_move_right_img_rect.y = -144
        
        if self.button_move_right_img_rect.y >= 0:
            self.button_move_right_img_rect.y = 0
        
        # button_move_down
        if self.button_move_down_img_rect.y <= -96:
            self.button_move_down_img_rect.y = -96
        
        if self.button_move_down_img_rect.y >= 48:
            self.button_move_down_img_rect.y = 48

        # button A
        if self.button_a_img_rect.y <= -48:
            self.button_a_img_rect.y = -48
        
        if self.button_a_img_rect.y >= 96:
            self.button_a_img_rect.y = 96
        
        # button B
        if self.button_b_img_rect.y <= 0:
            self.button_b_img_rect.y = 0
        
        if self.button_b_img_rect.y >= 144:
            self.button_b_img_rect.y = 144
        
        # button select
        if self.button_select_img_rect.y <= 48:
            self.button_select_img_rect.y = 48
        
        if self.button_select_img_rect.y >= 192:
            self.button_select_img_rect.y = 192

     

    def play_instructions_animations(self, dt):

        # instructions movement
        self.instructions_frame_move += 16 * dt

        if self.instructions_frame_move >= len(self.instructions_move_list):
            self.instructions_frame_move = 0

        self.movement_how_to_play_img = self.instructions_move_list[int(self.instructions_frame_move)]

        # instructions crouch
        self.instructions_frame_crouch += 5 * dt

        if self.instructions_frame_crouch >= len(self.instructions_crouch_list):
            self.instructions_frame_crouch = 0

        self.crouch_how_to_play_img = self.instructions_crouch_list[int(self.instructions_frame_crouch)]

        # instructions jump
        self.instructions_frame_jump += 16 * dt

        if self.instructions_frame_jump >= len(self.instructions_jump_list):
            self.instructions_frame_jump = 0

        self.jump_how_to_play_img = self.instructions_jump_list[int(self.instructions_frame_jump)]

        # instructions roll
        self.instructions_frame_roll += 10 * dt

        if self.instructions_frame_roll >= len(self.instructions_roll_list):
            self.instructions_frame_roll = 0

        self.roll_how_to_play_img = self.instructions_roll_list[int(self.instructions_frame_roll)]

        # instructions dance
        self.instructions_frame_dance += 8 * dt

        if self.instructions_frame_dance >= len(self.instructions_dance_list):
            self.instructions_frame_dance = 0

        self.dance_how_to_play_img = self.instructions_dance_list[int(self.instructions_frame_dance)]

        # button_move_left
        self.button_move_left_frame += 5 * dt

        if self.button_move_left_frame >= len(self.button_move_left_list):
            self.button_move_left_frame = 0
        
        self.button_move_left_img = self.button_move_left_list[int(self.button_move_left_frame)]

        # button_move_right
        self.button_move_right_frame += 6 * dt

        if self.button_move_right_frame >= len(self.button_move_right_list):
            self.button_move_right_frame = 0
        
        self.button_move_right_img = self.button_move_right_list[int(self.button_move_right_frame)]

        # button_move_down
        self.button_move_down_frame += 6 * dt

        if self.button_move_down_frame >= len(self.button_move_down_list):
            self.button_move_down_frame = 0
        
        self.button_move_down_img = self.button_move_down_list[int(self.button_move_down_frame)]

        # button A
        self.button_a_frame += 5 * dt

        if self.button_a_frame >= len(self.button_a_list):
            self.button_a_frame = 0
        
        self.button_a_img = self.button_a_list[int(self.button_a_frame)]

        # button B
        self.button_b_frame += 6 * dt

        if self.button_b_frame >= len(self.button_b_list):
            self.button_b_frame = 0
        
        self.button_b_img = self.button_b_list[int(self.button_b_frame)]

        # button select
        self.button_select_frame += 6 * dt

        if self.button_select_frame >= len(self.button_select_list):
            self.button_select_frame = 0
        
        self.button_select_img = self.button_select_list[int(self.button_select_frame)]


    def draw(self):

        # instruction display surface
        self.camera.display_surface.blit(self.instructions_display_surface, self.instructions_display_surface_rect)
        self.instructions_display_surface.fill(color["grey"])

        # instructions
        # movement
        self.instructions_display_surface.blit(self.movement_how_to_play_img, self.movement_how_to_play_img_rect)

        # crouch
        self.instructions_display_surface.blit(self.crouch_how_to_play_img, self.crouch_how_to_play_img_rect)

        # jump
        self.instructions_display_surface.blit(self.jump_how_to_play_img, self.jump_how_to_play_img_rect)

        # roll
        self.instructions_display_surface.blit(self.roll_how_to_play_img, self.roll_how_to_play_img_rect)

        # dance
        self.instructions_display_surface.blit(self.dance_how_to_play_img, self.dance_how_to_play_img_rect)

        # how to play title
        self.camera.display_surface.blit(self.in_how_to_play_text, self.in_how_to_play_text_rect)

        # exit
        self.camera.display_surface.blit(self.exit_text_how_to_play, self.exit_text_how_to_play_rect)

        # selector
        if self.dance_how_to_play_img_rect.y <= 48:
            self.camera.display_surface.blit(self.selector_how_to_play, self.selector_how_to_play_rect)
        
        # button_move_left
        self.instructions_display_surface.blit(self.button_move_left_img, (self.button_move_left_img_rect.x + 60, self.button_move_left_img_rect.y + 32))

        # button_move_right
        self.instructions_display_surface.blit(self.button_move_right_img, (self.button_move_right_img_rect.x + 80, self.button_move_right_img_rect.y + 32))

        # button_move_down
        self.instructions_display_surface.blit(self.button_move_down_img, (self.button_move_down_img_rect.x + 70, self.button_move_down_img_rect.y + 32))

        # button A
        self.instructions_display_surface.blit(self.button_a_img, (self.button_a_img_rect.x + 60, self.button_a_img_rect.y + 32))

        # button B
        self.instructions_display_surface.blit(self.button_b_img, (self.button_b_img_rect.x + 60, self.button_b_img_rect.y + 32))

        # button select
        self.instructions_display_surface.blit(self.button_select_img, (self.button_select_img_rect.x + 80, self.button_select_img_rect.y + 32))
        
    def update(self, dt):

        self.handle_input_how_to_play(dt)
        self.play_instructions_animations(dt)

        # reset template locations
        if self.game_path.go_to_how_to_play == False:
            self.movement_how_to_play_img_rect.y = 0
            self.crouch_how_to_play_img_rect.y = 48
            self.jump_how_to_play_img_rect.y = 96
            self.roll_how_to_play_img_rect.y = 144
            self.dance_how_to_play_img_rect.y = 192

            self.button_move_left_img_rect.y = 0
            self.button_move_right_img_rect.y = 0

            self.button_move_down_img_rect.y = 48

            self.button_a_img_rect.y = 96

            self.button_b_img_rect.y = 144

            self.button_select_img_rect.y = 192
    