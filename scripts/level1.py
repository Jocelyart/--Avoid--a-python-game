import json

from gui import GUI
from sound import Sound
from music import Music

from tile import Tile
from player import Player
from boss1 import Boss1
from zombie import Zombie
from heart import Heart
from doors import Door_B1

class Level1():

    def __init__(self, camera):

        self.tile = 16

        self.layer0_sprites = []
        self.layer1_sprites = []
        self.layer2_sprites = []
        self.player_sprite = []
        self.boss1_sprite = []

        self.gui = GUI(camera, self)
        self.sound = Sound()
        self.music = Music()
        self.zombie = Zombie(self)
        self.heart = Heart(self)
        self.doors = Door_B1(camera, self)
        
        self.angle = 0

        self.layer0()
        self.layer1()
        self.layer2()

        self.camera = camera

        self.loading_timer = 20
        
  
    def layer0(self):
        
        # Level data
        self.layer0_list = self.load_layer0_data()
        
        for y1, row in enumerate(self.layer0_list):
            for x1, tile in enumerate(row):

                x = x1 * self.tile
                y = y1 * self.tile

                pass

    def layer1(self):
        
        # Level data
        self.layer1_list = self.load_layer1_data()
        
        for y1, row in enumerate(self.layer1_list):
            for x1, tile in enumerate(row):

                x = x1 * self.tile
                y = y1 * self.tile

                if tile == 3:
                    sprite = Tile(x, y, tile, "herb")
                    self.layer2_sprites.append(sprite) 

    def layer2(self):
        
        # Level data
        self.layer2_list = self.load_layer2_data()
        
        for y1, row in enumerate(self.layer2_list):
            for x1, tile in enumerate(row):

                x = x1 * self.tile
                y = y1 * self.tile

                if tile == 0:
                    self.player = Player(x, y, self)
                    self.player_sprite.append(self.player)

                if tile == 1:
                    sprite = Tile(x, y, tile, "floor")
                    self.layer2_sprites.append(sprite)

                if tile == 2:
                    self.boss1 = Boss1(x, y, self)
                    self.boss1_sprite.append(self.boss1)
   
    def load_layer0_data(self):

        # load level 1 data
        with open("json/layer0.json", "r") as json_file:
            data = json.load(json_file)
        
        return data
     
    def load_layer1_data(self):

        # load level 1 data
        with open("json/layer1.json", "r") as json_file:
            data = json.load(json_file)
        
        return data

    def load_layer2_data(self):

        # load level 1 data
        with open("json/layer2.json", "r") as json_file:
            data = json.load(json_file)
        
        return data
   
    def update(self, dt):

        # if self.loading_timer > 0:
        #     self.loading_timer -= 1 * dt
        #     loading_timer_rounded = round(self.loading_timer)
        #     print(loading_timer_rounded)
            
        if self.doors.right_door_img_rect.x > 220:
            # player updates
            for player in self.player_sprite:
                player.update(dt)
        
            # boss 1 updates
            for boss1 in self.boss1_sprite:
                boss1.update(dt)
        
            # zombie updates
            self.zombie.update(dt)

            # heart updates
            self.heart.update(dt)

        # doors updates
        self.doors.update(dt)
