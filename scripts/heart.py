import pygame

class Heart:
    
    def __init__(self, level):

        self.level = level

        self.image = pygame.image.load("sprites/heart/0.png").convert_alpha()

        self.rect = self.image.get_rect(topleft = (0, -50)) # off camera

        self.pos = pygame.math.Vector2()
        self.pos = self.rect

        self.speed = 100

        self.opacity = 0

        self.handle_vfx_sprites()

        self.start_vfx_animation = False

    
    def handle_vfx_sprites(self):
        
        # vfx 01
        self.vfx_01_frame = 0
        self.vfx_01_list = []

        for i in range(19):

            img = pygame.image.load(f"sprites/heart/vfx_01/{i}.png").convert_alpha()
            self.vfx_01_list.append(img)

        self.vfx_01_img = self.vfx_01_list[self.vfx_01_frame]
        self.vfx_01_img_rect = self.vfx_01_img.get_rect(topleft = (0, -50))

        # vfx 02
        self.vfx_02_frame = 0
        self.vfx_02_list = []

        for i in range(13):

            img = pygame.image.load(f"sprites/heart/vfx_02/{i}.png").convert_alpha()
            self.vfx_02_list.append(img)

        self.vfx_02_img = self.vfx_02_list[self.vfx_01_frame]
        self.vfx_02_img_rect = self.vfx_02_img.get_rect(topleft = (0, -50))

        # vfx 03
        self.vfx_03_frame = 0
        self.vfx_03_list = []

        for i in range(19):

            img = pygame.image.load(f"sprites/heart/vfx_03/{i}.png").convert_alpha()
            self.vfx_03_list.append(img)

        self.vfx_03_img = self.vfx_03_list[self.vfx_03_frame]
        self.vfx_03_img_rect = self.vfx_03_img.get_rect(topleft = (0, -50))
    
    def handle_animation(self, dt):

        if self.start_vfx_animation == True:
            # animation vfx 01
            self.vfx_01_frame += 10 * dt

            if self.vfx_01_frame >= len(self.vfx_01_list):
                self.vfx_01_frame = len(self.vfx_01_list) - 1

            # shake the screen when the heart inflates
            if 8 < self.vfx_01_frame < 12:
                self.level.camera.game_path.in_game.camera_shake(self.level.camera, 1)

            self.vfx_01_img = self.vfx_01_list[int(self.vfx_01_frame)]

            # animation vfx 02
            self.vfx_02_frame += 10 * dt

            if self.vfx_02_frame >= len(self.vfx_02_list):
                self.vfx_02_frame = len(self.vfx_02_list) - 1

            self.vfx_02_img = self.vfx_02_list[int(self.vfx_02_frame)]

            # animation vfx 03
            self.vfx_03_frame += 10 * dt

            if self.vfx_03_frame >= len(self.vfx_03_list):
                self.vfx_03_frame = len(self.vfx_03_list) - 1

            self.vfx_03_img = self.vfx_03_list[int(self.vfx_03_frame)]
        
        else:
            if self.start_vfx_animation == False:
                # reset vfx frames
                self.vfx_01_frame = 0
                self.vfx_02_frame = 0
                self.vfx_03_frame = 0
    
    def vfx_locations(self, screen):
        if self.level.zombie.select_tomb == 0:
            self.vfx_01_img_rect.x = 0
            self.vfx_01_img_rect.y = 91
            
            self.vfx_02_img_rect.x = 0
            self.vfx_02_img_rect.y = 91

            self.vfx_03_img_rect.x = 0
            self.vfx_03_img_rect.y = 91

        if self.level.zombie.select_tomb == 1:
            self.vfx_01_img_rect.x = 20
            self.vfx_01_img_rect.y = 88
            
            self.vfx_02_img_rect.x = 20
            self.vfx_02_img_rect.y = 88

            self.vfx_03_img_rect.x = 20
            self.vfx_03_img_rect.y = 88
        
        if self.level.zombie.select_tomb == 2:
            self.vfx_01_img_rect.x = 40
            self.vfx_01_img_rect.y = 97
            
            self.vfx_02_img_rect.x = 40
            self.vfx_02_img_rect.y = 97

            self.vfx_03_img_rect.x = 40
            self.vfx_03_img_rect.y = 97
        
        if self.level.zombie.select_tomb == 3:
            self.vfx_01_img_rect.x = 57
            self.vfx_01_img_rect.y = 101
            
            self.vfx_02_img_rect.x = 57
            self.vfx_02_img_rect.y = 101

            self.vfx_03_img_rect.x = 57
            self.vfx_03_img_rect.y = 101
        
        if self.level.zombie.select_tomb == 4:
            self.vfx_01_img_rect.x = 80
            self.vfx_01_img_rect.y = 91
            
            self.vfx_02_img_rect.x = 80
            self.vfx_02_img_rect.y = 91

            self.vfx_03_img_rect.x = 80
            self.vfx_03_img_rect.y = 91
        
        if self.level.zombie.select_tomb == 5:
            self.vfx_01_img_rect.x = 104
            self.vfx_01_img_rect.y = 91
            
            self.vfx_02_img_rect.x = 104
            self.vfx_02_img_rect.y = 91

            self.vfx_03_img_rect.x = 104
            self.vfx_03_img_rect.y = 91
        
        if self.level.zombie.select_tomb == 6:
            self.vfx_01_img_rect.x = 130
            self.vfx_01_img_rect.y = 84
            
            self.vfx_02_img_rect.x = 130
            self.vfx_02_img_rect.y = 84

            self.vfx_03_img_rect.x = 130
            self.vfx_03_img_rect.y = 84

        if self.start_vfx_animation == True:
            # draw vfx 01
            screen.blit(self.vfx_01_img, (self.vfx_01_img_rect.x, self.vfx_01_img_rect.y))

            # draw vfx 02
            screen.blit(self.vfx_02_img, (self.vfx_02_img_rect.x, self.vfx_02_img_rect.y))

            # draw vfx 03
            screen.blit(self.vfx_03_img, (self.vfx_03_img_rect.x, self.vfx_03_img_rect.y))

    def update(self, dt):
        self.handle_animation(dt)

    def draw(self, screen):
        
        # draw heart
        self.image.set_alpha(self.opacity)
        screen.blit(self.image, self.rect)
        
        # draw vfx
        self.vfx_locations(screen)    

