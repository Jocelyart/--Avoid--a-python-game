import pygame

def handle_particle_update(timer, amount, particle_list, x, y, select_particle, opacity_speed, move_x, x_speed, move_y, y_speed, dt):

    # particle timer
    timer += amount * dt
    my_timer = round(timer)

    # create and spawn particle
    if my_timer > 1:
        timer = 0

        particle_list.append(Particle(x, y, select_particle))
  

    # get each particle into the list
    for particle in particle_list:
        
        if particle_list:

            # decrease image opacity
            particle.opacity -= opacity_speed * dt
            particle_opacity_rounded = round(particle.opacity)

            if particle_opacity_rounded <= 0:
                particle.opacity = 0
                
                # delete particle
                if particle in particle_list:
                    particle_list.remove(particle)
           
            # move particle
            if move_x == True:
                particle.rect.x += round(x_speed * dt)

            if move_y == True:
                particle.rect.y += round(y_speed * dt)
            
            # change particle image opacity
            particle.image.set_alpha(particle_opacity_rounded)
            
    return timer, particle_list

class Particle:

    def __init__(self, x, y, img_index):

        # particle 0
        if img_index == 0:
            self.opacity = 255
            self.image = pygame.image.load("sprites/particle0.png").convert_alpha()
            self.image.set_alpha(self.opacity)
        
        # particle 1
        if img_index == 1:
            self.opacity = 255
            self.image = pygame.image.load("sprites/particle1.png").convert_alpha()
            self.image.set_alpha(self.opacity)
        
        # particle 2
        if img_index == 2:
            self.opacity = 255
            self.image = pygame.image.load("sprites/particle2.png").convert_alpha()
            self.image.set_alpha(self.opacity)
        
        # particle 3
        if img_index == 5:
            self.opacity = 255
            self.image = pygame.image.load("sprites/particle3.png").convert_alpha()
            self.image.set_alpha(self.opacity)
        
        # particle 4
        if img_index == 6:
            self.opacity = 255
            self.image = pygame.image.load("sprites/particle4.png").convert_alpha()
            self.image.set_alpha(self.opacity)
        
        # particle 5
        if img_index == 7:
            self.opacity = 255
            self.image = pygame.image.load("sprites/particle5.png").convert_alpha()
            self.image.set_alpha(self.opacity)

        # right hand
        if img_index == 3:
            self.frame = 0
            self.image_list = []

            for i in range(6 + 1):
                img = pygame.image.load(f"sprites/boss/level1/right_hand/{i}.png").convert_alpha()
                self.image_list.append(img)

            self.opacity = 255
            self.image = self.image_list[self.frame]
            self.image.set_alpha(self.opacity)
        
        # left hand
        if img_index == 4: 
            self.frame = 0
            self.image_list = []

            for i in range(6 + 1):
                img = pygame.image.load(f"sprites/boss/level1/left_hand/{i}.png").convert_alpha()
                self.image_list.append(img)

            self.opacity = 255
            self.image = self.image_list[self.frame]
            self.image.set_alpha(self.opacity)

        # particles rectangle
        self.rect = self.image.get_rect(topleft = (x, y))

        

    