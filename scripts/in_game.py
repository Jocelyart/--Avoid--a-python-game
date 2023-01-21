import pygame

from random import randint
from screen_setup import *
from colors import color
from font_custom import*
from level1 import Level1
from music import Music
from flash_image_system import *
from particle import handle_particle_update


class InGame:

    def __init__(self, camera, game_path):

        self.game_assets(camera)
        self.pause_menu_assets()
        self.game_path = game_path


    def game_assets(self, camera):

        self.main_display = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.camera = camera
        self.level1 = Level1(camera)

        self.music = Music()

        # background game normal zone
        self.background = pygame.image.load("sprites/bckg.png").convert_alpha()

        # background game evil zone
        self.evil_background = pygame.image.load("sprites/bckg_evil_zone.png").convert_alpha()

        # gameboy image
        self.gameboy_image = pygame.image.load("sprites/gameboy_img.png").convert_alpha()

        # game_intro_screen ======================================================================
        self.show_game_intro = "yes"
        self.game_intro_screen = pygame.Surface((screen_width, screen_height)).convert()
        self.game_intro_screen_rect = self.game_intro_screen.get_rect(topleft = (0, 0))
        self.select_text_part = 0
        self.speech_text_list = [
                            "In a world blackened by chaos,", 
                            "ruled by demonic creatures when Man is a prey.", 
                            "You have nothing to defend yourself,", 
                            "the only way to survive is to avoid them.",
                            ]

        self.speech_intro_text = my_font_size_14.render(self.speech_text_list[self.select_text_part], 0, color["light_grey"])
        self.speech_intro_text_rect = self.speech_intro_text.get_rect(topleft = (0, 0))

        self.speech_timer = 0
        self.speech_text_pos_x = 0
        self.speech_text_pos_y = 0
        self.spacing = 0
        self.dialogue_box_img = pygame.image.load("sprites/gui/dialogue_box.png").convert_alpha()
        self.dialogue_box_img_rect = self.dialogue_box_img.get_rect(topleft = (0, 94))

        self.demon_town_frame = 0
        self.demon_town_sprite_list = []

        # handle multiple sprites demon over town
        for i in range(4):
            img = pygame.image.load(f"sprites/gui/game_intro/{i}.png").convert_alpha()
            self.demon_town_sprite_list.append(img)

        self.demon_town_img = self.demon_town_sprite_list[self.demon_town_frame]
        self.demon_town_img_rect = self.demon_town_img.get_rect(topleft = (0, 0))

        self.button_a_in_game_frame = 0
        self.button_a_in_game_img_list = []

        # handle multiple sprites button A
        for i in range(2):
            img = pygame.image.load(f"sprites/gui/options/press_a_{i}.png").convert_alpha()
            self.button_a_in_game_img_list.append(img)

        self.button_a_in_game_img = self.button_a_in_game_img_list[self.button_a_in_game_frame]
        self.button_a_in_game_img_rect = self.button_a_in_game_img.get_rect(topleft = (118, 123))

        self.in_game_screen = 0

        # ========================================================================================

        self.scroll_x = 0
        self.delay = 0
        
        self.scrolling_mode = "off"

        self.transition_state = "in_game"

        # on/off flash image
        self.flash_img = 0
        self.reset_flash_img = 0

        # camera position
        self.camera_pos = pygame.math.Vector2()
        self.camera_direction = pygame.math.Vector2()

        self.red_screen_img = pygame.image.load("sprites/red_screen.png").convert_alpha()
        self.red_screen_img_rect = self.red_screen_img.get_rect(topleft = (0, 0))

        self.is_pressing_p = False

        self.game_screen_counter = 0

        self.select_key = 0
        self.key_up_controls = [pygame.K_z, pygame.K_w]
     
        self.pause_menu_assets()


        
    def pause_menu_assets(self):
        # pause menu
        self.pause_menu_window = pygame.image.load("sprites/gui/pause/pause_window.png").convert_alpha()
        self.pause_menu_window_rect = self.pause_menu_window.get_rect(topleft = (24, 29))

        self.pause_counter = 1
        self.pause_menu_surface = pygame.Surface((76, 58))
        self.pause_menu_surface_rect = self.pause_menu_surface.get_rect(topleft = (36, 40))

        # selector
        self.selector_pause_menu = pygame.image.load("sprites/gui/pause/selector_menu.png").convert_alpha()
        self.selector_pause_menu_rect = self.selector_pause_menu.get_rect(topleft = (2, 22))

        # pause title
        self.pause_text_title = pygame.image.load("sprites/gui/pause/pause_text.png").convert_alpha()
        self.pause_text_title_rect = self.pause_text_title.get_rect(topleft = (10, 3))

        # restart
        self.restart_text = pygame.image.load("sprites/gui/pause/restart_text.png").convert_alpha()
        self.restart_text_rect = self.restart_text.get_rect(topleft = (10, 20))

        # main_menu
        self.main_menu_text = pygame.image.load("sprites/gui/pause/main_menu_text.png").convert_alpha()
        self.main_menu_text_rect = self.main_menu_text.get_rect(topleft = (10, 35))

        # pause key
        self.is_pressing_pause_key = False 

        # selector keys
        # move
        self.is_pressing_up_pause_menu = False
        self.is_pressing_down_pause_menu = False

        # pressed
        self.is_pressing_p_pause_menu = False

        # restart timer
        self.restart_timer = 0

        # evil background particle
        self.evil_bckg_particle1_timer = 0
        self.evil_bckg_particle1_list = []
    
    def handle_game_pause_input(self):
        
        key = pygame.key.get_pressed()

        # GET THE AZERTY OR QWERTY CONTROLS
        if self.game_path.in_setup_controls.azerty_controls == True:
            self.select_key = 0
            
        else:
            if self.game_path.in_setup_controls.qwerty_controls == True:
                self.select_key = 1

        # pause
        if key[pygame.K_n] and self.is_pressing_pause_key == False:
            self.is_pressing_pause_key = True
            self.level1.music.pause()

            if self.pause_counter > 1:
                self.pause_counter = 0
                self.level1.music.unpause() 

            self.pause_counter += 1

        if not key[pygame.K_n] and self.is_pressing_pause_key == True:
            self.is_pressing_pause_key = False



        # in pause menu
        if self.pause_counter == 2:
            # pause key pressed
            if key[pygame.K_p] and self.is_pressing_p_pause_menu == False:
                self.is_pressing_p_pause_menu = True
                # restart
                if self.selector_pause_menu_rect.y == 22:
                
                    self.pause_counter = 1
                    self.reset_the_game()
                    self.game_screen_counter = 2

                    # stop the mixer
                    pygame.mixer.stop()
                    
                # go back to main menu
                if self.selector_pause_menu_rect.y == 37:

                    self.game_path.go_to_game = False
                    self.game_path.go_to_options = False
                    self.game_path.go_to_how_to_play = False
                    self.game_path.go_to_credits = False

                    self.game_path.go_to_menu = True

                    # stop the mixer
                    pygame.mixer.stop()
            
            if not key[pygame.K_p] and self.is_pressing_p_pause_menu == True:
                self.is_pressing_p_pause_menu = False


            # move selector
            # up
            if key[self.key_up_controls[self.select_key]] and self.is_pressing_up_pause_menu == False:
                self.is_pressing_up_pause_menu = True

                self.selector_pause_menu_rect.y -= 15
            
            if not key[self.key_up_controls[self.select_key]] and self.is_pressing_up_pause_menu == True:
                self.is_pressing_up_pause_menu = False
            
            # down
            if key[pygame.K_s] and self.is_pressing_down_pause_menu == False:
                self.is_pressing_down_pause_menu = True

                self.selector_pause_menu_rect.y += 15
            
            if not key[pygame.K_s] and self.is_pressing_down_pause_menu == True:
                self.is_pressing_down_pause_menu = False
        
   
    
    def follow_target(self, dt):
        
        # target and position on screen
        target_x = self.level1.player.rect.x - (screen_width // 2)

        # stop scrolling
        if self.scrolling_mode == "on":
            # camera follow target
            self.scroll_x += (target_x - self.scroll_x) * self.delay * dt
    
    def draw_game_objects(self):
        # draw layer 0
        for sprite in self.level1.layer0_sprites:
            self.camera.display_surface.blit(sprite.image, (sprite.rect.x - round(self.scroll_x), sprite.rect.y))
        
        # draw zombie behind herb
        self.level1.zombie.draw(self.camera.display_surface)

        # draw layer 1
        for sprite in self.level1.layer1_sprites:
            self.camera.display_surface.blit(sprite.image, (sprite.rect.x - round(self.scroll_x), sprite.rect.y))
        
        
        # draw layer 2
        for sprite in self.level1.layer2_sprites:
            self.camera.display_surface.blit(sprite.image, (sprite.rect.x - round(self.scroll_x), sprite.rect.y))
        
        # draw heart
        self.level1.heart.draw(self.camera.display_surface)

                
        # draw player
        for player in self.level1.player_sprite:
            
            # readjust the player sprite
            if player.is_alive == "yes":
                if player.is_crouching == 1:
                    player.hitbox_inflate_x = 6
                    player.hitbox_inflate_y = 22
                
                elif player.is_rolling == 1:
                    player.hitbox_inflate_x = 6
                    player.hitbox_inflate_y = 23

                else:
                    player.hitbox_inflate_x = 6
                    player.hitbox_inflate_y = 17
            
            else:
                if player.is_alive == "no":
                    if player.is_dead == 1 and player.flip == False:
                        player.hitbox_inflate_x = 6
                        player.hitbox_inflate_y = 29
                    
                    if player.is_dead == 1 and player.flip == True:
                        player.hitbox_inflate_x = 22
                        player.hitbox_inflate_y = 29

            # normal image
            img = pygame.transform.flip(player.image, player.flip, 0)

            # mask image filled
            img2 = flashing_damage(img, color["light_grey"])

            # put normal img and mask img filled in a list
            img_flash = [img, img2]     

            rect = (player.rect.x - player.hitbox_inflate_x - round(self.scroll_x), player.rect.y - player.hitbox_inflate_y)

            # handle flash duration
            if self.flash_img == 0:
                self.reset_flash_img = 0

            if self.flash_img == 1:
                self.reset_flash_img += 1

                if self.reset_flash_img >= 20:
                    self.reset_flash_img = 20
                    self.flash_img = 0
                
            if player.is_alive == "no":
                self.flash_img = 0
                
            if self.level1.gui.boss_timer < 1088:   
                self.camera.display_surface.blit(img_flash[self.flash_img], rect)

            # draw player vfx
            self.camera.display_surface.blit(player.vfx_healing_image, (player.rect.x - 14, player.rect.y - 5))
         
            # draw thanks for playing text
            player.thanks_for_playing_text.set_alpha(player.thanks_text_opacity) 
            self.camera.display_surface.blit(player.thanks_for_playing_text, (player.rect.x - 10, player.rect.y - 15))

        # draw boss1
        for boss1 in self.level1.boss1_sprite:

            if self.level1.gui.boss_timer < 1088:  
                # ================================== BULLETS DRAW BEHIND THE BOSS =====================================
                # draw demon projectile head
                for bullet in boss1.head_normal_projectile_sprite:
                    self.camera.display_surface.blit(bullet.demon_bullet_list[bullet.demon_frame], (bullet.x - round(self.scroll_x), bullet.y))

                # draw spear
                for spear in boss1.head_spear_projectile_sprite:
                    self.camera.display_surface.blit(spear.image, (spear.x - round(self.scroll_x), spear.y))

                # draw cross projectile left hand
                for bullet in boss1.left_cross_projectile_sprite:
                    self.camera.display_surface.blit(bullet.image, (bullet.rect.x - round(self.scroll_x), bullet.rect.y))
                
                # draw cross projectile right hand
                for bullet in boss1.right_cross_projectile_sprite:
                    self.camera.display_surface.blit(bullet.image, (bullet.rect.x - round(self.scroll_x), bullet.rect.y))

                # draw normal projectile left hand
                for bullet in boss1.left_hand_normal_bullet_sprite_list:
                    self.camera.display_surface.blit(bullet.image, (bullet.rect.x - round(self.scroll_x), bullet.rect.y))

                # draw normal projectile right hand
                for bullet in boss1.right_hand_normal_bullet_sprite_list:
                    self.camera.display_surface.blit(bullet.image, (bullet.rect.x - round(self.scroll_x), bullet.rect.y))

                # draw rain
                for rain in boss1.rain_projectile_sprites_list:
                    self.camera.display_surface.blit(rain.image, (rain.rect.x - round(self.scroll_x), rain.rect.y))
                # =====================================================================================================

                # ================================== BULLETS PARTICLES ================================================

                # demon bullet
                for demon_bullet_particle1 in boss1.demon_bullet_particle1_list:
                    demon_bullet_particle1.image.set_alpha(demon_bullet_particle1.opacity)
                    self.camera.display_surface.blit(demon_bullet_particle1.image, demon_bullet_particle1.rect)
                
                # left cross bullet
                for left_cross_bullet_particle1 in boss1.left_cross_bullet_particle1_list:
                    left_cross_bullet_particle1.image.set_alpha(left_cross_bullet_particle1.opacity)
                    self.camera.display_surface.blit(left_cross_bullet_particle1.image, left_cross_bullet_particle1.rect)

                # right cross bullet
                for right_cross_bullet_particle1 in boss1.right_cross_bullet_particle1_list:
                    right_cross_bullet_particle1.image.set_alpha(right_cross_bullet_particle1.opacity)
                    self.camera.display_surface.blit(right_cross_bullet_particle1.image, right_cross_bullet_particle1.rect)

                # left normal bullet
                for left_bullet_particle1 in boss1.left_bullet_particle1_list:
                    left_bullet_particle1.image.set_alpha(left_bullet_particle1.opacity)
                    self.camera.display_surface.blit(left_bullet_particle1.image, left_bullet_particle1.rect)

                # right normal bullet
                for right_bullet_particle1 in boss1.right_bullet_particle1_list:
                    right_bullet_particle1.image.set_alpha(right_bullet_particle1.opacity)
                    self.camera.display_surface.blit(right_bullet_particle1.image, right_bullet_particle1.rect)

                # =====================================================================================================

                # draw left hand cross bullet
                left_hand_img = boss1.left_hand_img
                left_hand_img_rect = (boss1.left_hand_rect.x - round(self.scroll_x), boss1.left_hand_rect.y)

                self.camera.display_surface.blit(left_hand_img, left_hand_img_rect)

                # draw right hand cross bullet
                right_hand_img = boss1.right_hand_img
                right_hand_img_rect = (boss1.right_hand_rect.x - round(self.scroll_x), boss1.right_hand_rect.y)

                self.camera.display_surface.blit(right_hand_img, right_hand_img_rect)
                

                # draw left hand bullet  
                boss1.left_hand_bullet_img.set_alpha(255)
                left_hand_bullet_img = boss1.left_hand_bullet_img
                left_hand_bullet_img_rect = (boss1.left_hand_bullet_img_rect.x - round(self.scroll_x), boss1.left_hand_bullet_img_rect.y)

                self.camera.display_surface.blit(left_hand_bullet_img, left_hand_bullet_img_rect)

                # draw right hand bullet
                right_hand_bullet_img = boss1.right_hand_bullet_img
                right_hand_bullet_img_rect = (boss1.right_hand_bullet_img_rect.x - round(self.scroll_x), boss1.right_hand_bullet_img_rect.y)

                self.camera.display_surface.blit(right_hand_bullet_img, right_hand_bullet_img_rect)

                # ============================= LEFT HAND CROSS BULLET PARTICLES ================================
                for particle1_l in boss1.particle1_list_left_hand:
                    particle1_l.image.set_alpha(particle1_l.opacity)
                    self.camera.display_surface.blit(particle1_l.image, particle1_l.rect)
                
                for particle2_l in boss1.particle2_list_left_hand:
                    particle2_l.image.set_alpha(particle2_l.opacity)
                    self.camera.display_surface.blit(particle2_l.image, particle2_l.rect)
                
                for particle3_l in boss1.particle3_list_left_hand:
                    particle3_l.image.set_alpha(particle3_l.opacity)
                    self.camera.display_surface.blit(particle3_l.image, particle3_l.rect)
                
                # left hand particle - fast speed
                for particle4_l in boss1.particle1_list_left_hand_cross_bullet_list:
                    self.camera.display_surface.blit(particle4_l.image, particle4_l.rect)
                # =========================================================================================

                # ============================= RIGHT HAND CROSS BULLET PARTICLES ================================
                for particle1_r in boss1.particle1_list_right_hand:
                    particle1_r.image.set_alpha(particle1_r.opacity)
                    self.camera.display_surface.blit(particle1_r.image, particle1_r.rect)
                
                for particle2_r in boss1.particle2_list_right_hand:
                    particle2_r.image.set_alpha(particle2_r.opacity)
                    self.camera.display_surface.blit(particle2_r.image, particle2_r.rect)
                
                for particle3_r in boss1.particle3_list_right_hand:
                    particle3_r.image.set_alpha(particle3_r.opacity)
                    self.camera.display_surface.blit(particle3_r.image, particle3_r.rect)
                
                # right hand particle - fast speed
                for particle4_r in boss1.particle1_list_right_hand_cross_bullet_list:
                    self.camera.display_surface.blit(particle4_r.image, particle4_r.rect)
                
                # ============================= RIGHT HAND BULLET PARTICLES ================================
                for particle1_bullet_l in boss1.left_hand_bullet_particle1_list:
                    particle1_bullet_l.image.set_alpha(particle1_bullet_l.opacity)
                    self.camera.display_surface.blit(particle1_bullet_l.image, particle1_bullet_l.rect)

                for particle1_bullet_r in boss1.right_hand_bullet_particle1_list:
                    particle1_bullet_r.image.set_alpha(particle1_bullet_r.opacity)
                    self.camera.display_surface.blit(particle1_bullet_r.image, particle1_bullet_r.rect)
                # =========================================================================================

                # draw head
                head_img = boss1.image
                head_rect = (boss1.rect.x - round(self.scroll_x), boss1.rect.y)

                
                self.camera.display_surface.blit(head_img, head_rect)

        """ Draw flame wall particle """
        if self.level1.player.evil_zone > 3:

            # right flame wall
            for flame1 in self.level1.player.flame_wall_particle1_list:
                self.camera.display_surface.blit(flame1.image, flame1.rect)
            
            for flame2 in self.level1.player.flame_wall_particle2_list:
                self.camera.display_surface.blit(flame2.image, flame2.rect)
            
            for flame3 in self.level1.player.flame_wall_particle3_list:
                self.camera.display_surface.blit(flame3.image, flame3.rect)
            
            # left flame wall
            for flame4 in self.level1.player.flame_wall_particle4_list:
                self.camera.display_surface.blit(flame4.image, flame4.rect)
            
            for flame5 in self.level1.player.flame_wall_particle5_list:
                self.camera.display_surface.blit(flame5.image, flame5.rect)
            
            for flame6 in self.level1.player.flame_wall_particle6_list:
                self.camera.display_surface.blit(flame6.image, flame6.rect)
        

    def draw_game_intro(self):
        # game intro
        self.game_intro_screen.fill(color["grey"])
        self.camera.display_surface.blit(self.game_intro_screen, self.game_intro_screen_rect)   

        # draw demon over town
        self.camera.display_surface.blit(self.demon_town_img, self.demon_town_img_rect)

        # draw dialogue box
        self.camera.display_surface.blit(self.dialogue_box_img, self.dialogue_box_img_rect)

        # draw button A
        self.camera.display_surface.blit(self.button_a_in_game_img, self.button_a_in_game_img_rect)

        for sentence_index, sentence in enumerate(self.speech_text_list):
            
            if sentence_index == self.select_text_part:
                for letter_index, _ in enumerate(sentence):

                    if sentence_index == 0:
                        if 0 <= letter_index < 18:
                            self.speech_text_pos_x = 10
                            self.speech_text_pos_y = 100
                        
                        if letter_index > 19:
                            self.speech_text_pos_x = -137
                            self.speech_text_pos_y = 112
                    
                    if sentence_index == 1:
                        if 0 <= letter_index < 14:
                            self.speech_text_pos_x = 10
                            self.speech_text_pos_y = 100
                        
                        if letter_index > 15:
                            self.speech_text_pos_x = -110
                            self.speech_text_pos_y = 112
                        
                        if letter_index > 37:
                            self.speech_text_pos_x = -263
                            self.speech_text_pos_y = 125
                    
                    if sentence_index == 2:
                        if 0 <= letter_index < 18:
                            self.speech_text_pos_x = 10
                            self.speech_text_pos_y = 100
                        
                        if letter_index > 19:
                            self.speech_text_pos_x = -130
                            self.speech_text_pos_y = 115
                    
                    if sentence_index == 3:
                        if 0 <= letter_index < 14:
                            self.speech_text_pos_x = 10
                            self.speech_text_pos_y = 100
                        
                        if letter_index > 15:
                            self.speech_text_pos_x = -103
                            self.speech_text_pos_y = 112
                        
                        if letter_index > 35:
                            self.speech_text_pos_x = -242
                            self.speech_text_pos_y = 125

                    self.speech_intro_text = my_font_size_14.render(self.speech_text_list[sentence_index][letter_index], 0, color["light_grey"])

                    self.camera.display_surface.blit(self.speech_intro_text, (7 * letter_index + self.speech_text_pos_x, 10 * self.spacing + self.speech_text_pos_y)) 
            
          
    def camera_shake(self, camera, speed):

        if self.level1.player.is_alive == "yes":
            direction_x = [-1, 1]
            camera.display_surface_rect.x += direction_x[randint(0, 1)] * speed

            direction_y = [-1, 1]
            camera.display_surface_rect.y += direction_y[randint(0, 1)] * speed
           
       

    def camera_movement_init(self, dt):

        if self.level1.player.is_alive == "yes":
            self.camera_pos = self.camera.display_surface_rect

            # initialize camera position on X
            # print(self.camera_pos.x)

            if self.camera_pos.x <= 59:
                self.camera_direction.x = 1
                self.camera_pos.x += self.camera_direction.x * 200 * dt
                self.camera.display_surface_rect.x = round(self.camera_pos.x)
            
            elif self.camera_pos.x >= 61:
                self.camera_direction.x = -1
                self.camera_pos.x += self.camera_direction.x * 200 * dt
                self.camera.display_surface_rect.x = round(self.camera_pos.x)
            
            else:
                self.camera_direction.x = 0
            
            # initialize camera position on Y
            # print(self.camera_pos.y)

            if self.camera_pos.y <= 49:
                self.camera_direction.y = 1
                self.camera_pos.y += self.camera_direction.y * 200 * dt
                self.camera.display_surface_rect.y = round(self.camera_pos.y)
            
            elif self.camera_pos.y >= 51:
                self.camera_direction.y = -1
                self.camera_pos.y += self.camera_direction.y * 200 * dt
                self.camera.display_surface_rect.y = round(self.camera_pos.y)
            
            else:
                self.camera_direction.y = 0

        else:
            if self.level1.player.is_alive == "no":
                self.camera_pos.x = 60
                self.camera.display_surface_rect.x = self.camera_pos.x

                self.camera_pos.y = 50
                self.camera.display_surface_rect.y = self.camera_pos.y
    
            
            

    def reset_the_game(self):
        
        # reset game screen
        self.game_screen_counter = 1

        # reset pause menu -> off
        self.pause_counter = 1

        # reset player control
        self.level1.player.is_alive = "yes"

        # reset death animation
        self.level1.player.death_frame = 0

        # reset hitbox
        self.level1.player.select_hitbox = 0
        self.level1.player.hitbox = self.level1.player.hitbox_list[self.level1.player.select_hitbox]

        # reset player location
        self.level1.player.hitbox.x = 64
        self.level1.player.hitbox.y = 113

        # reset player state
        self.level1.player.is_idle = 1
        self.level1.player.is_dancing = 0
        self.level1.player.is_jumping = 0
        self.level1.player.is_rolling = 0
        self.level1.player.is_crouching = 0

        # reset player healing timer
        self.level1.player.healing_timer = 10

        # reset player vfx healing frame
        self.level1.player.vfx_healing_image_frame = 0
        self.level1.player.run_vfx_healing_animation = "no"

        # reset player voice healing yes
        self.level1.player.voice_healing_yes_timer = 10
        self.level1.player.voice_healing_yes_timer_counter = 0

        # reset player dance energy counter
        self.level1.player.energy_counter = 0
        self.level1.player.energy_counter_rounded = 0

        # reset player corner lover
        self.level1.player.corner_lover_timer = 30

        # reset zombie location
        self.level1.zombie.pos.x = 200
        self.level1.zombie.stop_moving = "yes"
        self.level1.zombie.new_location = "None"

        self.level1.zombie.direction.x = 0

        # reset tomb collision timer
        self.level1.zombie.collision_state_timer = 10
        self.level1.zombie.tomb_randomizer = 5

        # reset collision state
        self.level1.zombie.collision_state = "player"

        # reset / randomize heart location
        self.level1.zombie.select_tomb = 0

        # reset heart opacity
        self.level1.heart.opacity = 0

        # reset heart vfx frames
        self.level1.heart.vfx_01_frame = 0
        self.level1.heart.vfx_02_frame = 0
        self.level1.heart.vfx_03_frame = 0

        # reset heart start vfx
        self.level1.heart.start_vfx_animation = False

        # reset player pick up heart sound timer
        self.level1.zombie.pick_up_heart_timer = 10
        self.level1.zombie.pick_up_heart_timer_counter = 0

        # reset doors sound
        self.level1.doors.doors_sound_timer = 10
        self.level1.doors.doors_sound_timer_counter = 0

        # reset evil zone
        self.level1.player.evil_zone = 0

        # reset boss timer
        self.level1.gui.boss_timer = self.level1.gui.boss_timer_value

        # reset boss sound start
        self.level1.boss1.transition_sound_timer = 10
        self.level1.boss1.transition_sound_timer_counter = 0

        # reset life
        self.level1.gui.life_number = 1

        # reset life unit
        self.level1.gui.life_unit = 10

        # reset thanks text opacity
        self.level1.player.thanks_text_opacity = 0

        # clear demon bullet list
        self.level1.boss1.head_normal_projectile_sprite.clear()

        # clear left cross bullet list
        self.level1.boss1.left_cross_projectile_sprite.clear()

        # reset spawing left cross bullet
        self.level1.boss1.left_hand_randomize_spawn = 200

        # clear right cross bullet list
        self.level1.boss1.right_cross_projectile_sprite.clear()

        # reset spawing right cross bullet
        self.level1.boss1.right_hand_randomize_spawn = 200

        # clear left normal bullet list
        self.level1.boss1.left_hand_normal_bullet_sprite_list.clear()

        # clear right normal bullet list
        self.level1.boss1.right_hand_normal_bullet_sprite_list.clear()
        
        # clear rain list
        self.level1.boss1.rain_projectile_sprites_list.clear()

        # reset rain oscillation
        self.level1.boss1.rain_oscillation = False

        # reset left hand bullet
        self.level1.boss1.left_hand_bullet_pos_x = -50
        self.level1.boss1.left_hand_bullet_img_rect.x = self.level1.boss1.left_hand_bullet_pos_x

        self.level1.boss1.left_hand_bullet_pos_y = 110
        self.level1.boss1.left_hand_bullet_img_rect.y = self.level1.boss1.left_hand_bullet_pos_y

        # reset right hand bullet
        self.level1.boss1.right_hand_bullet_pos_x = 180
        self.level1.boss1.right_hand_bullet_img_rect.x = self.level1.boss1.right_hand_bullet_pos_x

        self.level1.boss1.right_hand_bullet_pos_y = 110
        self.level1.boss1.right_hand_bullet_img_rect.y = self.level1.boss1.right_hand_bullet_pos_y

        # reset death sound
        self.level1.player.death_sound_timer = 10
        self.level1.player.death_sound_counter = 0

        # reset boss1 voice
        self.level1.player.boss1_sound_timer = 10
        self.level1.player.boss1_sound_counter = 0

        # reset start fight boss 1 voice
        self.level1.boss1.voice_intro_timer = 10
        self.level1.boss1.voice_intro_counter = 0

        # reset boss 1 voice stay in corners
        self.level1.player.boss1_voice_stay_corners_timer = 10
        self.level1.player.boss1_voice_stay_corners_timer_counter = 0

        # reset boss 1 voice smartass
        self.level1.player.boss1_voice_smartass_timer = 10
        self.level1.player.boss1_voice_smartass_timer_counter = 0

        # reset boss 1 voice Enough! Die!
        self.level1.player.boss1_voice_enough_die_timer = 10
        self.level1.player.boss1_voice_enough_die_timer_counter = 0

        # reset end fight voice
        self.level1.boss1.avoided_sound_timer = 10
        self.level1.boss1.avoided_sound_counter = 0

        # reset evil boss1 voice dont piss me off
        self.level1.player.evil_boss1_piss_me_off_sound_timer = 10
        self.level1.player.evil_boss1_piss_me_off_sound_counter = 0

        # reset evil boss1 voice what
        self.level1.player.evil_boss1_what_sound_timer = 10
        self.level1.player.evil_boss1_what_sound_counter = 0

        # reset evil boss1 voice stop doing that
        self.level1.player.evil_boss1_stop_that_sound_timer = 10
        self.level1.player.evil_boss1_stop_that_sound_counter = 0

        # reset evil boss1 voice i said stop
        self.level1.player.evil_boss1_i_said_stop_sound_timer = 10
        self.level1.player.evil_boss1_i_said_stop_sound_counter = 0
        
        # reset boss1 shaking camera
        self.level1.boss1.camera_shake_timer = 4

        # reset flame wall collision timer
        self.level1.player.flame_wall_collision_timer = 2

        # reset doors
        self.level1.doors.open_doors_delay = 10
        self.level1.doors.left_door_img_rect.x = 0
        self.level1.doors.right_door_img_rect.x = 80
        self.level1.doors.open_doors_delay_evil_zone = 5

        # reset particles
        self.level1.boss1.particle1_list_left_hand.clear()
        self.level1.boss1.particle2_list_left_hand.clear()
        self.level1.boss1.particle3_list_left_hand.clear()

        self.level1.boss1.particle1_list_right_hand.clear()
        self.level1.boss1.particle2_list_right_hand.clear()
        self.level1.boss1.particle3_list_right_hand.clear()

        self.level1.boss1.demon_bullet_particle1_list.clear()

        self.level1.boss1.head_normal_projectile_sprite.clear()
        self.level1.boss1.left_cross_projectile_sprite.clear()
        self.level1.boss1.right_cross_projectile_sprite.clear()

        self.level1.boss1.left_cross_bullet_particle1_list.clear()
        self.level1.boss1.right_cross_bullet_particle1_list.clear()

        self.level1.boss1.left_hand_bullet_particle1_list.clear()
        self.level1.boss1.right_hand_bullet_particle1_list.clear()
        
        self.level1.boss1.left_bullet_particle1_list.clear()
        self.level1.boss1.right_bullet_particle1_list.clear()

        self.level1.boss1.rain_projectile_sprites_list.clear()

        # flame particles
        self.level1.player.flame_wall_particle1_list.clear()
        self.level1.player.flame_wall_particle2_list.clear()
        self.level1.player.flame_wall_particle3_list.clear()

        self.level1.player.flame_wall_particle4_list.clear()
        self.level1.player.flame_wall_particle5_list.clear()
        self.level1.player.flame_wall_particle6_list.clear()


    def handle_animation_game(self, dt):

        # demon over town animation
        self.demon_town_frame += 4 * dt

        if self.demon_town_frame >= len(self.demon_town_sprite_list):
            self.demon_town_frame = 0
        
        self.demon_town_img = self.demon_town_sprite_list[int(self.demon_town_frame)]

        # button A animation
        self.button_a_in_game_frame += 4 * dt

        if self.button_a_in_game_frame >= len(self.button_a_in_game_img_list):
            self.button_a_in_game_frame = 0
        
        self.button_a_in_game_img = self.button_a_in_game_img_list[int(self.button_a_in_game_frame)]


    def handle_evil_background_particles(self, dt):

        self.evil_bckg_particle1_timer, self.evil_bckg_particle1_list = handle_particle_update(self.evil_bckg_particle1_timer, 15, self.evil_bckg_particle1_list, randint(0, 140), 122, randint(5, 7), 200, False, 0, True, -100, dt)
    

    def draw(self):

        # draw game intro
        if self.in_game_screen == 0:
            self.draw_game_intro()

           
        if self.in_game_screen == 1:
            # draw backgrounds
            if self.level1.player.evil_zone > 3:
                self.evil_background.set_alpha(150)
                self.camera.display_surface.blit(self.evil_background, (0, 0))

                for particle1 in self.evil_bckg_particle1_list:
                    self.camera.display_surface.blit(particle1.image, particle1.rect)

            else:
                self.background.set_alpha(150)
                self.camera.display_surface.blit(self.background, (0, 0))

            # draw levels
            self.draw_game_objects()

            # draw GUI
            self.level1.gui.draw()

            # draw doors
            """ DRAW DOORS TRANSITION NORMAL/EVIL ZONE """
            self.level1.doors.draw(self.camera.display_surface)

            # draw pause menu
            if self.pause_counter == 2:

                # draw pause menu window sprite    
                self.camera.display_surface.blit(self.pause_menu_window, self.pause_menu_window_rect)

                # draw pause menu window surface
                self.camera.display_surface.blit(self.pause_menu_surface, self.pause_menu_surface_rect)
                self.pause_menu_surface.fill(color["grey"])

                # pause title
                self.pause_menu_surface.blit(self.pause_text_title, self.pause_text_title_rect)

                # restart
                self.pause_menu_surface.blit(self.restart_text, self.restart_text_rect)

                # main menu
                self.pause_menu_surface.blit(self.main_menu_text, self.main_menu_text_rect)

                # selector
                self.pause_menu_surface.blit(self.selector_pause_menu, self.selector_pause_menu_rect)
            

            # screen filter
            if self.level1.player.evil_zone > 3:
                self.camera.display_surface.blit(self.red_screen_img, self.red_screen_img_rect, None, pygame.BLEND_RGB_ADD)

    def update(self, dt):
        
        if self.in_game_screen == 0: # game intro
            
            key = pygame.key.get_pressed()

            if key[pygame.K_p] and self.is_pressing_p == False:
                self.is_pressing_p = True

                self.game_screen_counter += 1

                # game intro
                if self.game_screen_counter == 1:
                    self.in_game_screen = 0
                
                # actual game
                if self.game_screen_counter == 2:
                    self.in_game_screen = 1
               
            
            if not key[pygame.K_p] and self.is_pressing_p == True:
                self.is_pressing_p = False

            # animate demon
            self.handle_animation_game(dt)
            
            # switch sentences
            self.speech_timer += 1 * dt
            my_speech_timer = round(self.speech_timer)

            if 0 <= my_speech_timer < 4:
                self.select_text_part = 0
            
            if my_speech_timer > 5:
                self.select_text_part = 1
            
            if my_speech_timer > 10:
                self.select_text_part = 2
            
            if my_speech_timer > 13:
                self.select_text_part = 3
            
            if my_speech_timer >= 20:
                self.speech_timer = 20

                 
        if self.in_game_screen == 1:
            self.handle_game_pause_input()
            
            # RESET THE GAME
            if self.game_path.go_to_game == False: 
                
                self.reset_the_game()

                # reset in game screen
                self.speech_timer = 0
                self.in_game_screen = 0

            # selector limit
            # in pause menu
            if self.pause_counter == 2:

                if self.selector_pause_menu_rect.y < 22:
                    self.selector_pause_menu_rect.y = 37

                if self.selector_pause_menu_rect.y > 37:
                    self.selector_pause_menu_rect.y = 22
                
                # pause mixer
                pygame.mixer.pause()    

            
            if self.pause_counter == 1: # in actual game
                # in game
                self.follow_target(dt)
                self.level1.update(dt)
                self.level1.gui.update(dt)

                # evil background particles update
                if self.level1.player.evil_zone > 3:
                    self.handle_evil_background_particles(dt)

                # unpause
                pygame.mixer.unpause()

                # reset selector position
                self.selector_pause_menu_rect.y = 22
            
                self.camera_movement_init(dt)

                