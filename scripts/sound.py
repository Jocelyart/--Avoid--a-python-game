import pygame

class Sound:

    def __init__(self):

        self.game_stuff_sound_path = "sound/game_stuff_sound.ogg"

        self.avoid_title_sound_path = "sound/avoid_title_sound.ogg"
        # self.avoid_title_stop_sound = pygame.mixer.Sound("sound/avoid_title_stop_sound.ogg")

        self.avoid_start_fight_sound_path = "sound/avoid_start_fight_sound.ogg"
        self.avoided_end_fight_sound_path = "sound/avoided_end_fight_sound.ogg"

        # selector sound
        self.selector_sound = pygame.mixer.Sound("sound/selector_sound.ogg")

        # valid sound
        self.valid_sound = pygame.mixer.Sound("sound/valid_sound.ogg")

        # death sound
        self.death_sound_path = "sound/death_sound.ogg"

        # hurt sound
        self.hurt_sound_list = [
            pygame.mixer.Sound("sound/hurt1_sound.ogg"),
            pygame.mixer.Sound("sound/hurt2_sound.ogg"),
        ]

        # normal bullet sound
        self.normal_bullet_sound = pygame.mixer.Sound("sound/normal_bullet_sound.ogg")

        # cross bullet sound
        self.cross_bullet_sound = pygame.mixer.Sound("sound/cross_bullet_sound.ogg")

        # demon bullet sound
        self.demon_bullet_sound_list = [
            pygame.mixer.Sound("sound/demon_bullet_sound1.ogg"),
            pygame.mixer.Sound("sound/demon_bullet_sound2.ogg"),
            pygame.mixer.Sound("sound/demon_bullet_sound3.ogg"),
        ]

        # rain sound
        self.rain_sound_list = [
            pygame.mixer.Sound("sound/rain_sound_1.ogg"),
            pygame.mixer.Sound("sound/rain_sound_2.ogg"),
            pygame.mixer.Sound("sound/rain_sound_3.ogg"),
        ]

        # player voice healing
        self.player_voice_healing_yes_path = pygame.mixer.Sound("sound/player_voice_healing_yes.ogg")

        # running on grass sound
        self.run_roll_grass_sound = pygame.mixer.Sound("sound/run_roll_grass_sound.ogg")

        # jump sound
        self.jump_sound = pygame.mixer.Sound("sound/jump_sound.ogg")

        # door close open sound
        self.door_open_close_path = "sound/door_close_open_sound.ogg"

        # pick up heart sound
        self.pick_up_heart_path = "sound/pick_up_heart_sound.ogg"

        # boss1 transition sound
        self.boss1_transition_path = "sound/boss1_transition_sound.ogg"

        # boss1 voice
        self.boss1_voice_intro_sound_path = "sound/boss1_voice_intro_sound.ogg"
        self.boss1_you_done_sound_path = "sound/boss1_you_done.ogg"
        self.boss1_stay_in_corners_path = "sound/boss1_voice_stay_corners.ogg"
        self.boss1_smartass_path = "sound/boss1_voice_smartass.ogg"
        self.boss1_enough_die_path = "sound/boss1_voice_enough_die.ogg"

        # evil boss1 voice
        self.evil_boss1_dont_piss_me_off_path = "sound/boss1_voice_dont_piss_me_off.ogg"
        self.evil_boss1_what_path = "sound/boss1_voice_what.ogg"
        self.evil_boss1_stop_doing_that_path = "sound/boss1_voice_stop_doing_that.ogg"
        self.evil_boss1_i_said_stop_path = "sound/boss1_voice_i_said_stop.ogg"

        

    def play(self, sound):

        if sound == "cross_bullet_sound":
            self.cross_bullet_sound.play(loops=0)
            self.cross_bullet_sound.set_volume(0.2)
        
        if sound == "normal_bullet_sound":
            self.normal_bullet_sound.play(loops=0)
            self.normal_bullet_sound.set_volume(0.5)

        if sound == "run_roll_grass_sound":
            self.run_roll_grass_sound.play(loops=0)
            self.run_roll_grass_sound.set_volume(0.4)  

        if sound == "jump_sound":
            self.jump_sound.play(loops=0)
            self.jump_sound.set_volume(0.4) 

        if sound == "selector_sound":
            self.selector_sound.play(loops=0)
            self.selector_sound.set_volume(0.4)  
        
        if sound == "valid_sound":
            self.valid_sound.play(loops=0)
            self.valid_sound.set_volume(0.4)
        

        
 
    def stop(self, sound):
        
        if sound == "cross_bullet_sound":
            self.cross_bullet_sound.stop
          
        if sound == "hurt1_sound":
            self.hurt1_sound.stop()

        if sound == "hurt2_sound":
            self.hurt2_sound.stop()
        
        if sound == "selector_sound":
            self.selector_sound.stop()
        
        if sound == "valid_sound":
            self.selector_sound.stop()
        

    
    def randomized_sound_play(self, list, index):

        if list[index]:
            if index == 0:
                list[index].play(loops=0)
                list[index].set_volume(0.8)
            
            elif index == 1:
                list[index].play(loops=0)
                list[index].set_volume(1)
    

    def randomized_sound_stop(self, list, index):

        if list[index]:
            list[index].stop()

    
    def handle_repeat_sound(self, timer, stop_timer_value, reset_timer_value, counter, repeat_sound_time, sound_file, dt):

        if timer > 0:
            timer -= 1 * dt

        my_timer = round(timer)

        if my_timer == stop_timer_value:
            timer = reset_timer_value
            pygame.mixer.Sound(sound_file).play(loops=0)
            counter += 1
        
        if counter == repeat_sound_time:
            timer = 0
          
        return timer, counter
    
  