import pygame


class Music:

    def __init__(self):

        self.soundtrack = [
            [
                "music/music_menu.ogg",
                "music/music_boss1.ogg",
                "music/music_boss1_evil_mode.ogg"
            ],

            [
                "music/game_intro_speech.ogg",
                "music/game_intro_music_only.ogg"
            ]
        ]
        

    def load(self, select_channel, select_soundtrack):
        pygame.mixer.music.load(self.soundtrack[select_channel][select_soundtrack])


    def play(self, loop, start):
        pygame.mixer.music.play(loop, start)

    def stop(self):
        pygame.mixer.music.stop()
     
    def fadeout(self, time):
        pygame.mixer.music.fadeout(time)
    
    def pause(self):
        pygame.mixer.music.pause()
    
    def unpause(self):
        pygame.mixer.music.unpause()
    
    def queue(self, select_channel, select_soundtrack, loop):
        pygame.mixer.music.queue(self.soundtrack[select_channel][select_soundtrack], "", loop)
    
    def volume(self, value):
        pygame.mixer.music.set_volume(value)
    
    def handle_music(self, delay_timer, music_path, loops_value, start_value_track, dt):
        if delay_timer > 0:
            delay_timer -= 5 * dt
            delay_timer_rounded = round(delay_timer)

            # print(delay_timer_rounded)

            if delay_timer_rounded == 10:
                pygame.mixer.music.stop()
            
            if delay_timer_rounded == 9:
                pygame.mixer.music.set_volume(0)
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play(loops_value, start_value_track)
            
            if delay_timer_rounded == 8:
                pygame.mixer.music.set_volume(1)
            
            if delay_timer_rounded <= 7:    
                if loops_value == 0:
                    # next music
                    pygame.mixer.music.queue(self.soundtrack[1][1], "", -1)


        return delay_timer
    
  
    
   

   