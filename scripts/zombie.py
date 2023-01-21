import pygame

from random import randint

class Zombie:
    
    def __init__(self, level):

        self.level = level

        self.handle_sprites()
        self.tombs_colliders()

        self.idle_frame = 0
        self.walk_frame = 0
        self.run_frame = 0

        self.image = self.idle_sprite_list[self.idle_frame]
        
        self.flip = False

        self.rect = self.image.get_rect(topleft = (200, 96))

        self.pos = pygame.math.Vector2()
        self.pos = self.rect

        self.direction = pygame.math.Vector2()
        self.speed = 100

        self.state = "idle"
        
        self.select_tomb = 0

        self.collision_state = "zombie"

        self.left_collider_img = pygame.Surface((5, 40))
        self.left_collider_img.fill("red")
        self.left_collider_img_rect = self.left_collider_img.get_rect(topleft = (-100, 110))

        self.right_collider_img = pygame.Surface((5, 40))
        self.right_collider_img.fill("red")
        self.right_collider_img_rect = self.right_collider_img.get_rect(topleft = (250, 110))

        self.collision_state_timer = 10
        self.tomb_randomizer = 5

        self.new_location = "None"

        self.stop_moving = "yes"

        self.collision_contact = "yes"
        self.collision_contact_timer = 20
        
        # pick up heart sound timer
        self.pick_up_heart_timer = 10
        self.pick_up_heart_timer_counter = 0
       
    
    def tombs_colliders(self):

        self.tomb_list = [
            (pygame.Surface((10, 20)), pygame.Rect(11, 110, 10, 20)),
            (pygame.Surface((10, 20)), pygame.Rect(32, 110, 10, 20)),
            (pygame.Surface((5, 20)),  pygame.Rect(54, 110, 5, 20)),
            (pygame.Surface((10, 20)), pygame.Rect(69, 110, 10, 20)),
            (pygame.Surface((8, 20)),  pygame.Rect(92, 110, 8, 20)),
            (pygame.Surface((7, 20)),  pygame.Rect(117, 110, 7, 20)),
            (pygame.Surface((10, 20)), pygame.Rect(142, 110, 10, 20)),
        ]


    def handle_sprites(self):

        self.idle_sprite_list = []

        for i in range(4):
            img = pygame.image.load(f"sprites/zombie/idle/{i}.png").convert_alpha()
            self.idle_sprite_list.append(img)

        self.walk_sprite_list = []

        for i in range(10):
            img = pygame.image.load(f"sprites/zombie/walk/{i}.png").convert_alpha()
            self.walk_sprite_list.append(img)
        
        self.run_sprite_list = []

        for i in range(10):
            img = pygame.image.load(f"sprites/zombie/run/{i}.png").convert_alpha()
            self.run_sprite_list.append(img)

    def play_animation(self, dt):

        if self.state == "idle":

            self.idle_frame += 4 * dt

            if self.idle_frame >= len(self.idle_sprite_list):
                self.idle_frame = 0

            self.image = self.idle_sprite_list[int(self.idle_frame)]
        
        if self.state == "walk":

            self.walk_frame += 12 * dt

            if self.walk_frame >= len(self.walk_sprite_list):
                self.walk_frame = 0
            
            self.image = self.walk_sprite_list[int(self.walk_frame)]
        
        if self.state == "run":

            self.run_frame += 12 * dt

            if self.run_frame >= len(self.run_sprite_list):
                self.run_frame = 0
            
            self.image = self.run_sprite_list[int(self.run_frame)]
        
    def handle_movement(self):

        if self.direction.x == -1:
            self.flip = False
            self.state = "run"
        
        elif self.direction.x == 1:
            self.flip = True
            self.state = "run"

        else:
            if self.direction.x == 0:
                self.state = "idle"


    def move_and_collide(self, dt):

        if self.new_location == "right":
            self.direction.x = 1
        
        if self.new_location == "left":
            self.direction.x = -1
    

        if self.collision_state == "player":
            self.level.heart.rect.x = 0
            self.level.heart.rect.y = -50
            
        if self.collision_state == "zombie":
            # HEART LOCATION AFTER COLLISION
            if self.select_tomb == 0:
                self.level.heart.rect.x = self.tomb_list[self.select_tomb][1].x + 2
                self.level.heart.rect.y = self.tomb_list[self.select_tomb][1].y - 6
            
            if self.select_tomb == 1:
                self.level.heart.rect.x = self.tomb_list[self.select_tomb][1].x + 1
                self.level.heart.rect.y = self.tomb_list[self.select_tomb][1].y - 9
            
            if self.select_tomb == 2:
                self.level.heart.rect.x = self.tomb_list[self.select_tomb][1].x - 1
                self.level.heart.rect.y = self.tomb_list[self.select_tomb][1].y 
            
            if self.select_tomb == 3:
                self.level.heart.rect.x = self.tomb_list[self.select_tomb][1].x + 1
                self.level.heart.rect.y = self.tomb_list[self.select_tomb][1].y + 4
            
            if self.select_tomb == 4:
                self.level.heart.rect.x = self.tomb_list[self.select_tomb][1].x + 1
                self.level.heart.rect.y = self.tomb_list[self.select_tomb][1].y - 6
            
            if self.select_tomb == 5:
                self.level.heart.rect.x = self.tomb_list[self.select_tomb][1].x 
                self.level.heart.rect.y = self.tomb_list[self.select_tomb][1].y - 6
            
            if self.select_tomb == 6:
                self.level.heart.rect.x = self.tomb_list[self.select_tomb][1].x + 1 
                self.level.heart.rect.y = self.tomb_list[self.select_tomb][1].y - 13
        

        if self.collision_state_timer > 9:
            if self.collision_contact == "yes":
                
                if self.collision_contact_timer > 5:
                    if self.rect.colliderect(self.tomb_list[self.select_tomb][1]): # collision zombie / tomb
                        # player can't press pause while collision (avoid game crash)
                        self.level.camera.game_path.in_game.pause_counter = 1
                        if self.collision_contact_timer > 0:
                            self.collision_contact_timer -= 1 * dt
                        
                        # heart opacity
                        self.level.heart.opacity += 75 * dt
                        if self.level.heart.opacity >= 255:
                            self.level.heart.opacity = 255
                        
                        # activate heart vfx
                        self.level.heart.start_vfx_animation = True
                        
                        # collision state
                        self.collision_state = "zombie"
                        self.direction.x = 0

                        # collision directions
                        if self.direction.x < 0:
                            self.rect.left = self.tomb_list[self.select_tomb][1].right
                        
                        if self.direction.x > 0:
                            self.rect.right = self.tomb_list[self.select_tomb][1].left
                else:
                    # desactivate collisions and reset collision state
                    self.collision_contact = "no"
                    self.collision_state = "player"

                    # desactivate heart vfx
                    self.level.heart.start_vfx_animation = False
  
        # collision player / heart
        if self.level.player.hitbox.colliderect(self.level.heart.rect) and self.level.heart.opacity == 255:
            # player can't press pause while collision (avoid game crash)
            self.level.camera.game_path.in_game.pause_counter = 1
            self.collision_state_timer -= 1
            
            # reset collision state
            self.collision_state = "player"

            # full live player
            self.level.gui.life_unit = 10
            
            # heart diseapear
            self.level.heart.opacity = 0

            # desactivate heart vfx
            self.level.heart.start_vfx_animation = False

            # randomize heart locations normal/evil zone
            if self.level.player.evil_zone > 3:
                self.select_tomb = randint(1, 5)  
            else:  
                self.select_tomb = randint(0, 6)

            # pick up heart sound
            if self.level.camera.game_path.in_options.sfx_on_off_state == 0:
                    
                    self.pick_up_heart_timer, self.pick_up_heart_timer_counter = self.level.sound.handle_repeat_sound(self.pick_up_heart_timer, 10, 10, self.pick_up_heart_timer_counter, 1, self.level.sound.pick_up_heart_path, dt)
           

        if self.stop_moving == "yes":
            # collision zombie / left collider
            if self.rect.colliderect(self.left_collider_img_rect):
                self.direction.x = 0

                # reset timer
                self.collision_state_timer = 10

                # reset tomb randomizer
                self.tomb_randomizer = 2

                # reset collision
                self.collision_contact = "yes"

                # reset collision state timer
                self.collision_contact_timer = 20

                # desactivate heart vfx
                self.level.heart.start_vfx_animation = False

                # reset pick up heart sound timer
                self.pick_up_heart_timer = 10
                self.pick_up_heart_timer_counter = 0
            
            # collision zombie / right collider
            if self.rect.colliderect(self.right_collider_img_rect):
                self.direction.x = 0

                # reset timer
                self.collision_state_timer = 10

                # reset tomb randomizer
                self.tomb_randomizer = 2

                # reset collision
                self.collision_contact = "yes"

                # reset collision state timer
                self.collision_contact_timer = 20

                # desactivate heart vfx
                self.level.heart.start_vfx_animation = False

                # reset pick up heart sound timer
                self.pick_up_heart_timer = 10
                self.pick_up_heart_timer_counter = 0

        # zombie movement
        self.pos.x += round(self.direction.x * self.speed * dt)
        self.rect.x = self.pos.x

    def check_tomb_value(self, dt):
        if self.tomb_randomizer > 0:
            self.tomb_randomizer -= 1 * dt

            tomb_randomizer_rounded = round(self.tomb_randomizer)

            if self.level.player.evil_zone > 3:

                if tomb_randomizer_rounded >= 3:
                    self.select_tomb = randint(1, 5)
            else:
                if tomb_randomizer_rounded >= 3:
                    self.select_tomb = randint(0, 6)
        
        # refresh tomb value in the evil zone
        if self.level.player.evil_zone > 3:
            if self.select_tomb == 0:
                self.select_tomb = 1
            elif self.select_tomb == 6:
                self.select_tomb = 5


    def update(self, dt):

        self.handle_movement()
        self.move_and_collide(dt)
        self.play_animation(dt)
        self.check_tomb_value(dt)


    def draw(self, screen):

        # draw selected tomb
        self.tomb_list[self.select_tomb][0].set_alpha(0)
        self.tomb_list[self.select_tomb][0].fill("red")
        screen.blit(self.tomb_list[self.select_tomb][0], self.tomb_list[self.select_tomb][1])

        # left collider
        screen.blit(self.left_collider_img, self.left_collider_img_rect)

        # right collider
        screen.blit(self.right_collider_img, self.right_collider_img_rect)

        # draw zombie
        self.image.set_alpha(150)

        # draw hitbox
        # pygame.draw.rect(screen, "red", self.rect, 1)

        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)