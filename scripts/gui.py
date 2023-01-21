import pygame

from colors import color

class GUI:

    def __init__(self, camera, level):

        self.camera = camera
        self.level1 = level
        self.assets()
        

    def assets(self):
        # player portrait
        self.player_portrait = pygame.image.load("sprites/gui/player_portrait.png").convert_alpha()
        self.player_portrait_rect = self.player_portrait.get_rect(topleft = (5, 130))

        # multiplicator sprite
        self.multiplicator_sprite = pygame.image.load("sprites/gui/multiplicator.png").convert_alpha()
        self.multiplicator_sprite_rect = self.multiplicator_sprite.get_rect(topleft = (15, 132))

        # timer sprite
        self.timer_sprite = pygame.image.load("sprites/gui/timer.png").convert_alpha()
        self.timer_sprite_rect = self.timer_sprite.get_rect(topleft = (130, 131))

        # life bar border
        self.life_bar_border = pygame.image.load("sprites/gui/life_bar_border.png").convert_alpha()
        self.life_bar_border_rect = self.life_bar_border.get_rect(topleft = (5, 131))
        self.life_unit_border = 10

        # life bar
        self.life_bar = pygame.image.load("sprites/gui/life_bar.png").convert_alpha()
        self.life_bar_rect = self.life_bar.get_rect(topleft = (5, 131))
        self.life_unit = 10 # 10

        # stamina bar edge
        self.stamina_bar_edge = pygame.image.load("sprites/gui/stamina_bar_edge.png").convert_alpha()
        self.stamina_bar_edge_rect = self.stamina_bar_edge.get_rect(topleft = (5, 137))

        # stamina bar
        self.stamina_bar_size = (20, 3)
        self.stamina_bar = pygame.transform.scale(pygame.image.load("sprites/gui/stamina_bar.png").convert_alpha(), self.stamina_bar_size)
        self.stamina_bar_rect = self.stamina_bar.get_rect(topleft = (5, 137))

        # music note
        self.music_note_img = pygame.image.load("sprites/gui/music_note.png").convert_alpha()
        self.music_note_img_rect = self.music_note_img.get_rect(topleft = (105, 130))

        # dance energy bar
        self.dance_energy_bar_size = (5, 1)
        self.dance_energy_bar_img = pygame.transform.scale(pygame.image.load("sprites/gui/dance_energy_bar.png").convert_alpha(), self.dance_energy_bar_size)
        self.dance_energy_bar_img_rect = self.dance_energy_bar_img.get_rect(topleft = (96, 138))

        # dance energy container
        self.dance_energy_container_img = pygame.image.load("sprites/gui/dance_container_energy.png").convert_alpha()
        self.dance_energy_container_img_rect = self.dance_energy_container_img.get_rect(topleft = (95, 129))

        # fonts
        self.life_number = 1 # 1
        self.life_font = pygame.font.Font("font/Minecraft.ttf", 7)
        self.life_font_number = self.life_font.render(f"{self.life_number}", 0, color["dark_grey"])
        self.life_font_number_rect = self.life_font_number.get_rect(topleft = (22, 131))

        self.boss_counter = 0
        self.boss_timer_value = 1089 # 1089
        self.boss_timer = self.boss_timer_value
        self.boss_font = pygame.font.Font("font/Minecraft.ttf", 7)
        self.boss_font_number = self.boss_font.render(f"{self.boss_timer}", 0, color["dark_grey"])
        self.boss_font_number_rect = self.boss_font_number.get_rect(topleft = (140, 131))

        
    def draw(self):

        # player portrait
        self.camera.display_surface.blit(self.player_portrait, self.player_portrait_rect)

        # multiplicator sprite
        self.camera.display_surface.blit(self.multiplicator_sprite, self.multiplicator_sprite_rect)

        # life bar border
        for i in range(self.life_unit_border):
            self.camera.display_surface.blit(self.life_bar_border, (self.life_bar_border_rect.x * i + 35, self.life_bar_border_rect.y))

        # life bar
        for i in range(self.life_unit):
            self.camera.display_surface.blit(self.life_bar, (self.life_bar_rect.x * i + 35, self.life_bar_rect.y))
        
        # stamina bar
        self.camera.display_surface.blit(self.stamina_bar, self.stamina_bar_rect)

        # stamina bar edge
        self.camera.display_surface.blit(self.stamina_bar_edge, self.stamina_bar_edge_rect)

        # timer sprite
        self.camera.display_surface.blit(self.timer_sprite, self.timer_sprite_rect)

        # life number
        self.camera.display_surface.blit(self.life_font_number, self.life_font_number_rect)

        # boss timer
        self.camera.display_surface.blit(self.boss_font_number, self.boss_font_number_rect)

        # music note
        self.camera.display_surface.blit(self.music_note_img, self.music_note_img_rect)

        # dance energy bar
        # show energy bar even not pressing select
        for i in range(self.level1.player.energy_counter_rounded):
            self.camera.display_surface.blit(self.dance_energy_bar_img, (self.dance_energy_bar_img_rect.x, -i + self.dance_energy_bar_img_rect.y))

        # dance energy container
        self.camera.display_surface.blit(self.dance_energy_container_img, self.dance_energy_container_img_rect)



    def update(self, dt):

        # life unit
        if self.life_unit <= 0:
            self.life_unit = 0
            self.life_number = 0

        
        # boss timer
        self.boss_counter += round(100 * dt)
        if self.boss_counter > 25:
            self.boss_counter = 0

            if self.level1.player.is_alive == "yes":
                if self.level1.doors.right_door_img_rect.x > 220:
                    self.boss_timer -= 1    

                
        if self.boss_timer < 0:
            self.boss_timer = 0

        # update images
        self.boss_font_number = self.boss_font.render(f"{self.boss_timer}", 0, color["dark_grey"])
        self.life_font_number = self.life_font.render(f"{self.life_number}", 0, color["dark_grey"])
        