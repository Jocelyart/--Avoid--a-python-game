import pygame

class Tile():

    def __init__(self, x, y, tile, entity):

        self.tile = 16
        self.entity = entity

        if tile == 1:
            self.entity = "floor"
            self.image = pygame.transform.scale(pygame.image.load("sprites/1.png").convert_alpha(), (self.tile, self.tile))
            
            if self.entity == "floor":
                self.rect = self.image.get_rect(topleft = (x, y))
        
        if tile == 3:
            self.entity = "herb"
            self.image = pygame.transform.scale(pygame.image.load("sprites/3.png").convert_alpha(), (self.tile, self.tile))
            
            if self.entity == "herb":
                self.rect = self.image.get_rect(topleft = (x, y))
        
        
        
        