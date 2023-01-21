import pygame, math

from random import randint

def math_projectile(angle, angle_speed, amplitude_x, offset_x, dt):

    angle += angle_speed * dt # radians value

    if angle >= (360 * math.pi/180): # 360 degrees into radians 6.28
        angle = 0
    
    dx = math.cos(angle) * amplitude_x + offset_x

    return angle, dx

class CrossProjectile:

    def __init__(self, x, y):

        # projectile 1
        self.size = (6, 16)
        self.image = pygame.transform.scale(pygame.image.load("sprites/boss/level1/cross_bullet.png").convert_alpha(), self.size)
        self.rect = self.image.get_rect(topleft = (x, y))

        self.speed = 150

class LeftBulletProjectile:

    def __init__(self, x, y):

        # projectile 1
        self.size = (9, 4)
        self.image = pygame.transform.scale(pygame.image.load("sprites/boss/level1/left_bullet.png").convert_alpha(), self.size)
        self.rect = self.image.get_rect(topleft = (x, y))

        self.speed = 160

class RightBulletProjectile:

    def __init__(self, x, y):

        # projectile 1
        self.size = (9, 4)
        self.image = pygame.transform.scale(pygame.image.load("sprites/boss/level1/right_bullet.png").convert_alpha(), self.size)
        self.rect = self.image.get_rect(topleft = (x, y))

        self.speed = 100

class DemonProjectile:

    def __init__(self, x, y, target_x, target_y):

        self.size = (7, 32)
        self.demon_frame = 0
        self.demon_bullet_list = [
            pygame.transform.scale(pygame.image.load("sprites/boss/level1/demon_bullet/0.png").convert_alpha(), self.size),
            pygame.transform.scale(pygame.image.load("sprites/boss/level1/demon_bullet/1.png").convert_alpha(), self.size),
        ]
        self.demon_bullet_image = self.demon_bullet_list[self.demon_frame]
        
        # boss aims projectile 2
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y

        self.speed = 150  #randint(150, 250)
        rotation = 0
        
        self.angle = math.degrees(math.atan2(y - target_y, x - target_x))

        if target_x <= 70:
            rotation = 60
        
        if target_x >= 71:
            rotation = 82
    
        self.image = pygame.transform.rotate(self.demon_bullet_image, self.angle + rotation)
        self.rect = self.image.get_rect(center = (x, y))
        self.dx = math.cos(math.radians(self.angle)) * self.speed
        self.dy = math.sin(math.radians(self.angle)) * self.speed

class RainProjectile:

    def __init__(self, x, y, speed):

        self.size = (4, 16)
        self.image = pygame.transform.scale(pygame.image.load("sprites/boss/level1/cross_rain.png").convert_alpha(), self.size)
        self.rect = self.image.get_rect(topleft = (x, y))

        self.angle_speed = 0
        self.amplitude_x = 0
        self.offset_x = 0
        self.dx = 0

        self.speed = speed

class SpearProjectile: # deadly -> one shot player

    def __init__(self, x, y, target_x, target_y):

        self.size = (3, 32)
        self.spear_image = pygame.image.load("sprites/boss/level1/spear.png").convert_alpha()
        
        # boss aims projectile 2
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y

        self.speed = 300 
        rotation = 0
        
        self.angle = math.degrees(math.atan2(y - target_y, x - target_x))

        if target_x <= 70:
            rotation = 60
        
        if 71 <= target_x <= 119:
            rotation = 80

        if target_x >= 120:
            rotation = 100
    
        self.image = pygame.transform.rotate(self.spear_image, self.angle + rotation)
        self.rect = self.image.get_rect(center = (x, y))
        self.dx = math.cos(math.radians(self.angle)) * self.speed
        self.dy = math.sin(math.radians(self.angle)) * self.speed
       