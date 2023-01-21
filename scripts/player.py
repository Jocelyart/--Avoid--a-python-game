import pygame

from random import randint

from sound import Sound

from particle import handle_particle_update

class Player:

    def __init__(self, x, y, level):
        self.level = level
        self.sound = Sound()

        self.width = 16
        self.height = 32
        self.flip = False
        self.idle_frame = 0
        self.running_frame = 0
        self.jumping_frame = 0
        self.rolling_frame = 0
        self.crouching_frame = 0
        self.death_frame = 0
        self.dancing_frame = 0
        
        # player state machine
        self.is_idle = 0
        self.is_running = 0
        self.is_jumping = 0
        self.is_rolling = 0
        self.is_crouching = 0
        self.is_dead = 0
        self.is_dancing = 0
        self.is_alive = "yes"

        # hitboxes*
        self.handle_hitboxes(x, y)
        
        self.handle_sprites()

        self.image = self.idle_sprite_list[self.idle_frame]
        self.rect = self.image.get_rect(midbottom = (x, y - 5)) # -5 player pops on floor


        self.select_hitbox = 0
        self.hitbox = self.hitbox_list[self.select_hitbox]
        self.rect = self.hitbox

      
        self.hitbox_inflate_x = 0
        self.hitbox_inflate_y = 0

        self.direction = pygame.Vector2()
        self.speed = 90 # min 32
        self.gravity = 0
        self.gravity_value = 1200
        self.jumpforce = -200


        self.is_l_key_pressed = False
        self.l_key = "on"

        self.left_key = "on"
        self.right_key = "on"

        self.avoid_projectile = False

        self.rolling_boost = 0
        self.start_rolling_boost = False
        self.rolling_speed_index = 0
        self.rolling_speed = [-600, 600]
        self.rolling_counter = 0
        self.rolling_cooldown = 0

        self.active_stamina_bar = False
        self.stamina_width = 0
        self.stamina_rounded = 0
        self.stamina_cooldown = 0
        self.stamina_cooldown_rounded = 0
        self.stamina_counter_speed = -45
        self.stamina_bar_timer = 0

        self.visible_hitbox = "no"
        self.death_sound_timer = 10
        self.death_sound_counter = 0

        self.boss1_sound_timer = 10
        self.boss1_sound_counter = 0

        self.evil_boss1_piss_me_off_sound_timer = 10
        self.evil_boss1_piss_me_off_sound_counter = 0

        self.evil_boss1_what_sound_timer = 10
        self.evil_boss1_what_sound_counter = 0

        self.evil_boss1_stop_that_sound_timer = 10
        self.evil_boss1_stop_that_sound_counter = 0

        self.evil_boss1_i_said_stop_sound_timer = 10
        self.evil_boss1_i_said_stop_sound_counter = 0

        self.run_sound_timer = 0

        self.evil_zone = 0

        # prevent crashing the game when player collide too fast after flame wall appearing
        self.flame_wall_collision_timer = 2

        # right wall flame  (evil zone)
        # particle1
        self.flame_wall_particle1_list = []
        self.flame_wall_particle1_timer = 0

        # particle2
        self.flame_wall_particle2_list = []
        self.flame_wall_particle2_timer = 0

        # particle3
        self.flame_wall_particle3_list = []
        self.flame_wall_particle3_timer = 0

        # left wall flame  (evil zone)
        # particle4
        self.flame_wall_particle4_list = []
        self.flame_wall_particle4_timer = 0

        # particle5
        self.flame_wall_particle5_list = []
        self.flame_wall_particle5_timer = 0

        # particle6
        self.flame_wall_particle6_list = []
        self.flame_wall_particle6_timer = 0

        self.healing_timer = 10
        self.energy_counter = 0
        self.energy_counter_rounded = 0

        self.corner_lover_timer = 30

        self.select_key = 0
        self.key_left_controls = [pygame.K_q, pygame.K_a]
        
        # boss 1 voice you stay in the corners
        self.boss1_voice_stay_corners_timer = 10
        self.boss1_voice_stay_corners_timer_counter = 0

        # boss 1 voice you think you're smart
        self.boss1_voice_smartass_timer = 10
        self.boss1_voice_smartass_timer_counter = 0

        # boss 1 voice Enough! Die!
        self.boss1_voice_enough_die_timer = 10
        self.boss1_voice_enough_die_timer_counter = 0

        # player voice healing yes
        self.voice_healing_yes_timer = 10
        self.voice_healing_yes_timer_counter = 0

        # vfx image
        self.vfx_healing_image_frame = 0
        self.vfx_healing_image = self.vfx_healing_sprite_list[self.vfx_healing_image_frame]
        self.vfx_healing_image_rect = self.vfx_healing_image.get_rect(topleft = (x, y))
        self.run_vfx_healing_animation = "no"

        # thanks for player text
        self.thanks_for_playing_text = pygame.image.load("sprites/thanks_for_playing_text.png").convert_alpha()
        self.thanks_for_playing_text_rect = self.thanks_for_playing_text.get_rect(topleft = (x, y))

        self.thanks_text_opacity = 0
        
        

    def handle_hitboxes(self, x, y):
        # stand
        self.standing_hitbox = pygame.image.load("sprites/player/hitboxes/standing_hitbox.png").convert_alpha()
        self.standing_hitbox_rect = self.standing_hitbox.get_rect(topleft = (x, y - 5))

        # crouch
        self.crouch_hitbox = pygame.image.load("sprites/player/hitboxes/crouch_hitbox.png").convert_alpha()
        self.crouch_hitbox_rect = self.crouch_hitbox.get_rect(topleft = (x, y - 5))

        # death
        self.death_hitbox = pygame.image.load("sprites/player/hitboxes/death_hitbox.png").convert_alpha()
        self.death_hitbox_rect = self.death_hitbox.get_rect(topleft = (x, y - 5))

        self.hitbox_list = [
            self.standing_hitbox_rect,
            self.crouch_hitbox_rect,
            self.death_hitbox_rect,
        ]

    def handle_sprites(self):
        # IDLE
        self.idle_sprite_list = []
        for i in range(3 + 1):
            idle_img = pygame.transform.scale(pygame.image.load(f"sprites/player/idle/{i}.png").convert_alpha(), (self.width, self.height))
            
            self.idle_sprite_list.append(idle_img)

        # RUN
        self.run_sprite_list = []
        for i in range(5 + 1):
            run_img = pygame.transform.scale(pygame.image.load(f"sprites/player/run/{i}.png").convert_alpha(), (self.width, self.height))

            self.run_sprite_list.append(run_img)

        # JUMP
        self.jump_sprite_list = []
        for i in range(1):
            jump_img = pygame.transform.scale(pygame.image.load(f"sprites/player/jump/{i}.png").convert_alpha(), (self.width, self.height))

            self.jump_sprite_list.append(jump_img)

        # ROLL
        self.roll_sprite_list = []
        for i in range(5 + 1):
            roll_img = pygame.transform.scale(pygame.image.load(f"sprites/player/roll/{i}.png").convert_alpha(), (self.width, self.height))

            self.roll_sprite_list.append(roll_img)
        
        # CROUCH
        self.crouch_sprite_list = []
        for i in range(1):
            crouch_img = pygame.transform.scale(pygame.image.load(f"sprites/player/crouch/{i}.png").convert_alpha(), (self.width, self.height))

            self.crouch_sprite_list.append(crouch_img)
        
        # DEATH
        self.death_sprite_list = []
        for i in range(15 + 1):
            death_img = pygame.transform.scale(pygame.image.load(f"sprites/player/death/{i}.png").convert_alpha(), (32, 32))

            self.death_sprite_list.append(death_img)
        
        # DANCE
        self.dance_sprite_list = []
        for i in range(5 + 1):
            dance_img = pygame.transform.scale(pygame.image.load(f"sprites/player/dance/{i}.png").convert_alpha(), (self.width, self.height))

            self.dance_sprite_list.append(dance_img)

        # HEALING VFX
        self.vfx_healing_sprite_list = []
        for i in range(9 + 1):
            vfx_healing_img = pygame.image.load(f"sprites/player/dance/dancing_vfx/{i}.png").convert_alpha()

            self.vfx_healing_sprite_list.append(vfx_healing_img)
            

    def handle_control(self, dt):
        key = pygame.key.get_pressed()

        # GET THE AZERTY OR QWERTY CONTROLS
        if self.level.camera.game_path.in_setup_controls.azerty_controls == True:
            self.select_key = 0
            
        else:
            if self.level.camera.game_path.in_setup_controls.qwerty_controls == True:
                self.select_key = 1
               

        # S Key (CROUCH)
        if key[pygame.K_s] and self.hitbox.y >= 110:
            self.is_crouching = 1
            self.is_idle = 0
            self.is_dancing = 0

            self.select_hitbox = 1
            self.hitbox = self.hitbox_list[self.select_hitbox]

        
        if not key[pygame.K_s]:
            self.is_crouching = 0
            self.select_hitbox = 0
            self.hitbox = self.hitbox_list[self.select_hitbox]
            

        # P KEY (JUMP)
        if key[pygame.K_p] and self.is_jumping == 0 and self.is_rolling == 0:
            self.gravity = self.jumpforce
            self.is_jumping = 1
            self.is_dancing = 0
            if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                self.sound.play("jump_sound")

        # L KEY (ROLL)
        if self.l_key == "on":
            if key[pygame.K_l] and self.is_l_key_pressed == False and self.is_crouching == 0:
                self.is_l_key_pressed = True
                self.is_dancing = 0

                # not hitting by projectile
                self.avoid_projectile = True
                
                self.start_rolling_boost = True

                # stamina bar actived
                self.active_stamina_bar = True
            
            if not key[pygame.K_l] and self.is_l_key_pressed == True:
                self.is_l_key_pressed = False

        # B KEY
        if key[pygame.K_b] and self.is_idle == 1 and self.hitbox.y >= 110:
            self.is_dancing = 1

        # ROLLING
        if self.start_rolling_boost == True and self.hitbox.y >= 110:
            
            # while rolling
            if self.rolling_boost < -250 or self.rolling_boost < 250:
                self.left_key = "off"
                self.right_key = "off"
                self.is_running = 0
                self.is_dancing = 0
                self.is_rolling = 1

                if self.run_sound_timer == 0:
                    self.run_sound_timer = 30
                    if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                        self.sound.play("run_roll_grass_sound")

                # change hitbox
                self.select_hitbox = 1
                self.hitbox = self.hitbox_list[self.select_hitbox]

                # stop player speed
                if self.speed <= 0:
                    self.speed = 0

                self.speed -= round(100 * dt)

            # stop rolling boost
            if self.rolling_boost < -250 or self.rolling_boost > 250:
                self.start_rolling_boost = False
            
                self.left_key = "on"
                self.right_key = "on"

                # reset get hitting by projectile
                self.avoid_projectile = False
                
                # reset boost
                self.rolling_boost = 0
                
                # reactive default player speed
                self.speed = 90

            # player direction rolling
            if self.direction.x < 0 or self.flip == True:
                self.rolling_speed_index = 0

            elif self.direction.x > 0 or self.flip == False:
                self.rolling_speed_index = 1

            
            self.rolling_boost += round(self.rolling_speed[self.rolling_speed_index] * dt)

        
        self.hitbox_list[0].x += round(self.rolling_boost * dt)

        # stamina bar =========================================================================================

        # active the stamina bar timer and stamina cooldown if player pressed L key
        if self.active_stamina_bar == True:
            self.stamina_bar_timer += self.stamina_counter_speed * dt
            self.stamina_rounded = round(self.stamina_bar_timer)
            
            self.stamina_cooldown += 10 * dt
            self.stamina_cooldown_rounded = round(self.stamina_cooldown)
        
        # stop the stamina bar timer and stamina cooldown
        if self.stamina_cooldown_rounded >= 15:
            self.stamina_counter_speed = 0
            self.stamina_cooldown = 0
            self.active_stamina_bar = False


        if self.active_stamina_bar == False:
            self.stamina_cooldown = 0 # reset the stamina cooldown

        # decrease stamina width
        if self.stamina_width >= 20 and self.stamina_cooldown <= 0:
            self.stamina_counter_speed = -45
        
        # increase stamina width
        if self.stamina_width <= 0:
            self.stamina_counter_speed = 20
          

        self.stamina_width = self.level.gui.stamina_bar_size[0] + self.stamina_rounded
        stamina_height = self.level.gui.stamina_bar_size[1]
        self.level.gui.stamina_bar = pygame.transform.scale(pygame.image.load("sprites/gui/stamina_bar.png").convert_alpha(), (self.stamina_width, stamina_height))
     
        # ======================================================================================================

        # ROLLING COOLDOWN
        if self.rolling_boost < -250 or self.rolling_boost > 250:
            self.rolling_counter += round(100 * dt)
        

        if self.rolling_counter >= 1:
            
            self.rolling_cooldown += round(100 * dt)
            self.l_key = "off"
            
        
        if self.rolling_cooldown > 150:
            self.l_key = "on"
            self.rolling_counter = 0
            self.rolling_cooldown = 0
        
        # ====================================

        # handle run sound timer
        if self.run_sound_timer > 0:
            self.run_sound_timer -= 1

        # KEYS MOVEMENT
        if key[self.key_left_controls[self.select_key]] and self.is_crouching == 0:
            if self.left_key == "on":
                self.direction.x = -1
                self.flip = True

                self.is_running = 1
                self.is_idle = 0
                self.is_dancing = 0
                
            
        elif key[pygame.K_d] and self.is_crouching == 0:
            if self.right_key == "on":
                self.direction.x = 1
                self.flip = False

                self.is_running = 1
                self.is_idle = 0  
                self.is_dancing  = 0 
                 

        else:
            self.direction.x = 0

            self.is_idle = 1
            self.is_running = 0
       
       
                   
    def handle_collisions(self, dt):

        self.gravity += self.gravity_value * dt
        self.rect.y += self.gravity * dt
        self.hitbox.y = round(self.rect.y)

        # hitbox
        if self.visible_hitbox == "yes":
            pygame.draw.rect(self.level.camera.display_surface, "green", self.hitbox, 1)

        """ COLLISION ON THE Y AXIS """
        for sprite in self.level.layer2_sprites:
            # floor
            collision_distance = 10
            if sprite.entity == "floor":
                if self.hitbox.colliderect(sprite.rect):

                    # on the floor
                    if abs(self.hitbox.bottom - sprite.rect.top) < collision_distance:
                        self.hitbox.bottom = sprite.rect.top
                        self.gravity = 0
                        self.is_jumping = 0
                        if self.direction.x != 0:
                            if self.run_sound_timer == 0:
                                self.run_sound_timer = 30
                                if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                                    self.sound.play("run_roll_grass_sound")
    
                    # in the air
                    if abs(self.hitbox.top - sprite.rect.bottom) < collision_distance:
                        self.hitbox.top = sprite.rect.bottom
                        self.gravity = 0
                        
        
        """ MOVEMENT ON THE X AXIS """ # =================================================
        if self.is_alive == "yes":
            self.rect.x += round(self.direction.x * self.speed * dt)
            self.hitbox.x = self.rect.x
        # ================================================================================

        """ COLLISION ON THE X AXIS """
        for sprite in self.level.layer2_sprites:

            if sprite.entity == "floor":
                collision_distance = 10
                if self.hitbox.colliderect(sprite.rect):
                    
                    # left collision
                    if abs(self.hitbox.left - sprite.rect.right) < collision_distance:
                        self.hitbox.left = sprite.rect.right

                    # right collision
                    if abs(self.hitbox.right - sprite.rect.left) < collision_distance:
                        self.hitbox.right = sprite.rect.left
        
        # COLLISION WITH FLAME WALL
        if self.evil_zone > 3:
            
            # if self.level.doors.right_door_img_rect.x == 220:
            if self.flame_wall_collision_timer > 0:
                self.flame_wall_collision_timer -= 1 * dt
                flame_wall_timer_rounded = round(self.flame_wall_collision_timer)

                if flame_wall_timer_rounded <= 0:
                    self.flame_wall_collision_timer = 0
                
            # flame wall right
            if self.flame_wall_collision_timer == 0:
                for particle1_r in self.flame_wall_particle1_list:

                    if self.hitbox.colliderect(particle1_r.rect):
                        # player can't press pause while collision (avoid game crash)
                        self.level.camera.game_path.in_game.pause_counter = 1
                        self.level.gui.life_unit = 0
                
                for particle2_r in self.flame_wall_particle2_list:

                    if self.hitbox.colliderect(particle2_r.rect):
                        # player can't press pause while collision (avoid game crash)
                        self.level.camera.game_path.in_game.pause_counter = 1
                        self.level.gui.life_unit = 0
                
                for particle3_r in self.flame_wall_particle3_list:

                    if self.hitbox.colliderect(particle3_r.rect):
                        # player can't press pause while collision (avoid game crash)
                        self.level.camera.game_path.in_game.pause_counter = 1
                        self.level.gui.life_unit = 0
            

            # flame wall left
            if self.flame_wall_collision_timer == 0:
                for particle4_l in self.flame_wall_particle4_list:

                    if self.hitbox.colliderect(particle4_l.rect):
                        # player can't press pause while collision (avoid game crash)
                        self.level.camera.game_path.in_game.pause_counter = 1
                        self.level.gui.life_unit = 0   
            
                for particle5_l in self.flame_wall_particle5_list:

                    if self.hitbox.colliderect(particle5_l.rect):
                        # player can't press pause while collision (avoid game crash)
                        self.level.camera.game_path.in_game.pause_counter = 1
                        self.level.gui.life_unit = 0
            
                for particle6_l in self.flame_wall_particle6_list:

                    if self.hitbox.colliderect(particle6_l.rect):
                        # player can't press pause while collision (avoid game crash)
                        self.level.camera.game_path.in_game.pause_counter = 1
                        self.level.gui.life_unit = 0 
             
    
    def handle_animations(self, dt):

        if self.is_alive == "yes":
            # PLAY ANIMATIONS
            # IDLE
            if self.is_idle == 1:
                self.idle_frame += 8 * dt
                
                if self.idle_frame >= len(self.idle_sprite_list):
                    self.idle_frame = 0

                self.image = self.idle_sprite_list[int(self.idle_frame)]
                
            
            # RUNNING
            if self.is_running == 1:
                self.running_frame += 12 * dt
                
                if self.running_frame >= len(self.run_sprite_list):
                    self.running_frame = 0
                    
                self.image = self.run_sprite_list[int(self.running_frame)]

            # JUMPING
            if self.is_jumping == 1:
                self.jumping_frame += 10 * dt
            
                if self.jumping_frame >= len(self.jump_sprite_list):
                    self.jumping_frame = 0
                    
                self.image = self.jump_sprite_list[int(self.jumping_frame)]
            
            # ROLLING
            if self.is_rolling == 1:
                self.rolling_frame += 12 * dt
                if self.rolling_frame >= len(self.roll_sprite_list):
                    self.rolling_frame = 0  
                    self.is_rolling = 0 # don't loop the animation
            
                
                self.image = self.roll_sprite_list[int(self.rolling_frame)]
            
            # CROUCHING
            if self.is_crouching == 1:
                self.crouching_frame += 10 * dt
            
                if self.crouching_frame >= len(self.crouch_sprite_list):
                    self.crouching_frame = 0
                    
                self.image = self.crouch_sprite_list[int(self.crouching_frame)]
            
            # DANCING
            if self.is_dancing == 1:
                self.dancing_frame += 8 * dt

                if self.dancing_frame >= len(self.dance_sprite_list):
                    self.dancing_frame = 0
                
                self.image = self.dance_sprite_list[int(self.dancing_frame)]
            
            # VFX HEALING EFFECT
            if self.run_vfx_healing_animation == "yes":
                self.vfx_healing_image_frame += 15 * dt

                if self.vfx_healing_image_frame >= len(self.vfx_healing_sprite_list):
                    self.vfx_healing_image_frame = len(self.vfx_healing_sprite_list) - 1
                
                self.vfx_healing_image = self.vfx_healing_sprite_list[int(self.vfx_healing_image_frame)]
            
        
        else:
            if self.is_alive == "no":
                
                # play player death sound
                if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                    self.death_sound_timer, self.death_sound_counter = self.sound.handle_repeat_sound(self.death_sound_timer, 9, 10, self.death_sound_counter, 1, self.sound.death_sound_path, dt)

                # play boss voice
                if self.evil_zone > 3:
                    if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                        self.evil_boss1_piss_me_off_sound_timer, self.evil_boss1_piss_me_off_sound_counter = self.sound.handle_repeat_sound(self.evil_boss1_piss_me_off_sound_timer, 7, 10, self.evil_boss1_piss_me_off_sound_counter, 1, self.sound.evil_boss1_dont_piss_me_off_path, dt)

                else:
                    if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                        self.boss1_sound_timer, self.boss1_sound_counter = self.sound.handle_repeat_sound(self.boss1_sound_timer, 7, 10, self.boss1_sound_counter, 1, self.sound.boss1_you_done_sound_path, dt)

                # play death animation
                if self.is_dead == 1:
                    self.death_frame += 10 * dt
                
                    if self.death_frame >= len(self.death_sprite_list):
                        self.death_frame = len(self.death_sprite_list) - 1 # play once

                    self.image = self.death_sprite_list[int(self.death_frame)]

      
    def warp(self, dt):
        
        # warp / evil zone counter
        if self.hitbox.x > 154:
            self.hitbox.x = 0


            if self.level.gui.boss_timer < 1000:
                if self.avoid_projectile == False:
                    self.evil_zone += 1
        

        
        if self.hitbox.x < 0:
            self.hitbox.x = 154


            if self.level.gui.boss_timer < 1000:
                if self.avoid_projectile == False:
                    self.evil_zone += 1
        
        # print(self.evil_zone)

        # evil boss1 -> what? the boss doesnt understand how the player can do that (warp)
        if self.evil_zone == 1:
            if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                self.evil_boss1_what_sound_timer, self.evil_boss1_what_sound_counter = self.sound.handle_repeat_sound(self.evil_boss1_what_sound_timer, 10, 10, self.evil_boss1_what_sound_counter, 1, self.sound.evil_boss1_what_path, dt)
        
        # evil boss1 -> stop doing that!
        if self.evil_zone == 2:
            if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                self.evil_boss1_stop_that_sound_timer, self.evil_boss1_stop_that_sound_counter = self.sound.handle_repeat_sound(self.evil_boss1_stop_that_sound_timer, 10, 10, self.evil_boss1_stop_that_sound_counter, 1, self.sound.evil_boss1_stop_doing_that_path, dt)
        
        # evil boss1 -> I said stop !
        if self.evil_zone == 3:
            if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                self.evil_boss1_i_said_stop_sound_timer, self.evil_boss1_i_said_stop_sound_counter = self.sound.handle_repeat_sound(self.evil_boss1_i_said_stop_sound_timer, 10, 10, self.evil_boss1_i_said_stop_sound_counter, 1, self.sound.evil_boss1_i_said_stop_path, dt)

    def set_up_flames(self, dt):
        
        if self.evil_zone > 3:
            # right flame wall particules evil zone
            # particle1
            self.flame_wall_particle1_timer, self.flame_wall_particle1_list = handle_particle_update(self.flame_wall_particle1_timer, 20, self.flame_wall_particle1_list, 145 + randint(-2, 2), 122, 2, 500, False, 0, True, -100, dt)

            # particle2
            self.flame_wall_particle2_timer, self.flame_wall_particle2_list = handle_particle_update(self.flame_wall_particle2_timer, 40, self.flame_wall_particle2_list, 145 + randint(-8, 8), 122 + randint(-10, 10), 1, 500, True, randint(-85, 85), True, -120, dt)

            # particle3
            self.flame_wall_particle3_timer, self.flame_wall_particle3_list = handle_particle_update(self.flame_wall_particle3_timer, 20, self.flame_wall_particle3_list, 145 + randint(-8, 8), 122 + randint(-8, 8), 0, 500, True, randint(-100, 100), True, -85, dt)

            # left flame wall particules evil zone
            # particle1
            self.flame_wall_particle4_timer, self.flame_wall_particle4_list = handle_particle_update(self.flame_wall_particle4_timer, 20, self.flame_wall_particle4_list, 5 + randint(-2, 2), 122, 2, 500, False, 0, True, -100, dt)

            # particle2
            self.flame_wall_particle5_timer, self.flame_wall_particle5_list = handle_particle_update(self.flame_wall_particle5_timer, 40, self.flame_wall_particle5_list, 5 + randint(-8, 8), 122 + randint(-10, 10), 1, 500, True, randint(-85, 85), True, -120, dt)

            # particle3
            self.flame_wall_particle6_timer, self.flame_wall_particle6_list = handle_particle_update(self.flame_wall_particle6_timer, 20, self.flame_wall_particle6_list, 5 + randint(-8, 8), 122 + randint(-8, 8), 0, 500, True, randint(-100, 100), True, -85, dt)

    def healing_system(self, dt):
        if self.is_dancing == 1:

            if self.healing_timer > 0:
                self.healing_timer -= 1 * dt

                healing_timer_rounded = round(self.healing_timer)

                if healing_timer_rounded == 0:
                    self.healing_timer = 10

                    # increase life by one unit
                    if self.level.gui.life_unit <= 9:
                        self.level.gui.life_unit += 1

                    # flash player image
                    self.level.camera.game_path.in_game.flash_img = 1
                    
                    # reset vfx healing frame
                    self.vfx_healing_image_frame = 0

                    # run vfx healing animation
                    self.run_vfx_healing_animation = "yes"

                    # player voice
                    # +1 life unit
                    if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                        self.voice_healing_yes_timer, self.voice_healing_yes_timer_counter = self.sound.handle_repeat_sound(self.voice_healing_yes_timer, 10, 10, self.voice_healing_yes_timer_counter, 1, self.sound.player_voice_healing_yes_path, dt)

                    # reset player voice healing yes
                    self.voice_healing_yes_timer = 10
                    self.voice_healing_yes_timer_counter = 0
                
            if self.energy_counter <= 10:
                self.energy_counter += 1 * dt
                self.energy_counter_rounded = round(self.energy_counter)

                if self.energy_counter_rounded == 10:
                    self.energy_counter = 0
        
    def player_corner_lover(self, dt):
        if ((0 <= self.hitbox.x < 20 and self.direction.x == 0) or (131 <= self.hitbox.x < 160 and self.direction.x == 0)) and self.level.gui.boss_timer < 1000 and self.level.gui.boss_timer != 0:

            if self.corner_lover_timer > 0:
                self.corner_lover_timer -= 2 * dt
                corner_lover_timer_rounded = round(self.corner_lover_timer)
                
                if corner_lover_timer_rounded == 20:

                    if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                    
                        self.boss1_voice_stay_corners_timer, self.boss1_voice_stay_corners_timer_counter = self.sound.handle_repeat_sound(self.boss1_voice_stay_corners_timer, 10, 10, self.boss1_voice_stay_corners_timer_counter, 1, self.sound.boss1_stay_in_corners_path, dt)
                    
                
                if corner_lover_timer_rounded == 10:
                    
                    if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                    
                        self.boss1_voice_smartass_timer, self.boss1_voice_smartass_timer_counter = self.sound.handle_repeat_sound(self.boss1_voice_smartass_timer, 10, 10, self.boss1_voice_smartass_timer_counter, 1, self.sound.boss1_smartass_path, dt)


                if corner_lover_timer_rounded == 0:
                    self.corner_lover_timer = 0  

                    if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                    
                        self.boss1_voice_enough_die_timer, self.boss1_voice_enough_die_timer_counter = self.sound.handle_repeat_sound(self.boss1_voice_enough_die_timer, 10, 10, self.boss1_voice_enough_die_timer_counter, 1, self.sound.boss1_enough_die_path, dt)
    
    def thanks_text_update(self, dt):
        if self.level.gui.boss_timer == 0:
            if self.thanks_text_opacity <= 255:
                self.thanks_text_opacity += 100 * dt

    def update(self, dt):

        if self.level.gui.life_number == 0:
            self.is_alive = "no"
            self.is_dead = 1
            self.select_hitbox = 2
            self.hitbox = self.hitbox_list[self.select_hitbox]
        
        if self.is_alive == "yes":
            self.handle_control(dt)

        self.handle_collisions(dt)
        self.handle_animations(dt)
        self.warp(dt)
        self.set_up_flames(dt)
        self.healing_system(dt)
        self.player_corner_lover(dt)
        self.thanks_text_update(dt)
  