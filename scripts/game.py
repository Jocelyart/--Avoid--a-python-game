import pygame

from camera import Camera

class Game():

    def __init__(self, engine):

        self.display_surface = pygame.display.get_surface()
        self.engine = engine
        self.camera = Camera(self)
        self.game_boy_img = pygame.image.load("sprites/gameboy_img.png").convert_alpha()
        self.game_boy_img_rect = self.game_boy_img.get_rect(topleft = (0, 0))
    
    def draw(self):

        self.camera.draw()
        self.display_surface.blit(self.game_boy_img, self.game_boy_img_rect)


    def update(self, dt):
        
        self.camera.update(dt)
