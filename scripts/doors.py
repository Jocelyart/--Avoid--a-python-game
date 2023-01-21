import pygame


class Door_B1:
    
    def __init__(self, camera, level):

        self.camera = camera
        self.level = level

        self.left_door_img = pygame.image.load("sprites/doors/boss1_left_door.png").convert_alpha()
        self.left_door_img_rect = self.left_door_img.get_rect(topleft = (0, 0))

        self.right_door_img = pygame.image.load("sprites/doors/boss1_right_door.png").convert_alpha()
        self.right_door_img_rect = self.right_door_img.get_rect(topleft = (80, 0))

        self.left_door_direction = pygame.math.Vector2()
        self.left_door_speed = 150

        self.right_door_direction = pygame.math.Vector2()
        self.right_door_speed = 150

        self.open_doors_delay = 10
        self.open_doors_delay_evil_zone = 5

        self.doors_sound_timer = 10
        self.doors_sound_timer_counter = 0
    

    def clean_the_evil_zone(self):

        # reset player location
        self.level.player.hitbox.x = 64
        self.level.player.hitbox.y = 113

        # clear demon bullet list
        self.level.boss1.head_normal_projectile_sprite.clear()

        # clear left cross bullet list
        self.level.boss1.left_cross_projectile_sprite.clear()

        # clear right cross bullet list
        self.level.boss1.right_cross_projectile_sprite.clear()

        # clear left normal bullet list
        self.level.boss1.left_hand_normal_bullet_sprite_list.clear()

        # clear right normal bullet list
        self.level.boss1.right_hand_normal_bullet_sprite_list.clear()
        
        # clear rain list
        self.level.boss1.rain_projectile_sprites_list.clear()

        # reset particles
        self.level.boss1.particle1_list_left_hand.clear()
        self.level.boss1.particle2_list_left_hand.clear()
        self.level.boss1.particle3_list_left_hand.clear()

        self.level.boss1.particle1_list_right_hand.clear()
        self.level.boss1.particle2_list_right_hand.clear()
        self.level.boss1.particle3_list_right_hand.clear()

        self.level.boss1.demon_bullet_particle1_list.clear()

        self.level.boss1.head_normal_projectile_sprite.clear()
        self.level.boss1.left_cross_projectile_sprite.clear()
        self.level.boss1.right_cross_projectile_sprite.clear()

        self.level.boss1.left_cross_bullet_particle1_list.clear()
        self.level.boss1.right_cross_bullet_particle1_list.clear()

        self.level.boss1.left_hand_bullet_particle1_list.clear()
        self.level.boss1.right_hand_bullet_particle1_list.clear()
        
        self.level.boss1.left_bullet_particle1_list.clear()
        self.level.boss1.right_bullet_particle1_list.clear()

        self.level.boss1.rain_projectile_sprites_list.clear()

    def update(self, dt):

        if self.open_doors_delay > 0:
            self.open_doors_delay -= 10 * dt
            open_doors_delay_rounded = round(self.open_doors_delay)

            if open_doors_delay_rounded == 0:
                self.open_doors_delay = 0

        if self.open_doors_delay == 0:

            # enter in evil zone 
            if self.level.player.evil_zone > 3:

                if self.open_doors_delay_evil_zone > 0:
                    self.open_doors_delay_evil_zone -= 1 * dt
                    open_doors_delay_evil_zone_rounded = round(self.open_doors_delay_evil_zone)

    
                    if open_doors_delay_evil_zone_rounded == 5:
                        self.left_door_direction.x = 1
                        self.right_door_direction.x = -1
                     

                    if open_doors_delay_evil_zone_rounded == 0:
                        self.left_door_direction.x = -1
                        self.right_door_direction.x = 1       
            
            else:
                self.left_door_direction.x = -1
                self.right_door_direction.x = 1
            
            # =========================================================================
            """ LEFT DOOR """

            # closed
            if self.left_door_img_rect.x > 0:
                self.left_door_img_rect.x = 0

            # open
            if self.left_door_img_rect.x < -100:
                self.left_door_img_rect.x = -100
            
            # while left door's moving
            if self.left_door_img_rect.x != 0 and self.left_door_img_rect.x != -100:
                self.level.camera.game_path.in_game.camera_shake(self.level.camera, 1)                
            # left door movement
            self.left_door_img_rect.x += self.left_door_direction.x * self.left_door_speed * dt

            # =========================================================================    
            """ RIGHT DOOR """

            # closed
            if self.right_door_img_rect.x < 80:
                self.right_door_img_rect.x = 80

                # reset sound doors
                self.doors_sound_timer = 10
                self.doors_sound_timer_counter = 0

                self.clean_the_evil_zone()

            # open
            if self.right_door_img_rect.x > 220:
                self.right_door_img_rect.x = 220

                # reset sound doors
                self.doors_sound_timer = 10
                self.doors_sound_timer_counter = 0
            

            # while right door's moving
            if self.right_door_img_rect.x != 80 and self.right_door_img_rect.x != 220:
                self.level.camera.game_path.in_game.camera_shake(self.level.camera, 1)

                if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                    
                        self.doors_sound_timer, self.doors_sound_timer_counter = self.level.sound.handle_repeat_sound(self.doors_sound_timer, 10, 10, self.doors_sound_timer_counter, 1, self.level.sound.door_open_close_path, dt)

            # move the right door
            self.right_door_img_rect.x += self.right_door_direction.x * self.right_door_speed * dt
            
            


    def draw(self, screen):
        
        # left door
        screen.blit(self.left_door_img, self.left_door_img_rect)

        # right door
        screen.blit(self.right_door_img, self.right_door_img_rect)