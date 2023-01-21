import pygame

from random import randint

from projectile import CrossProjectile, LeftBulletProjectile, RightBulletProjectile, DemonProjectile, RainProjectile, math_projectile, SpearProjectile

from particle import Particle

class Boss1:

    def __init__(self, x, y, level):

        self.level = level
        self.handle_sprites()

        self.head_frame = 0

        self.left_hand_frame = 0
        self.left_hand_bullet_frame = 0
        self.evil_left_hand_bullet_frame = 0

        self.right_hand_frame = 0
        self.right_hand_bullet_frame = 0
        self.evil_right_hand_bullet_frame = 0

        # head
        self.head_center_rect = pygame.Rect(x, y, 80, 80)
        self.image = self.head_sprite_list[self.head_frame]
        self.rect = self.image.get_rect(topleft = (x, y - 40)) # -30, -40

        self.head_pos = pygame.math.Vector2()
        self.left_hand_pos = pygame.math.Vector2()
        self.right_hand_pos = pygame.math.Vector2()

        # evil head
        self.evil_head_frame = 0

        # left hand cross bullet
        self.left_hand_img = self.left_hand_sprite_list[self.left_hand_frame]
        self.left_hand_rect  = self.left_hand_img.get_rect(topleft = (x - 50, y))

        # evil left hand cross bullet
        self.evil_left_hand_frame = 0

        # right hand cross bullet
        self.right_hand_img = self.right_hand_sprite_list[self.right_hand_frame]
        self.right_hand_rect  = self.right_hand_img.get_rect(topleft = (x + 50, y + 20))

        # evil right hand cross bullet
        self.evil_right_hand_frame = 0

        # left hand bullet
        self.left_hand_bullet_img = self.left_hand_bullet_sprite_list[self.left_hand_bullet_frame]
        self.left_hand_bullet_img_rect = self.left_hand_bullet_img.get_rect(topleft = (x - 125, y + 110))

        # right hand bullet
        self.right_hand_bullet_img = self.right_hand_bullet_sprite_list[self.right_hand_bullet_frame]
        self.right_hand_bullet_img_rect = self.right_hand_bullet_img.get_rect(topleft = (x + 110, y + 110))

        # cross bullet
        self.head_normal_projectile_sprite = []
        self.left_cross_projectile_sprite = []
        self.right_cross_projectile_sprite = []

        # spear
        self.head_spear_projectile_sprite = []

        # normal bullet
        self.left_hand_normal_bullet_sprite_list = []
        self.right_hand_normal_bullet_sprite_list = []

        # left hand bullet particle
        self.left_hand_bullet_particle1_list = []
        self.left_hand_bullet_particle1_timer = 0

        # right hand bullet particle
        self.right_hand_bullet_particle1_list = []
        self.right_hand_bullet_particle1_timer = 0

        # demon bullet particle
        self.demon_bullet_particle1_list = []
        self.demon_bullet_particle1_timer = 0

        # left cross bullet particle
        self.left_cross_bullet_particle1_list = []
        self.left_cross_bullet_particle1_timer = 0

        # right cross bullet particle
        self.right_cross_bullet_particle1_list = []
        self.right_cross_bullet_particle1_timer = 0

        # left bullet particle
        self.left_bullet_particle1_list = []
        self.left_bullet_particle1_timer = 0

        # right bullet particle
        self.right_bullet_particle1_list = []
        self.right_bullet_particle1_timer = 0

        # left hand particle
        self.particle1_list_left_hand = []
        self.particle2_list_left_hand = []
        self.particle3_list_left_hand = []

        self.particle1_list_left_hand_cross_bullet_list = []
        self.particle1_list_left_hand_cross_bullet_timer = 0

        self.left_particle1_timer = 0
        self.left_particle2_timer = 0
        self.left_particle3_timer = 0

        # right hand particle
        self.particle1_list_right_hand = []
        self.particle2_list_right_hand = []
        self.particle3_list_right_hand = []

        self.particle1_list_right_hand_cross_bullet_list = []
        self.particle1_list_right_hand_cross_bullet_timer = 0

        self.right_particle1_timer = 0
        self.right_particle2_timer = 0
        self.right_particle3_timer = 0
    

        self.head_timer = 0
        self.left_hand_timer = 0
        self.right_hand_timer = 0
        self.left_hand_normal_bullet_timer = 0
        self.right_hand_normal_bullet_timer = 0

        self.spear_timer = 0
        

        # hands cross bullets
        self.left_hand_pos_x = self.left_hand_rect.x
        self.left_hand_pos_y = self.left_hand_rect.y

        self.right_hand_pos_x = self.right_hand_rect.x
        self.right_hand_pos_y = self.right_hand_rect.y

        # hands bullets
        self.left_hand_bullet_pos_x = self.left_hand_bullet_img_rect.x
        self.left_hand_bullet_pos_y = self.left_hand_bullet_img_rect.y

        self.right_hand_bullet_pos_x = self.right_hand_bullet_img_rect.x
        self.right_hand_bullet_pos_y = self.right_hand_bullet_img_rect.y

        self.upper_body_part = "None"
        self.left_body_part = "None"
        self.right_body_part = "None"

        self.spawn_projectile_head = "yes"
        self.spawn_projectile_left_hand = "yes"
        self.spawn_projectile_right_hand  ="yes"

        self.head_projectile_fire = "None"
        self.left_hand_projectile_fire = "None"
        self.right_hand_projectile_fire = "None"

        self.right_hand_bullet_fire = "None"

        self.attack_state = "None"

        # self.bullet_speed = randint(50, 150)

        self.head_direction = pygame.math.Vector2()
        self.left_hand_direction = pygame.math.Vector2()
        self.right_hand_direction = pygame.math.Vector2()

        self.attack_step = 0

        self.follow_player_right_hand = 0
        self.follow_player_left_hand = 0

        self.move_x_left_hand = 0
        self.move_x_right_hand = 0

        self.head_fire_select = 0
        self.left_fire_select = 0
        self.right_fire_select = 0

        self.head_fire = ["yes", "no"]
        self.left_hand_fire = ["yes", "no"]
        self.right_hand_fire = ["yes", "no"]

        self.head_movement = [0, 0]
        self.head_up_down_move = [0, 0]
        self.up_down_step = 0

        self.left_hand_speed = 200
        self.left_hand_speed_selector = 0
        self.left_hand_movement = [-400, 200]
        self.right_hand_movement = [0, 0]

        self.head_randomize_spawn = randint(50, 200)
        self.left_hand_randomize_spawn = 200
        self.right_hand_randomize_spawn = 200
        self.rain_randomize_spawn = 20

        self.right_hand_bullet_randomize_spawn = 1

        self.game_screen_width = 150

        self.attack2_speed_select = 0
        self.attack2_speed = [-100, 100]

        self.rain_projectile_timer = 0
        self.rain_projectile_sprites_list = []

        self.head_size_speed = 100
        self.head_move_speed = 100

        self.voice_intro_timer = 10
        self.voice_intro_counter = 0

        self.avoided_sound_timer = 10
        self.avoided_sound_counter = 0

        self.cross_bullet_sound_timer = 10
        self.cross_bullet_sound_counter = 0

        self.rain_projectile_angle = 0
        self.rain_oscillation = False

        self.mute_voice = "no"

        self.camera_shake_timer = 4

        self.play_sfx = "yes"
        self.play_voice = "yes"

        self.transition_sound_timer = 10
        self.transition_sound_timer_counter = 0
        


    def handle_sprites(self):

        # head sprites
        self.head_sprite_size = [80, 80]
        self.head_sprite_list = []

        for i in range(17 + 1):
            head_img = pygame.transform.scale(pygame.image.load(f"sprites/boss/level1/head/{i}.png").convert_alpha(), self.head_sprite_size)
            
            self.head_sprite_list.append(head_img)
        
        # evil head sprites
        self.evil_head_sprite_size = [80, 80]
        self.evil_head_sprite_list = []

        for i in range(11 + 1):
            evil_head = pygame.transform.scale(pygame.image.load(f"sprites/boss/level1/evil_head/{i}.png").convert_alpha(), self.evil_head_sprite_size)

            self.evil_head_sprite_list.append(evil_head)

        # left_hand_sprites_cross_bullet
        self.left_hand_size = (16, 48)
        self.left_hand_sprite_list = []

        for i in range(6 + 1):
            left_hand_img = pygame.transform.scale(pygame.image.load(f"sprites/boss/level1/left_hand/{i}.png").convert_alpha(), self.left_hand_size)

            self.left_hand_sprite_list.append(left_hand_img)
        
        # evil left hand sprites cross bullet
        self.evil_left_hand_size = (16, 48)
        self.evil_left_hand_sprite_list = []

        for i in range(5 + 1):
            evil_left_hand_img = pygame.transform.scale(pygame.image.load(f"sprites/boss/level1/evil_left_hand/{i}.png").convert_alpha(), self.evil_left_hand_size)

            self.evil_left_hand_sprite_list.append(evil_left_hand_img)    

        # right_hand_sprites_cross_bullet
        self.right_hand_size = (16, 48)
        self.right_hand_sprite_list = []

        for i in range(6 + 1):
            right_hand_img = pygame.transform.scale(pygame.image.load(f"sprites/boss/level1/right_hand/{i}.png").convert_alpha(), self.right_hand_size)

            self.right_hand_sprite_list.append(right_hand_img)
        

        # evil right hand sprites cross bullet
        self.evil_right_hand_size = (16, 48)
        self.evil_right_hand_sprite_list = []

        for i in range(5 + 1):
            evil_right_hand_img = pygame.transform.scale(pygame.image.load(f"sprites/boss/level1/evil_right_hand/{i}.png").convert_alpha(), self.evil_right_hand_size)

            self.evil_right_hand_sprite_list.append(evil_right_hand_img) 
        
        # left_hand_bullet_sprites
        self.left_hand_bullet_size = (32, 16)
        self.left_hand_bullet_sprite_list = []

        for i in range(1 + 1):
            left_hand_bullet_img = pygame.transform.scale(pygame.image.load(f"sprites/boss/level1/left_hand_bullet/{i}.png").convert_alpha(), self.left_hand_bullet_size)

            self.left_hand_bullet_sprite_list.append(left_hand_bullet_img)
        
        # evil_left_hand_bullet_sprites
        self.evil_left_hand_bullet_size = (32, 16)
        self.evil_left_hand_bullet_sprite_list = []

        for i in range(1 + 1):
            evil_left_hand_bullet_img = pygame.transform.scale(pygame.image.load(f"sprites/boss/level1/evil_left_hand_bullet/{i}.png").convert_alpha(), self.evil_left_hand_bullet_size)

            self.evil_left_hand_bullet_sprite_list.append(evil_left_hand_bullet_img)

        # right_hand_bullet_sprites
        self.right_hand_bullet_size = (32, 16)
        self.right_hand_bullet_sprite_list = []

        for i in range(1 + 1):
            right_hand_bullet_img = pygame.transform.scale(pygame.image.load(f"sprites/boss/level1/right_hand_bullet/{i}.png").convert_alpha(), self.right_hand_bullet_size)

            self.right_hand_bullet_sprite_list.append(right_hand_bullet_img)
        
        # evil_right_hand_bullet_sprites
        self.evil_right_hand_bullet_size = (32, 16)
        self.evil_right_hand_bullet_sprite_list = []

        for i in range(1 + 1):
            evil_right_hand_bullet_img = pygame.transform.scale(pygame.image.load(f"sprites/boss/level1/evil_right_hand_bullet/{i}.png").convert_alpha(), self.evil_right_hand_bullet_size)

            self.evil_right_hand_bullet_sprite_list.append(evil_right_hand_bullet_img)


    def spawn_projectile(self, dt):
        
        # HEAD ========================================
        if self.head_projectile_fire == "yes" and self.level.player.corner_lover_timer != 0:
            if self.spawn_projectile_head == "yes":
                # head timer
                self.head_timer += self.head_randomize_spawn * dt # 50
                head_time = self.head_timer * dt

                # boss aim toward player
                if head_time > 1:
                    self.head_timer = 0

                    # sound
                    if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                        self.level.sound.randomized_sound_play(self.level.sound.demon_bullet_sound_list, randint(0, 2))

                    self.head_randomize_spawn = randint(50, 200)
                    x = self.rect.x + 50
                    y = self.rect.y 
                    target_x = self.level.player.hitbox.x
                    target_y = self.level.player.hitbox.y

                    self.head_normal_projectile_sprite.append(DemonProjectile(x, y, target_x, target_y))
        
        # spear 
        if self.level.player.is_alive == "yes" and self.level.player.corner_lover_timer == 0:
            
            # spear timer
            self.spear_timer += 2 * dt
            spear_time = round(self.spear_timer)

            # boss aim toward player
            if spear_time > 1:
                self.spear_timer = 0

                x = self.rect.x + 50
                y = self.rect.y
                target_x = self.level.player.hitbox.x
                target_y = self.level.player.hitbox.y

                self.head_spear_projectile_sprite.append(SpearProjectile(x, y, target_x, target_y))

                    
        # LEFT HAND ===================================
        if self.left_hand_projectile_fire == "yes":
            if self.spawn_projectile_left_hand == "yes":    
                # left hand timer
                self.left_hand_timer += self.left_hand_randomize_spawn * dt # 500
                my_left_hand_timer = self.left_hand_timer * dt

                if my_left_hand_timer > 1:
                    self.left_hand_timer = 0

                    if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                        if self.play_sfx == "yes":
                            self.level.sound.play("cross_bullet_sound")
                    
                    # left hand
                    x = self.left_hand_rect.x + 3
                    y = self.left_hand_rect.y + 40
                    self.left_cross_projectile_sprite.append(CrossProjectile(x, y))
        
        if self.attack_state == "attack2-step1" or self.attack_state == "attack2-step2-left":
            # left hand bullet
            self.left_hand_normal_bullet_timer += self.left_hand_bullet_randomize_spawn * dt
            my_left_hand_normal_bullet_timer = round(self.left_hand_normal_bullet_timer)

            if my_left_hand_normal_bullet_timer > 1:
                self.left_hand_normal_bullet_timer = 0

                # sound
                if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                    self.level.sound.play("normal_bullet_sound")

                x = self.left_hand_bullet_img_rect.x + 30
                y = self.left_hand_bullet_img_rect.y + 7
                self.left_hand_normal_bullet_sprite_list.append(LeftBulletProjectile(x, y))
           
        # RIGHT HAND ================================================================
        if self.right_hand_projectile_fire == "yes":
            if self.spawn_projectile_right_hand == "yes":
                # right hand timer
                self.right_hand_timer += self.right_hand_randomize_spawn * dt
                my_right_hand_timer = self.right_hand_timer * dt
                

                if my_right_hand_timer > 1:
                    self.right_hand_timer = 0
                    
                    if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                        if self.play_sfx == "yes":
                            self.level.sound.play("cross_bullet_sound")

                    # right hand
                    x = self.right_hand_rect.x + 5
                    y = self.right_hand_rect.y + 42
                    self.right_cross_projectile_sprite.append(CrossProjectile(x, y))

              

        if self.attack_state == "attack2-step1" or self.attack_state == "attack2-step2-right":
            # right hand bullet
            self.right_hand_normal_bullet_timer += self.right_hand_bullet_randomize_spawn * dt
            my_right_hand_normal_bullet_timer = round(self.right_hand_normal_bullet_timer)

            if my_right_hand_normal_bullet_timer > 1:
                self.right_hand_normal_bullet_timer = 0

                # sound
                if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                    self.level.sound.play("normal_bullet_sound")

                x = self.right_hand_bullet_img_rect.x - 2
                y = self.right_hand_bullet_img_rect.y + 7
                self.right_hand_normal_bullet_sprite_list.append(RightBulletProjectile(x, y))
        
        if self.attack_state == "rain":
            # rain
            self.rain_projectile_timer += self.rain_randomize_spawn * dt
            my_rain_projectile_timer = round(self.rain_projectile_timer)

            if my_rain_projectile_timer > 1:
                self.rain_projectile_timer = 0

                x = randint(0, self.game_screen_width)
                y = randint(-100, -70)
                self.rain_projectile_sprites_list.append(RainProjectile(x, y, randint(200, 250)))
        

    def combat_state(self, dt):
        
        # player is dead -> boss mode neutral follow
        if self.level.player.is_alive == "no":

            self.head_up_down_move[self.up_down_step] = 100

            self.attack_state = "follow"
          
            self.head_fire_select = 1       # - no
            self.left_fire_select = 1       # - no
            self.right_fire_select = 1      # - no

            # reset left hand bullet
            self.left_hand_bullet_pos_x -= 80 * dt

            if self.left_hand_bullet_pos_x < -50:
                self.left_hand_bullet_pos_x = -50
            self.left_hand_bullet_img_rect.x = self.left_hand_bullet_pos_x


            # reset right hand bullet
            self.right_hand_bullet_pos_x += 80 * dt

            if self.right_hand_bullet_pos_x > 180:
                self.right_hand_bullet_pos_x = 180
            self.right_hand_bullet_img_rect.x = self.right_hand_bullet_pos_x

            # stop boss music
            self.level.music.fadeout(100) 

            
        if self.level.player.is_alive == "yes":
            
            # ATTACK STATES ===========================================
            if self.level.gui.boss_timer < 1090: # start
                
                self.play_sfx = "no"

                self.upper_body_part = "head"
                self.left_body_part = "left_hand"
                self.right_body_part = "right_hand"

                self.attack_state = "start"
            
                self.head_fire_select = 1       # - no
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no
            
            if self.level.gui.boss_timer < 1085: # 1085 boss intro

                # START THE FIGHT  
                if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                    if self.play_voice == "yes":
                        self.voice_intro_timer, self.voice_intro_counter = self.level.sound.handle_repeat_sound(self.voice_intro_timer, 9, 10, self.voice_intro_counter, 1, self.level.sound.boss1_voice_intro_sound_path, dt)


            if self.level.gui.boss_timer < 1050: # follow idle

                if self.camera_shake_timer > 0:
                    self.camera_shake_timer -= 1 * dt
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 1)

                self.head_up_down_move[self.up_down_step] = 70

                self.attack_state = "follow"
            
                self.head_fire_select = 1       # - no
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no

            if self.level.gui.boss_timer < 1040:
                if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                    
                    self.transition_sound_timer, self.transition_sound_timer_counter = self.level.sound.handle_repeat_sound(self.transition_sound_timer, 10, 10, self.transition_sound_timer_counter, 2, self.level.sound.boss1_transition_path, dt)

            if self.level.gui.boss_timer < 1000: # follow attack
               
                self.play_sfx = "yes"

                if self.level.player.evil_zone > 3:
                    self.head_randomize_spawn = 500
                    self.left_hand_randomize_spawn = 200
                    self.right_hand_randomize_spawn = 200
                else:
                    self.head_randomize_spawn = 100
                    self.left_hand_randomize_spawn = 150
                    self.right_hand_randomize_spawn = 150
                
                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"
            
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 0       # - yes
                self.right_fire_select = 0      # - yes


            if self.level.gui.boss_timer < 980: # attack 1

                self.head_up_down_move[self.up_down_step] = 100

                if self.level.player.evil_zone > 3:
                    self.left_hand_randomize_spawn = 700
                    self.right_hand_randomize_spawn = 700
                else:
                    self.left_hand_randomize_spawn = 500
                    self.right_hand_randomize_spawn = 500

        
                self.attack_state = "attack1"

                self.head_fire_select = 1       # - no
                self.left_fire_select = 0       # - yes
                self.right_fire_select = 0      # - yes
    
                

            if self.level.gui.boss_timer < 950: # follow idle

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"
    
                self.head_fire_select = 1       # - no
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no

    
            if self.level.gui.boss_timer < 940: # transition 2 
              
                if self.camera_shake_timer > 0:
                    self.camera_shake_timer -= 1 * dt
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 1)

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "transition2"

                # zombie wait
                self.level.zombie.stop_moving = "yes"


            if self.level.gui.boss_timer < 930: # transition 2 step 1

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "transition2-step1"

             

            if self.level.gui.boss_timer < 925: # attack 2 step 1

                self.head_up_down_move[self.up_down_step] = -100

                if self.level.player.evil_zone > 3:
                    self.left_hand_bullet_randomize_spawn = 3
                    self.right_hand_bullet_randomize_spawn = 3
                else:
                    self.left_hand_bullet_randomize_spawn = 2
                    self.right_hand_bullet_randomize_spawn = 2

                self.attack_state = "attack2-step1"

                self.level.zombie.stop_moving = "yes"

            if self.level.gui.boss_timer < 900: # attack 2 step 2 right hand

                self.head_up_down_move[self.up_down_step] = -100

                if self.level.player.evil_zone > 3:
                    self.right_hand_bullet_randomize_spawn = 4
                else:
                    self.right_hand_bullet_randomize_spawn = 3

                self.attack_state = "attack2-step2-right"


            if self.level.gui.boss_timer < 870: # attack 2 step 2 left hand

                self.head_up_down_move[self.up_down_step] = -100

                if self.level.player.evil_zone > 3:
                    self.left_hand_bullet_randomize_spawn = 4
                else:
                    self.left_hand_bullet_randomize_spawn = 3

                self.attack_state = "attack2-step2-left"
        

            if self.level.gui.boss_timer < 850: # transition 2 step 2

                if self.camera_shake_timer > 0:
                    self.camera_shake_timer -= 1 * dt
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 1)

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "transition2-step2"
            
    
            if self.level.gui.boss_timer < 840: # follow idle

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                # transition
    
                self.head_fire_select = 1       # - no
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no

                # zombie go left
                self.level.zombie.new_location = "left"

            

            if self.level.gui.boss_timer < 830: # follow attack

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                if self.level.player.evil_zone > 3:
                    self.head_randomize_spawn = 300
                else:
                    self.head_randomize_spawn = 100
    
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 0       # - yes
                self.right_fire_select = 0      # - yes

                # zombie wait
                self.level.zombie.stop_moving = "yes"
            

            if self.level.gui.boss_timer < 800: # attack 1

                self.head_up_down_move[self.up_down_step] = 50

                if self.level.player.evil_zone > 3:
                    self.left_hand_randomize_spawn = 700
                    self.right_hand_randomize_spawn = 700
                else:
                    self.left_hand_randomize_spawn = 500
                    self.right_hand_randomize_spawn = 500
        
                self.attack_state = "attack1"

                self.head_fire_select = 1       # - no
                self.left_fire_select = 0       # - yes
                self.right_fire_select = 0      # - yes


            if self.level.gui.boss_timer < 750: # follow attack

                self.head_up_down_move[self.up_down_step] = -100

                if self.level.player.evil_zone > 3:
                    self.head_randomize_spawn = 500
                else:
                    self.head_randomize_spawn = 400

                self.attack_state = "follow"
    
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no
            

            if self.level.gui.boss_timer < 700: # transition 2

                if self.camera_shake_timer > 0:
                    self.camera_shake_timer -= 1 * dt
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 1)

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "transition2"

                self.head_fire_select = 1


            if self.level.gui.boss_timer < 690: # rain

                self.head_up_down_move[self.up_down_step] = -100

                if self.level.player.evil_zone > 3:
                    self.rain_randomize_spawn = 30
                else:
                    self.rain_randomize_spawn = 20

                self.attack_state = "rain"
    
                self.head_fire_select = 1       # - no
            

            if self.level.gui.boss_timer < 600: # follow idle

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                # transition
    
                self.head_fire_select = 1       # - no
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no

                # zombie go right
                self.level.zombie.stop_moving = "no"
                self.level.zombie.new_location = "right"
                
            
            if self.level.gui.boss_timer < 595: # follow attack head spamming

                self.head_up_down_move[self.up_down_step] = -100

                if self.level.player.evil_zone > 3:
                    self.head_randomize_spawn = 500
                else:
                    self.head_randomize_spawn = 400

                self.attack_state = "follow"
    
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no

                self.level.zombie.stop_moving = "yes"
                

            if self.level.gui.boss_timer < 550: # follow idle

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

    
                self.head_fire_select = 1       # - no
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no
            
            if self.level.gui.boss_timer < 545: # transition 2 
              
                if self.camera_shake_timer > 0:
                    self.camera_shake_timer -= 1 * dt
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 1)

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "transition2"
            
            if self.level.gui.boss_timer < 535: # transition 2 step 1

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "transition2-step1"
            
            if self.level.gui.boss_timer < 530: # attack 2 step 2 left hand

                self.head_up_down_move[self.up_down_step] = -100

                if self.level.player.evil_zone > 3:
                    self.left_hand_bullet_randomize_spawn = 6
                else:
                    self.left_hand_bullet_randomize_spawn = 5

                self.attack_state = "attack2-step2-left"
            
            if self.level.gui.boss_timer < 500: # attack 2 step 2 right hand

                self.head_up_down_move[self.up_down_step] = -100

                if self.level.player.evil_zone > 3:
                    self.right_hand_bullet_randomize_spawn = 6
                else:
                    self.right_hand_bullet_randomize_spawn = 5

                self.attack_state = "attack2-step2-right"
            
            if self.level.gui.boss_timer < 470: # attack 2 step 1

                self.head_up_down_move[self.up_down_step] = -100

                # already fast enough normal/evil zone
                self.left_hand_bullet_randomize_spawn = 3
                self.right_hand_bullet_randomize_spawn = 3

                self.attack_state = "attack2-step1"
            
            if self.level.gui.boss_timer < 430: # transition 2 step 2

                if self.camera_shake_timer > 0:
                    self.camera_shake_timer -= 1 * dt
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 1)

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "transition2-step2"

            if self.level.gui.boss_timer < 420: # follow idle

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                # transition
    
                self.head_fire_select = 1       # - no
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no

                # zombie go left
                self.level.zombie.stop_moving = "no"
                self.level.zombie.new_location = "left"
            
            if self.level.gui.boss_timer < 410: # follow attack

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"


                self.head_fire_select = 0       # - yes
                self.left_fire_select = 0       # - yes
                self.right_fire_select = 0      # - yes

                self.level.zombie.stop_moving = "yes"
                
            
            if self.level.gui.boss_timer < 400: # attack 1

                self.head_up_down_move[self.up_down_step] = 50

                self.left_hand_randomize_spawn = 600
                self.right_hand_randomize_spawn = 600
        
                self.attack_state = "attack1"

                self.head_fire_select = 1       # - no
                self.left_fire_select = 0       # - yes
                self.right_fire_select = 0      # - yes
            
            if self.level.gui.boss_timer < 320: # follow idle

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                # transition
                self.head_fire_select = 1       # - no
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no

                # zombie go right
                self.level.zombie.stop_moving = "no"
                self.level.zombie.new_location = "right"
            
            if self.level.gui.boss_timer < 315: # follow attack all

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                self.head_randomize_spawn = 100

                # already fast enough normal/evil zone
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 0       # - yes
                self.right_fire_select = 0      # - yes

                self.level.zombie.stop_moving = "yes"
            
            if self.level.gui.boss_timer < 300: # follow attack left

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                if self.level.player.evil_zone > 3:
                    self.head_randomize_spawn = 150
                else:
                    self.head_randomize_spawn = 125
    
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 0       # - yes
                self.right_fire_select = 1      # - no

            
            if self.level.gui.boss_timer < 270: # follow attack right

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                if self.level.player.evil_zone > 3:
                    self.head_randomize_spawn = 175
                else:
                    self.head_randomize_spawn = 150
    
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 1       # - no
                self.right_fire_select = 0      # - yes
            
            if self.level.gui.boss_timer < 250: # follow attack left

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                if self.level.player.evil_zone > 3:
                    self.head_randomize_spawn = 190
                else:
                    self.head_randomize_spawn = 175
    
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 0       # - yes
                self.right_fire_select = 1      # - no
            
            if self.level.gui.boss_timer < 230: # follow attack right

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                if self.level.player.evil_zone > 3:
                    self.head_randomize_spawn = 225
                else:
                    self.head_randomize_spawn = 200
    
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 1       # - no
                self.right_fire_select = 0      # - yes
            
            if self.level.gui.boss_timer < 210: # follow attack left

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                if self.level.player.evil_zone > 3:
                    self.head_randomize_spawn = 250
                else:
                    self.head_randomize_spawn = 225
    
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 0       # - yes
                self.right_fire_select = 1      # - no
            
            if self.level.gui.boss_timer < 190: # follow attack right

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                if self.level.player.evil_zone > 3:
                    self.head_randomize_spawn = 275
                else:
                    self.head_randomize_spawn = 250
    
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 1       # - no
                self.right_fire_select = 0      # - yes
            
            if self.level.gui.boss_timer < 170: # follow attack left

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                if self.level.player.evil_zone > 3:
                    self.head_randomize_spawn = 290
                else:
                    self.head_randomize_spawn = 275
    
                self.head_fire_select = 0       # - yes
                self.left_fire_select = 0       # - yes
                self.right_fire_select = 1      # - no
            
            if self.level.gui.boss_timer < 150: # follow idle 

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                # transition
    
                self.head_fire_select = 1       # - no
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no

                # zombie go left
                self.level.zombie.stop_moving = "no"
                self.level.zombie.new_location = "left"
            
            if self.level.gui.boss_timer < 120: # transition 2

                if self.camera_shake_timer > 0:
                    self.camera_shake_timer -= 1 * dt
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 1)

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "transition2"

                self.level.zombie.stop_moving = "yes"
            
            
            if self.level.gui.boss_timer < 115: # rain

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "rain"

                if self.level.player.evil_zone > 3:
                    self.rain_randomize_spawn = 30
                else:
                    self.rain_randomize_spawn = 20
    
                self.head_fire_select = 1       # - no

                self.rain_oscillation = True
            
            
            if self.level.gui.boss_timer < 15: # follow idle

                self.head_up_down_move[self.up_down_step] = -100

                self.attack_state = "follow"

                # transition
    
                self.head_fire_select = 1       # - no
                self.left_fire_select = 1       # - no
                self.right_fire_select = 1      # - no
            
            if self.level.gui.boss_timer < 5:

                # boss defeated
                self.level.music.fadeout(1000) 

            if self.level.gui.boss_timer == 0: # end
                
                # END THE FIGHT
                if self.level.camera.game_path.in_options.sfx_on_off_state == 0:   
                    self.avoided_sound_timer, self.avoided_sound_counter = self.level.sound.handle_repeat_sound(self.avoided_sound_timer, 8, 10, self.avoided_sound_counter, 3, self.level.sound.avoided_end_fight_sound_path, dt)
    
        # ==============================================================
                          
    def behaviour(self, dt):

        if self.attack_state == "transition2":
            self.camera_shake_timer = 3

        if self.attack_state == "transition2-step2":
            self.camera_shake_timer = 3
        
        # =========================================== HEAD ==========================================================
        if self.upper_body_part == "head":
            """ Moving Head On X Axis """
            self.head_projectile_fire = self.head_fire[self.head_fire_select]

            # boss follows the player
            follow_speed = 1.5

            # stop the head on screen border
            if self.head_pos.x < 0:
                self.head_pos.x = 0
            
            if self.head_pos.x > 85:
                self.head_pos.x = 85

            if self.attack_state == "start":
                self.head_pos.y = -300
                self.left_hand_pos_y = -250
                self.left_hand_rect.y = self.left_hand_pos_y

                self.right_hand_pos_y = -250
                self.right_hand_rect.y = self.right_hand_pos_y

                

                
            if self.attack_state == "follow": # ============================================
                self.attack_step = 0
                self.head_movement[self.attack_step] = self.level.player.hitbox.x
        

       

            if self.attack_state == "rain": # ==============================================
                self.head_projectile_fire = self.head_fire[self.head_fire_select]
                self.attack_step = 1

                # head inflated =================================================
                speed = -20

                if self.head_sprite_size[0] >= 85:
                    self.head_size_speed = speed
                
                if self.head_sprite_size[0] <= 80:
                    self.head_size_speed = -speed

                    
                self.head_sprite_size[0] += self.head_size_speed * dt


                if self.head_sprite_size[1] >= 85:
                    self.head_size_speed = speed
                
                if self.head_sprite_size[1] <= 80:
                    self.head_size_speed = -speed

                    
                self.head_sprite_size[1] += self.head_size_speed * dt

                # ==========================================================

                # evil head inflated
                if self.level.player.evil_zone > 3: # evil mode
                    if self.evil_head_sprite_size[0] >= 85:
                        self.head_size_speed = speed
                
                    if self.evil_head_sprite_size[0] <= 80:
                        self.head_size_speed = -speed

                        
                    self.evil_head_sprite_size[0] += self.head_size_speed * dt


                    if self.evil_head_sprite_size[1] >= 85:
                        self.head_size_speed = speed
                    
                    if self.evil_head_sprite_size[1] <= 80:
                        self.head_size_speed = -speed

                        
                    self.evil_head_sprite_size[1] += self.head_size_speed * dt

                # =================================================================
            
                if self.head_pos.x > 80:
                    self.head_movement[self.attack_step] = 0 # -20 * 1.5
                
                elif self.head_pos.x < 20:
                    self.head_movement[self.attack_step] = 100
                
                if 38 < self.head_pos.x < 40:
                    follow_speed = 0

           

            if self.attack_state == "transition2": # ==========================================
                self.head_projectile_fire = self.head_fire[self.head_fire_select]
                self.attack_step = 1

                if self.head_pos.x > 60:
                    self.head_movement[self.attack_step] = 0 # -20 * 1.5
                
                elif self.head_pos.x < 20:
                    self.head_movement[self.attack_step] = 100
                
                if 38 < self.head_pos.x < 40:
                    follow_speed = 0
           


            if self.attack_state == "transition2-step1": # ==========================================
                self.head_projectile_fire = self.head_fire[self.head_fire_select]
                self.attack_step = 1

                if self.head_pos.x > 80:
                    self.head_movement[self.attack_step] = 0 # -20 * 1.5
                
                elif self.head_pos.x < 20:
                    self.head_movement[self.attack_step] = 100
                
                if 38 < self.head_pos.x < 40:
                    follow_speed = 0

                


            if self.attack_state == "transition2-step2": # ==========================================
                self.head_projectile_fire = self.head_fire[self.head_fire_select]
                self.attack_step = 1

                if self.head_pos.x > 80:
                    self.head_movement[self.attack_step] = 0 # -20 * 1.5
                
                elif self.head_pos.x < 20:
                    self.head_movement[self.attack_step] = 100
                
                if 38 < self.head_pos.x < 40:
                    follow_speed = 0
     
           


            if self.attack_state == "attack1": # ===========================================
                self.head_projectile_fire = self.head_fire[self.head_fire_select]
                self.attack_step = 1

                if self.head_pos.x > 40:
                    self.head_movement[self.attack_step] = 0 # -20 * 1.5
                
                elif self.head_pos.x < 30:
                    self.head_movement[self.attack_step] = 100
                
                if 38 < self.head_pos.x < 40:
                    follow_speed = 0
                
   
                
            if self.attack_state == "attack2": # ===========================================

                self.head_projectile_fire = self.head_fire[self.head_fire_select]
                self.attack_step = 1

                if self.head_pos.x > 80:
                    self.head_movement[self.attack_step] = 0 # -20 * 1.5
                
                elif self.head_pos.x < 20:
                    self.head_movement[self.attack_step] = 100
                
                               

            if self.attack_state == "attack2-step1": # =========================================
                self.head_projectile_fire = self.head_fire[self.head_fire_select]
                self.attack_step = 1

                if self.head_pos.x > 80:
                    self.head_movement[self.attack_step] = 0 # -20 * 1.5
                
                elif self.head_pos.x < 20:
                    self.head_movement[self.attack_step] = 100
                
                if 38 < self.head_pos.x < 40:
                    follow_speed = 0
                if 38 < self.head_pos.x < 40:
                    follow_speed = 0
                
   
            
            if self.attack_state == "attack2-step2-left": # ==========================================
                self.head_projectile_fire = self.head_fire[self.head_fire_select]
                self.attack_step = 1

                self.head_movement[self.attack_step] = -100

                if self.head_pos.x < 5:
                    follow_speed = 0
                
          


            if self.attack_state == "attack2-step2-right": # ==========================================
                self.head_projectile_fire = self.head_fire[self.head_fire_select]
                self.attack_step = 1

                self.head_movement[self.attack_step] = 100

                if self.head_pos.x > 130:
                    follow_speed = 0
            
        
            
            # MOVING ON X AXIS
            self.head_pos.x += (self.head_movement[self.attack_step] - self.head_pos.x - 20) * follow_speed * dt
            self.rect.x = round(self.head_pos.x)


            # MOVING ON Y AXIS
            self.head_pos.y += self.head_up_down_move[self.up_down_step] * dt
            self.rect.y = round(self.head_pos.y)

            
                
            if self.level.gui.boss_timer >= 1000:
                """ Moving Head On Y Axis """
                if self.head_pos.y >= -42:
                    self.head_pos.y = -42
            
            if self.level.gui.boss_timer <= 999:
                """ Moving Head On Y Axis """
                
                if self.head_pos.y < -40: # -40
                    self.head_pos.y = -40
                
                if self.head_pos.y > -30:
                    self.head_pos.y = -30
        
        # =========================================== LEFT HAND =====================================================
        if self.left_body_part == "left_hand":
            """ Moving Left Hand """
            # on x axis
            if self.attack_state == "follow": # =========================================================
                
                self.left_hand_projectile_fire = self.left_hand_fire[self.left_fire_select]
                self.follow_player_left_hand = 1.5
                self.left_hand_movement[self.left_hand_speed_selector] = self.level.player.hitbox.x
                self.move_x_left_hand = 40

                # location limitation on y axis
                if self.left_hand_pos_y > 10:
                    self.left_hand_pos_y = 10

                self.left_hand_pos_y += 75 * dt
                self.left_hand_rect.y = self.left_hand_pos_y

                self.left_hand_pos.x += (self.left_hand_movement[self.left_hand_speed_selector] - self.left_hand_pos.x - self.move_x_left_hand) * self.follow_player_left_hand * dt
                self.left_hand_rect.x = round(self.left_hand_pos.x)


            if self.attack_state == "transition2": # ==========================================

                self.left_hand_speed_selector = 1

                if self.left_hand_pos_x > 80:
                    self.left_hand_movement[self.left_hand_speed_selector] = 0 # -20 * 1.5
                
                elif self.left_hand_pos_x < 20:
                    self.left_hand_movement[self.left_hand_speed_selector] = 100
                
                if 38 < self.left_hand_pos_x < 40:
                    self.follow_player_left_hand = 0
          
                self.left_hand_pos.x += (self.left_hand_movement[self.left_hand_speed_selector] - self.left_hand_pos.x - self.move_x_left_hand) * self.follow_player_left_hand * dt
                self.left_hand_rect.x = round(self.left_hand_pos.x)


            if self.attack_state == "attack1": # ==========================================================
                self.left_hand_projectile_fire = self.left_hand_fire[self.left_fire_select]

                if self.left_hand_pos.x < 0:
                    self.left_hand_speed = 250

                if self.left_hand_pos.x > 140:
                    self.left_hand_speed = -250

                # hand movement
                self.left_hand_pos.x += self.left_hand_speed * dt
                self.left_hand_rect.x = round(self.left_hand_pos.x)
               

            if self.attack_state == "attack2-step1":
                # on y axis
                # left hand bullet ====================================================
                follow_player = 7
                if self.left_hand_bullet_pos_y > 110: # on floor aim player body
                    self.left_hand_bullet_pos_y = 110

                # follow player
                self.left_hand_bullet_pos_y += (self.level.player.hitbox.y - self.left_hand_bullet_img_rect.y - 6) * follow_player * dt
                self.left_hand_bullet_img_rect.y = self.left_hand_bullet_pos_y

            
            if self.attack_state == "attack2-step2-left":
                # on y axis
                if self.left_hand_bullet_pos_y < 60: # in air player's max jump height
                    self.attack2_speed_select = 0
                
                if self.left_hand_bullet_pos_y > 115: # on floor aim player body
                    self.attack2_speed_select = 1

                self.left_hand_bullet_pos_y -= self.attack2_speed[self.attack2_speed_select] * dt
                self.left_hand_bullet_img_rect.y = self.left_hand_bullet_pos_y


            if self.attack_state == "transition2-step1": # on screen
                
                # on x axis
                if self.left_hand_bullet_pos_x >= 4:
                    self.left_hand_bullet_pos_x = 4
                
                
                self.left_hand_bullet_pos_x += 80 * dt
                self.left_hand_bullet_img_rect.x = self.left_hand_bullet_pos_x
            
            else:
                if self.attack_state == "transition2-step2": # out of screen

                    if self.left_hand_bullet_pos_x < -50:
                        self.left_hand_bullet_pos_x = -50

                    self.left_hand_bullet_pos_x -= 30 * dt
                    self.left_hand_bullet_img_rect.x = self.left_hand_bullet_pos_x

            """ STOP SCREEN BORDER """ 
            # stop left hand on screen border =================
            if self.left_hand_rect.x <= 0:
                self.left_hand_rect.x = 0
            
            if self.left_hand_rect.x >= 141:
                self.left_hand_rect.x = 141
            
            """ SPAWN PARTICLES LEFT HAND BULLET """
            self.left_hand_bullet_particle(self.left_hand_bullet_img_rect.x + randint(-2, 2), self.left_hand_bullet_img_rect.y + randint(0, 12), dt)

            """ LEFT HAND BULLET COLLISION WITH PLAYER """
            if self.level.player.avoid_projectile == False:
                if self.left_hand_bullet_img_rect.colliderect(self.level.player.rect): 
                    # kill the player instantly
                    if self.left_hand_bullet_img_rect.x >= 4:
                        self.level.gui.life_unit = 0
            
        # =========================================== RIGHT HAND =====================================================
        if self.right_body_part == "right_hand":
            """ Moving Right Hand """
            if self.attack_state == "follow": # ========================================
                self.right_hand_projectile_fire = self.right_hand_fire[self.right_fire_select]
                self.follow_player_right_hand = 1.5
                self.attack_step = 0
                self.right_hand_movement[self.attack_step] = self.level.player.hitbox.x
                self.move_x_right_hand = 60

                # location limitation on y axis
                if self.right_hand_pos_y > 10:
                    self.right_hand_pos_y = 10

                self.right_hand_pos_y += 75 * dt
                self.right_hand_rect.y = self.right_hand_pos_y
            

            if self.attack_state == "transition2": # ==========================================

                self.attack_step = 1

                if self.right_hand_pos_x > 80:
                    self.right_hand_movement[self.attack_step] = 0 # -20 * 1.5
                
                elif self.right_hand_pos_x < 20:
                    self.right_hand_movement[self.attack_step] = 100
                
                if 38 < self.right_hand_pos_x < 40:
                    follow_speed = 0


            if self.attack_state == "attack1": # =========================================
                self.right_hand_projectile_fire = self.right_hand_fire[self.right_fire_select]
                self.follow_player_right_hand = 1.5
                self.attack_step = 1
                self.move_x_right_hand = -10

                if self.right_hand_pos.x < 5:
                    self.right_hand_movement[self.attack_step] = 200

                if self.right_hand_pos.x > 140:
                    self.right_hand_movement[self.attack_step] = -60


            if self.attack_state == "attack2-step1": # =========================================

                # right hand bullet ===================================================
                follow_player = 7
                # on y axis
                if self.right_hand_bullet_pos_y < 80: # in air player's max jump height
                    self.right_hand_bullet_pos_y = 80
                
                if self.right_hand_bullet_pos_y > 110: # on floor aim player body
                    self.right_hand_bullet_pos_y = 110

                # follow player
                self.right_hand_bullet_pos_y += (self.level.player.hitbox.y - self.right_hand_bullet_img_rect.y - 6) * follow_player * dt
                self.right_hand_bullet_img_rect.y = self.right_hand_bullet_pos_y


            if self.attack_state == "attack2-step2-right":
                # on y axis
                if self.right_hand_bullet_pos_y < 60: # in air player's max jump height
                    self.attack2_speed_select = 1
                
                if self.right_hand_bullet_pos_y > 115: # on floor aim player body
                    self.attack2_speed_select = 0

                self.right_hand_bullet_pos_y += self.attack2_speed[self.attack2_speed_select] * dt
                self.right_hand_bullet_img_rect.y = self.right_hand_bullet_pos_y


            if self.attack_state == "transition2-step1":
                # on x axis
                if self.right_hand_bullet_pos_x <= 124:
                    self.right_hand_bullet_pos_x = 124
                
                
                self.right_hand_bullet_pos_x -= 80 * dt
                self.right_hand_bullet_img_rect.x = self.right_hand_bullet_pos_x

            else:
                if self.attack_state == "transition2-step2":

                    if self.right_hand_bullet_pos_x > 180:
                        self.right_hand_bullet_pos_x = 180

                    self.right_hand_bullet_pos_x += 30 * dt
                    self.right_hand_bullet_img_rect.x = self.right_hand_bullet_pos_x


            # hands cross bullet X movement
            self.right_hand_pos.x += (self.right_hand_movement[self.attack_step] - self.right_hand_pos.x + self.move_x_right_hand) * self.follow_player_right_hand * dt
            self.right_hand_rect.x = round(self.right_hand_pos.x)
        
            """ STOP SCREEN BORDER """ 
            # stop right hand on screen border
            if self.right_hand_rect.x <= 0:
                self.right_hand_rect.x = 0

            if self.right_hand_rect.x >= 141:
                self.right_hand_rect.x = 141
            
            """ SPAWN PARTICLES RIGHT HAND BULLET """
            self.right_hand_bullet_particle(self.right_hand_bullet_img_rect.x + 28 + randint(-2, 2), self.right_hand_bullet_img_rect.y + randint(0, 12), dt)

            """ RIGHT HAND BULLET COLLISION WITH PLAYER """
            if self.level.player.avoid_projectile == False:
                if self.right_hand_bullet_img_rect.colliderect(self.level.player.rect): 
                    # kill the player instantly
                    if self.right_hand_bullet_img_rect.x <= 123:
                        self.level.gui.life_unit = 0

         
        # ===================================== TRANSITIONS TO SECOND ATTACK ==============================================
        # follow player and first attack disabled ===================

        if self.attack_state == "transition2":

            # left hand
            if self.left_hand_pos_y <= -55:
                self.left_hand_pos_y = -55

            self.left_hand_pos_y -= 30 * dt
            self.left_hand_rect.y = self.left_hand_pos_y

            # right hand 
            if self.right_hand_pos_y <= -55:
                self.right_hand_pos_y = -55

            self.right_hand_pos_y -= 30 * dt
            self.right_hand_rect.y = self.right_hand_pos_y


    def head_projectile_physics(self, dt): # ========================== HEAD =====================================

        # handle bullet locations
        for bullet in self.head_normal_projectile_sprite:

            # spawn particles
            self.spawn_demon_bullet_particle(bullet.x + randint(1, 10), bullet.y, dt)
            
            # play animation
            if bullet.y >= 60:
                bullet.demon_frame = 1
            else:
                bullet.demon_frame = 0

            if bullet.demon_frame >= len(bullet.demon_bullet_list):
                bullet.demon_frame = 0
            
            bullet.demon_bullet_image = bullet.demon_bullet_list[int(bullet.demon_frame)]


            # movement
            demon_bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.image.get_width(), bullet.image.get_height())

            bullet.x -= bullet.dx * dt
            bullet.y -= bullet.dy * dt
            


            """ INTERACTION WITH PLAYER AND GUI """
            if self.level.player.avoid_projectile == False:
                    
                if self.level.player.hitbox.colliderect(demon_bullet_rect):
                    # player can't press pause while collision (avoid game crash)
                    self.level.camera.game_path.in_game.pause_counter = 1

                    self.level.camera.game_path.in_game.flash_img = 1
                    self.head_normal_projectile_sprite.remove(bullet)
                    self.level.gui.life_unit -= 1
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 5)

                    # stop the player's dancing animation and reset healing timer
                    self.level.player.is_dancing = 0
                    self.level.player.healing_timer = 10

                    # reset dance energy counter
                    self.level.player.energy_counter = 0
                    self.level.player.energy_counter_rounded = 0

                    if self.level.player.is_alive == "yes":
                        if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                            self.level.sound.randomized_sound_play(self.level.sound.hurt_sound_list, randint(0, 1))
                  

            # handle bullet collisions with the floor
            for sprite in self.level.layer2_sprites:
                # floor
                collision_distance = 10
                if sprite.entity == "floor":
                    if demon_bullet_rect.colliderect(sprite.rect):
                        # collisions on the floor
                        if abs(demon_bullet_rect.bottom - sprite.rect.top) < collision_distance:

                            # delete bullet if in the list
                            if bullet in self.head_normal_projectile_sprite:
                                self.head_normal_projectile_sprite.remove(bullet)
                            
                            else:
                                if demon_bullet_rect.x < -5 or demon_bullet_rect.x > 161:
                                    self.head_normal_projectile_sprite.remove(bullet)

        # handle spear
        for spear in self.head_spear_projectile_sprite:

            # movement
            spear_rect = pygame.Rect(spear.x, spear.y, spear.image.get_width(), spear.image.get_height())

            spear.x -= spear.dx * dt
            spear.y -= spear.dy * dt

            """ INTERACTION WITH PLAYER AND GUI """
            if self.level.player.avoid_projectile == False:
                    
                if self.level.player.hitbox.colliderect(spear_rect):
                    # player can't press pause while collision (avoid game crash)
                    self.level.camera.game_path.in_game.pause_counter = 1

                    self.level.camera.game_path.in_game.flash_img = 1
                    self.head_spear_projectile_sprite.remove(spear)
                    self.level.gui.life_unit -= 10
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 2)

                    # stop the player's dancing animation and reset healing timer
                    self.level.player.is_dancing = 0
                    self.level.player.healing_timer = 10

                    # reset dance energy counter
                    self.level.player.energy_counter = 0
                    self.level.player.energy_counter_rounded = 0

                    if self.level.player.is_alive == "yes":
                        if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                            self.level.sound.randomized_sound_play(self.level.sound.hurt_sound_list, randint(0, 1))

            # handle bullet collisions with the floor
            for sprite in self.level.layer2_sprites:
                # floor
                collision_distance = 10
                if sprite.entity == "floor":
                    if spear_rect.colliderect(sprite.rect):
                        # collisions on the floor
                        if abs(spear_rect.bottom - sprite.rect.top) < collision_distance:
                            self.level.camera.game_path.in_game.camera_shake(self.level.camera, 3)
                            # delete bullet if in the list
                            if spear in self.head_spear_projectile_sprite:
                                self.head_spear_projectile_sprite.remove(spear)
                            
                            else:
                                if spear_rect.x < -5 or spear_rect.x > 161:
                                    self.head_spear_projectile_sprite.remove(spear)

    def left_hand_projectile_physics(self, dt): # ============================= LEFT HAND =============================

        # handle bullet locations
        for bullet in self.left_cross_projectile_sprite:
            bullet.rect.y += bullet.speed * dt

            # spawn particle
            self.left_cross_bullet_particle(bullet.rect.x + randint(-4, 4), bullet.rect.y, dt)

            """ INTERACTION WITH PLAYER AND GUI """
            if self.level.player.avoid_projectile == False:
                if self.level.player.hitbox.colliderect(bullet):
                    # player can't press pause while collision (avoid game crash)
                    self.level.camera.game_path.in_game.pause_counter = 1

                    self.level.camera.game_path.in_game.flash_img = 1
                    self.left_cross_projectile_sprite.remove(bullet)
                    self.level.gui.life_unit -= 1
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 5)

                    # stop the player's dancing animation and reset healing timer
                    self.level.player.is_dancing = 0
                    self.level.player.healing_timer = 10

                    # reset dance energy counter
                    self.level.player.energy_counter = 0
                    self.level.player.energy_counter_rounded = 0

                    if self.level.player.is_alive == "yes":
                        if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                            self.level.sound.randomized_sound_play(self.level.sound.hurt_sound_list, randint(0, 1))

            # handle cross bullet collisions with the floor
            for sprite in self.level.layer2_sprites:
                # floor
                # delete bullet on Y axis
                if bullet in self.left_cross_projectile_sprite:
                    if bullet.rect.y < 0:
                        self.left_cross_projectile_sprite.remove(bullet)

                collision_distance = 10
                if sprite.entity == "floor":
                    if bullet.rect.colliderect(sprite.rect): 
                        # collisions on the floor
                        if abs(bullet.rect.bottom - sprite.rect.top) < collision_distance:

                            # delete bullet if in the list
                            if bullet in self.left_cross_projectile_sprite:
                                self.left_cross_projectile_sprite.remove(bullet)
                            
        
        # handle normal bullet movement
        for bullet in self.left_hand_normal_bullet_sprite_list:
            bullet.rect.x += bullet.speed * dt

            # spawn bullet particle
            self.spawn_left_bullet_particle(bullet.rect.x, bullet.rect.y + randint(-2, 2), dt)

            """ INTERACTION WITH PLAYER AND GUI """
            if self.level.player.avoid_projectile == False:
                if self.level.player.hitbox.colliderect(bullet):
                    # player can't press pause while collision (avoid game crash)
                    self.level.camera.game_path.in_game.pause_counter = 1

                    self.level.camera.game_path.in_game.flash_img = 1
                    self.left_hand_normal_bullet_sprite_list.remove(bullet)
                    self.level.gui.life_unit -= 1
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 5)

                    # stop the player's dancing animation and reset healing timer
                    self.level.player.is_dancing = 0
                    self.level.player.healing_timer = 10

                    # reset dance energy counter
                    self.level.player.energy_counter = 0
                    self.level.player.energy_counter_rounded = 0

                    if self.level.player.is_alive == "yes":
                        if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                            self.level.sound.randomized_sound_play(self.level.sound.hurt_sound_list, randint(0, 1))

            if bullet.rect.x <= 0 or bullet.rect.x >= self.game_screen_width:
                if bullet in self.left_hand_normal_bullet_sprite_list:
                    self.left_hand_normal_bullet_sprite_list.remove(bullet)


    def right_hand_projectile_physics(self, dt): # ============================= RIGHT HAND ======================

        # handle cross bullet movement
        for bullet in self.right_cross_projectile_sprite:
            bullet.rect.y += bullet.speed * dt

            # spawn particle
            self.right_cross_bullet_particle(bullet.rect.x + randint(-4, 4), bullet.rect.y, dt)

            """ INTERACTION WITH PLAYER AND GUI """
            if self.level.player.avoid_projectile == False:
                if self.level.player.hitbox.colliderect(bullet):
                    # player can't press pause while collision (avoid game crash)
                    self.level.camera.game_path.in_game.pause_counter = 1

                    self.level.camera.game_path.in_game.flash_img = 1
                    self.right_cross_projectile_sprite.remove(bullet)
                    self.level.gui.life_unit -= 1
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 5)

                    # stop the player's dancing animation and reset healing timer
                    self.level.player.is_dancing = 0
                    self.level.player.healing_timer = 10

                    # reset dance energy counter
                    self.level.player.energy_counter = 0
                    self.level.player.energy_counter_rounded = 0

                    if self.level.player.is_alive == "yes":
                        if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                            self.level.sound.randomized_sound_play(self.level.sound.hurt_sound_list, randint(0, 1))
                 
            # handle cross bullet collisions with the floor
            for sprite in self.level.layer2_sprites:
                # floor
                # delete bullet on Y axis
                if bullet in self.right_cross_projectile_sprite:
                    if bullet.rect.y < 0:
                        self.right_cross_projectile_sprite.remove(bullet)

                collision_distance = 10
                if sprite.entity == "floor":
                    if bullet.rect.colliderect(sprite.rect):

                        # coliisions on the floor
                        if abs(bullet.rect.bottom - sprite.rect.top) < collision_distance:

                            # delete cross bullet if in the list
                            if bullet in self.right_cross_projectile_sprite:
                                self.right_cross_projectile_sprite.remove(bullet)
                                

        
        # handle normal bullet movement
        for bullet in self.right_hand_normal_bullet_sprite_list:
            bullet.rect.x -= bullet.speed * dt

            # spawn particles
            self.spawn_right_bullet_particle(bullet.rect.x + 8, bullet.rect.y + randint(-2, 2), dt)

            """ INTERACTION WITH PLAYER AND GUI """
            if self.level.player.avoid_projectile == False:
                if self.level.player.hitbox.colliderect(bullet):
                    # player can't press pause while collision (avoid game crash)
                    self.level.camera.game_path.in_game.pause_counter = 1

                    self.level.camera.game_path.in_game.flash_img = 1
                    self.right_hand_normal_bullet_sprite_list.remove(bullet)
                    self.level.gui.life_unit -= 1
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 5)

                    # stop the player's dancing animation and reset healing timer
                    self.level.player.is_dancing = 0
                    self.level.player.healing_timer = 10

                    # reset dance energy counter
                    self.level.player.energy_counter = 0
                    self.level.player.energy_counter_rounded = 0

                    if self.level.player.is_alive == "yes":
                        if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                            self.level.sound.randomized_sound_play(self.level.sound.hurt_sound_list, randint(0, 1))

            if bullet.rect.x <= 0 or bullet.rect.x >= self.game_screen_width:
                if bullet in self.right_hand_normal_bullet_sprite_list:
                    self.right_hand_normal_bullet_sprite_list.remove(bullet)
       

    def rain_projectile_physics(self, dt): # =============================== RAIN ==================================
        for rain in self.rain_projectile_sprites_list:
            
            rain.angle_speed = 20
            rain.amplitude_x = 160
            rain.offset_x = 50

            if self.rain_oscillation == True:
                self.rain_projectile_angle, rain.dx = math_projectile(self.rain_projectile_angle, rain.angle_speed, rain.amplitude_x, rain.offset_x, dt)

                rain.rect.x += rain.dx * dt

            rain.rect.y += rain.speed * dt

            """ INTERACTION WITH PLAYER AND GUI """
            if self.level.player.avoid_projectile == False:
                if self.level.player.hitbox.colliderect(rain):
                    # player can't press pause while collision (avoid game crash)
                    self.level.camera.game_path.in_game.pause_counter = 1
                    
                    self.level.camera.game_path.in_game.flash_img = 1
                    self.rain_projectile_sprites_list.remove(rain)
                    self.level.gui.life_unit -= 1
                    self.level.camera.game_path.in_game.camera_shake(self.level.camera, 5)

                    # stop the player's dancing animation and reset healing timer
                    self.level.player.is_dancing = 0
                    self.level.player.healing_timer = 10

                    # reset dance energy counter
                    self.level.player.energy_counter = 0
                    self.level.player.energy_counter_rounded = 0

                    if self.level.player.is_alive == "yes":
                        if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                            self.level.sound.randomized_sound_play(self.level.sound.hurt_sound_list, randint(0, 1))

            # handle rain collisions with the floor
            for sprite in self.level.layer2_sprites:
                # floor
                collision_distance = 10
                if sprite.entity == "floor":
                    if rain.rect.colliderect(sprite.rect):

                        # coliisions on the floor
                        if abs(rain.rect.bottom - sprite.rect.top) < collision_distance:
                            self.level.camera.game_path.in_game.camera_shake(self.level.camera, 2)
                            # delete rain if in the list
                            if rain in self.rain_projectile_sprites_list:
                                if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                                    self.level.sound.randomized_sound_play(self.level.sound.rain_sound_list, randint(0, 2))
                                self.rain_projectile_sprites_list.remove(rain)

    def left_hand_bullet_particle(self,x, y, dt):
        # particle 1
        self.left_hand_bullet_particle1_timer += 20 * dt
        my_timer = int(self.left_hand_bullet_particle1_timer)

        if my_timer > 1:
            self.left_hand_bullet_particle1_timer = 0
           
            self.left_hand_bullet_particle1_list.append(Particle(x, y, 1))

    def right_hand_bullet_particle(self,x, y, dt):
        # particle 1
        self.right_hand_bullet_particle1_timer += 20 * dt
        my_timer = int(self.right_hand_bullet_particle1_timer)

        if my_timer > 1:
            self.right_hand_bullet_particle1_timer = 0
           
            self.right_hand_bullet_particle1_list.append(Particle(x, y, 1))

    def spawn_demon_bullet_particle(self,x, y, dt):
        # particle 1
        self.demon_bullet_particle1_timer += 20 * dt
        my_timer = int(self.demon_bullet_particle1_timer)

        if my_timer > 1:
            self.demon_bullet_particle1_timer = 0
           
            self.demon_bullet_particle1_list.append(Particle(x, y, 0))
    
    def left_cross_bullet_particle(self,x, y, dt):
        # particle 1
        self.left_cross_bullet_particle1_timer += 20 * dt
        my_timer = int(self.left_cross_bullet_particle1_timer)

        if my_timer > 1:
            self.left_cross_bullet_particle1_timer = 0
           
            self.left_cross_bullet_particle1_list.append(Particle(x, y, 0))

    def right_cross_bullet_particle(self,x, y, dt):
        # particle 1
        self.right_cross_bullet_particle1_timer += 20 * dt
        my_timer = int(self.right_cross_bullet_particle1_timer)

        if my_timer > 1:
            self.right_cross_bullet_particle1_timer = 0
           
            self.right_cross_bullet_particle1_list.append(Particle(x, y, 0))

    def spawn_left_bullet_particle(self,x, y, dt):
        # particle 1
        self.left_bullet_particle1_timer += 20 * dt
        my_timer = int(self.left_bullet_particle1_timer)

        if my_timer > 1:
            self.left_bullet_particle1_timer = 0
           
            self.left_bullet_particle1_list.append(Particle(x, y, 1))

    def spawn_right_bullet_particle(self,x, y, dt):
        # particle 1
        self.right_bullet_particle1_timer += 20 * dt
        my_timer = int(self.right_bullet_particle1_timer)

        if my_timer > 1:
            self.right_bullet_particle1_timer = 0
           
            self.right_bullet_particle1_list.append(Particle(x, y, 1))
        

    def spawn_particle_left_hand(self, dt):
    # particle 1
        self.left_particle1_timer += 20 * dt
        my_timer = int(self.left_particle1_timer)

        if my_timer > 1:
            self.left_particle1_timer = 0

            x = self.left_hand_rect.x + randint(2, 10)

            y = self.left_hand_rect.y + randint(15, 19)

            self.particle1_list_left_hand.append(Particle(x, y, 0))
    
    # particle 2
        self.left_particle2_timer += 10 * dt
        my_timer2 = int(self.left_particle2_timer)

        if my_timer2 > 1:
            self.left_particle2_timer = 0

            x = self.left_hand_rect.x + randint(2, 8)

            y = self.left_hand_rect.y + 15

            self.particle2_list_left_hand.append(Particle(x, y, 1))

    # particle 3

        self.left_particle3_timer += 20 * dt
        my_timer3 = int(self.left_particle3_timer)

        if  my_timer3 > 1:
            self.left_particle3_timer = 0
           

            x = self.left_hand_rect.x + randint(2, 8)

            y = self.left_hand_rect.y + 15

            self.particle3_list_left_hand.append(Particle(x, y, 2)) 
    
    # particle right head cross bullet  
        if self.attack_state == "attack1":
            self.particle1_list_left_hand_cross_bullet_timer += 10 * dt
            my_timer4 = int(self.particle1_list_left_hand_cross_bullet_timer)

            if my_timer4 > 1:
                self.particle1_list_left_hand_cross_bullet_timer = 0

                x = self.left_hand_rect.x
                y = self.left_hand_rect.y

                self.particle1_list_left_hand_cross_bullet_list.append(Particle(x, y, 4))


    def spawn_particle_right_hand(self, dt):
        # particle 1
        self.right_particle1_timer += 20 * dt
        my_timer = int(self.right_particle1_timer)

        if my_timer > 1:
            self.right_particle1_timer = 0

            x = self.right_hand_rect.x + randint(-2, 10)

            y = self.right_hand_rect.y + randint(15, 19)

            self.particle1_list_right_hand.append(Particle(x, y, 0))
    
        # particle 2
        self.right_particle2_timer += 10 * dt
        my_timer2 = int(self.right_particle2_timer)

        if my_timer2 > 1:
            self.right_particle2_timer = 0

            x = self.right_hand_rect.x + randint(0, 8)

            y = self.right_hand_rect.y + 15

            self.particle2_list_right_hand.append(Particle(x, y, 1))

        # particle 3
        self.right_particle3_timer += 20 * dt
        my_timer3 = int(self.right_particle3_timer)

        if  my_timer3 > 1:
            self.right_particle3_timer = 0
           
            x = self.right_hand_rect.x + randint(0, 6)

            y = self.right_hand_rect.y + 15

            self.particle3_list_right_hand.append(Particle(x, y, 2))  

        # particle right head cross bullet  
        if self.attack_state == "attack1":
            self.particle1_list_right_hand_cross_bullet_timer += 10 * dt
            my_timer4 = int(self.particle1_list_right_hand_cross_bullet_timer)

            if my_timer4 > 1:
                self.particle1_list_right_hand_cross_bullet_timer = 0

                x = self.right_hand_rect.x
                y = self.right_hand_rect.y

                self.particle1_list_right_hand_cross_bullet_list.append(Particle(x, y, 3))

    def left_hand_normal_bullet_particle_physics(self, dt):

        for left_hand_bullet_particle1 in self.left_hand_bullet_particle1_list:
            left_hand_bullet_particle1.rect.y -= 1 * dt

            if left_hand_bullet_particle1.opacity <= 0:
                left_hand_bullet_particle1.opacity = 0
                if left_hand_bullet_particle1 in self.left_bullet_particle1_list:
                        self.left_hand_bullet_particle1_list.remove(left_hand_bullet_particle1)

            left_hand_bullet_particle1.opacity -= 800 * dt

    def right_hand_normal_bullet_particle_physics(self, dt):

        for right_hand_bullet_particle1 in self.right_hand_bullet_particle1_list:
            right_hand_bullet_particle1.rect.y -= 1 * dt

            if right_hand_bullet_particle1.opacity <= 0:
                right_hand_bullet_particle1.opacity = 0
                if right_hand_bullet_particle1 in self.right_bullet_particle1_list:
                        self.right_hand_bullet_particle1_list.remove(right_hand_bullet_particle1)

            right_hand_bullet_particle1.opacity -= 800 * dt

    def demon_bullet_particle_physics(self, dt):

        for bullet_demon_particle1 in self.demon_bullet_particle1_list:
            bullet_demon_particle1.rect.y -= 1 * dt

            if bullet_demon_particle1.opacity <= 0:
                bullet_demon_particle1.opacity = 0
                if bullet_demon_particle1 in self.demon_bullet_particle1_list:
                        self.demon_bullet_particle1_list.remove(bullet_demon_particle1)

            bullet_demon_particle1.opacity -= 500 * dt
    
    def left_cross_bullet_particle_physics(self, dt):

        for left_cross_bullet_particle1 in self.left_cross_bullet_particle1_list:
            left_cross_bullet_particle1.rect.y -= 1 * dt

            if left_cross_bullet_particle1.opacity <= 0:
                left_cross_bullet_particle1.opacity = 0
                if left_cross_bullet_particle1 in self.left_cross_bullet_particle1_list:
                        self.left_cross_bullet_particle1_list.remove(left_cross_bullet_particle1)

            left_cross_bullet_particle1.opacity -= 800 * dt

    def right_cross_bullet_particle_physics(self, dt):

        for right_cross_bullet_particle1 in self.right_cross_bullet_particle1_list:
            right_cross_bullet_particle1.rect.y -= 1 * dt

            if right_cross_bullet_particle1.opacity <= 0:
                right_cross_bullet_particle1.opacity = 0
                if right_cross_bullet_particle1 in self.right_cross_bullet_particle1_list:
                        self.right_cross_bullet_particle1_list.remove(right_cross_bullet_particle1)

            right_cross_bullet_particle1.opacity -= 800 * dt

    def left_bullet_particle_physics(self, dt):

        for left_bullet_particle1 in self.left_bullet_particle1_list:
            # left_bullet_particle1.rect.x -= 0 * dt

            if left_bullet_particle1.opacity <= 0:
                left_bullet_particle1.opacity = 0
                if left_bullet_particle1 in self.left_bullet_particle1_list:
                        self.left_bullet_particle1_list.remove(left_bullet_particle1)

            left_bullet_particle1.opacity -= 800 * dt

    def right_bullet_particle_physics(self, dt):

        for right_bullet_particle1 in self.right_bullet_particle1_list:
            # right_bullet_particle1.rect.x += 1 * dt

            if right_bullet_particle1.opacity <= 0:
                right_bullet_particle1.opacity = 0
                if right_bullet_particle1 in self.right_bullet_particle1_list:
                        self.right_bullet_particle1_list.remove(right_bullet_particle1)

            right_bullet_particle1.opacity -= 800 * dt


    def left_hand_particle_physics(self, dt):
        
        # particle 1
        for particle in self.particle1_list_left_hand:

            particle.rect.y -= 1 * dt
            
            if particle.opacity <= 0 or particle.rect.y < 1:
                particle.opacity = 0

                if particle in self.particle1_list_left_hand:
                    self.particle1_list_left_hand.remove(particle)

            particle.opacity -= 250 * dt
        
        # particle 2
        for particle2 in self.particle2_list_left_hand:

            particle2.rect.y -= 1 * dt

            if particle2.opacity <= 0 or particle2.rect.y < 1:
                particle2.opacity = 0

                if particle2 in self.particle2_list_left_hand:
                    self.particle2_list_left_hand.remove(particle2)

            particle2.opacity -= 250 * dt
        
        # particle 3
        for particle3 in self.particle3_list_left_hand:

            particle3.rect.y -= 1 * dt
            
            if particle3.opacity <= 0 or particle3.rect.y < 1:
                particle3.opacity = 0

                if particle3 in self.particle3_list_left_hand:
                    self.particle3_list_left_hand.remove(particle3)
            
            particle3.opacity -= 250 * dt
        
        # particle 4 - fast speed
        for particle4 in self.particle1_list_left_hand_cross_bullet_list:

            # play animation
            particle4.frame += 2 * dt
            if particle4.frame >= len(particle4.image_list):
                particle4.frame = 0

            particle4.image = particle4.image_list[int(particle4.frame)]

            particle4.image.set_alpha(particle4.opacity)
            particle4.opacity -= 250 * dt
            opacity_rounded = round(particle4.opacity)

            if opacity_rounded <= 0:
                particle4.opacity = 0
                if particle4 in self.particle1_list_left_hand_cross_bullet_list:
                    self.particle1_list_left_hand_cross_bullet_list.remove(particle4)


    def right_hand_particle_physics(self, dt):
        
        # particle 1
        for particle in self.particle1_list_right_hand:

            particle.rect.y -= 1 * dt
            
            if particle.opacity <= 0 or particle.rect.y < 1:
                particle.opacity = 0

                if particle in self.particle1_list_right_hand:
                    self.particle1_list_right_hand.remove(particle)

            particle.opacity -= 250 * dt
        
        # particle 2
        for particle2 in self.particle2_list_right_hand:

            particle2.rect.y -= 1 * dt

            if particle2.opacity <= 0 or particle2.rect.y < 1:
                particle2.opacity = 0

                if particle2 in self.particle2_list_right_hand:
                    self.particle2_list_right_hand.remove(particle2)

            particle2.opacity -= 250 * dt
        
        # particle 3
        for particle3 in self.particle3_list_right_hand:

            particle3.rect.y -= 1 * dt
            
            if particle3.opacity <= 0 or particle3.rect.y < 1:
                particle3.opacity = 0

                if particle3 in self.particle3_list_right_hand:
                    self.particle3_list_right_hand.remove(particle3)
            
            particle3.opacity -= 250 * dt
        
        # particle 4 - fast speed
        for particle4 in self.particle1_list_right_hand_cross_bullet_list:

            # play animation
            particle4.frame += 2 * dt
            if particle4.frame >= len(particle4.image_list):
                particle4.frame = 0

            particle4.image = particle4.image_list[int(particle4.frame)]

            particle4.image.set_alpha(particle4.opacity)
            particle4.opacity -= 250 * dt
            opacity_rounded = round(particle4.opacity)

            if opacity_rounded <= 0:
                particle4.opacity = 0
                if particle4 in self.particle1_list_right_hand_cross_bullet_list:
                    self.particle1_list_right_hand_cross_bullet_list.remove(particle4)

         
    def handle_animations(self, dt):

        """ NORMAL MODE """
        # head animations
        self.head_frame += 12 * dt
        if self.head_frame >= len(self.head_sprite_list):
            self.head_frame = 0
        
        self.image = pygame.transform.scale(self.head_sprite_list[int(self.head_frame)], self.head_sprite_size)

        # left hand animations
        self.left_hand_frame += 12 * dt
        if self.left_hand_frame >= len(self.left_hand_sprite_list):
            self.left_hand_frame = 0

        self.left_hand_img = self.left_hand_sprite_list[int(self.left_hand_frame)] 

        # left hand bullet animations
        if self.left_hand_normal_bullet_timer > 1:
            self.left_hand_bullet_frame = 1
        else:
            if self.left_hand_normal_bullet_timer < 1:
                self.left_hand_bullet_frame = 0


        if self.left_hand_bullet_frame >= len(self.left_hand_bullet_sprite_list):
            self.left_hand_bullet_frame = 0
        
        self.left_hand_bullet_img = self.left_hand_bullet_sprite_list[int(self.left_hand_bullet_frame)]

        # right hand animations
        self.right_hand_frame += 12 * dt
        if self.right_hand_frame >= len(self.right_hand_sprite_list):
            self.right_hand_frame = 0

        self.right_hand_img = self.right_hand_sprite_list[int(self.right_hand_frame)] 

        # right hand bullet animations
        if self.right_hand_normal_bullet_timer > 1:
            self.right_hand_bullet_frame = 1
        else:
            if self.right_hand_normal_bullet_timer < 1:
                self.right_hand_bullet_frame = 0

        if self.right_hand_bullet_frame >= len(self.right_hand_bullet_sprite_list):
            self.right_hand_bullet_frame = 0
        
        self.right_hand_bullet_img = self.right_hand_bullet_sprite_list[int(self.right_hand_bullet_frame)]

        """ EVIL MODE """
        if self.level.player.evil_zone > 3:
            # evil head animations
            self.evil_head_frame += 12 * dt
            if self.evil_head_frame >= len(self.evil_head_sprite_list):
                self.evil_head_frame = 0
            
            self.image = pygame.transform.scale(self.evil_head_sprite_list[int(self.evil_head_frame)], self.evil_head_sprite_size)

            # evil left hand animations
            self.evil_left_hand_frame += 12 * dt
            if self.evil_left_hand_frame >= len(self.evil_left_hand_sprite_list):
                self.evil_left_hand_frame = 0
            
            self.left_hand_img = self.evil_left_hand_sprite_list[int(self.evil_left_hand_frame)] 

            # evil left hand bullet animations
            if self.left_hand_normal_bullet_timer > 1:
                self.evil_left_hand_bullet_frame = 1
            else:
                if self.left_hand_normal_bullet_timer < 1:
                    self.evil_left_hand_bullet_frame = 0


            if self.evil_left_hand_bullet_frame >= len(self.evil_left_hand_bullet_sprite_list):
                self.evil_left_hand_bullet_frame = 0
            
            self.left_hand_bullet_img = self.evil_left_hand_bullet_sprite_list[int(self.evil_left_hand_bullet_frame)]

            # evil right hand animations
            self.evil_right_hand_frame += 12 * dt
            if self.evil_right_hand_frame >= len(self.evil_right_hand_sprite_list):
                self.evil_right_hand_frame = 0
            
            self.right_hand_img = self.evil_right_hand_sprite_list[int(self.evil_right_hand_frame)] 

            # evil right hand bullet animations
            if self.right_hand_normal_bullet_timer > 1:
                self.evil_right_hand_bullet_frame = 1
            else:
                if self.right_hand_normal_bullet_timer < 1:
                    self.evil_right_hand_bullet_frame = 0


            if self.evil_right_hand_bullet_frame >= len(self.evil_right_hand_bullet_sprite_list):
                self.evil_right_hand_bullet_frame = 0
            
            self.right_hand_bullet_img = self.evil_right_hand_bullet_sprite_list[int(self.evil_right_hand_bullet_frame)]


    def update(self, dt):

        # SPAWNING SYSTEM
        self.spawn_projectile(dt)

        self.spawn_particle_left_hand(dt)
        self.spawn_particle_right_hand(dt)


        # PARTICLES PHYSICS
        self.demon_bullet_particle_physics(dt)

        self.left_hand_particle_physics(dt)
        self.right_hand_particle_physics(dt)

        self.left_hand_normal_bullet_particle_physics(dt)
        self.right_hand_normal_bullet_particle_physics(dt)

        self.left_cross_bullet_particle_physics(dt)
        self.right_cross_bullet_particle_physics(dt)

        self.left_bullet_particle_physics(dt)
        self.right_bullet_particle_physics(dt)
        
        # PROJECTILES PHYSICS
        self.head_projectile_physics(dt)
        self.left_hand_projectile_physics(dt)
        self.right_hand_projectile_physics(dt)
        self.rain_projectile_physics(dt)

        # BEHAVIOUR MECHANICS
        self.combat_state(dt)
        self.behaviour(dt)

        # ANIMATIONS
        self.handle_animations(dt)

    
    