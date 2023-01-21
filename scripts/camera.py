import pygame

from screen_setup import *
from font_custom import *
from colors import *

from game_path import GamePath


class Camera:

    def __init__(self, game):

        self.game = game

        self.game_path = GamePath(self)

    
        # main_screen_surface
        self.main_display_surface = pygame.display.get_surface()
        self.main_display_surface_width = self.main_display_surface.get_width()
        self.main_display_surface_height = self.main_display_surface.get_height()

        # camera_surface
        self.display_surface = pygame.Surface((self.main_display_surface_width, self.main_display_surface_height))
        self.display_surface_rect = self.display_surface.get_rect(topleft = (60, 50))


     
    def draw(self):
        # draw camera surface on main screen
        self.main_display_surface.blit(self.display_surface, self.display_surface_rect)
        self.display_surface.fill(color["grey"])

        # draw game path
        self.game_path.draw()
    
        # draw FPS
        # self.display_surface.blit(my_font_size_16.render(f"FPS : {round(self.game.engine.clock.get_fps())}", 0, color["light_grey"]), (0, 0))


    def update(self, dt):

        # update game path
        self.game_path.update(dt)
        