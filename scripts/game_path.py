import pygame

from music import Music

from in_intro_0 import InIntro0
from in_setup_control import InSetupControl
from in_intro_1 import InIntro1
from in_menu import InMenu
from in_game import InGame
from in_options import InOptions
from in_how_to_play import InHowToPlay
from in_credits import InCredits
from music import Music
from sound import Sound


class GamePath:

    def __init__(self, camera):

        self.music = Music()
        self.sound = Sound()

        self.in_intro_0 = InIntro0(camera, self)
        self.in_intro_1 = InIntro1(camera, self)
        self.in_setup_controls = InSetupControl(camera, self)
        self.in_menu = InMenu(camera, self)
        self.in_game = InGame(camera, self)
        self.in_options = InOptions(camera, self)
        self.in_how_to_play = InHowToPlay(camera, self)
        self.in_credits = InCredits(camera, self)

        self.go_to_intro_0 = True
        self.go_to_setup_controls = False
        self.go_to_intro_1 = False
        self.go_to_menu = False
        self.go_to_game = False
        self.go_to_options = False
        self.go_to_how_to_play = False
        self.go_to_credits = False

        # self.reload_timer = "no"
        self.delay_timer_music = 10
        self.force_reload_timer = 5

        self.select_channel = 0
        self.select_track = 0
        self.loops = -1
        self.start_value_track = 0.0

        self.check_playtime_value = "yes"
        self.last_playtime_value = 0.0
        self.new_playtime_value = 0.0

    def update(self, dt):

        """ HANDLE GAME PATH """

        # GO TO INTRO 0 
        if self.go_to_intro_0 == True:
            self.in_intro_0.update(dt)

        # GO TO SETUP CONTROLS
        if self.go_to_setup_controls == True:
            self.in_setup_controls.update(dt)
        
        # GO TO INTRO 1
        if self.go_to_intro_1 == True:
            self.in_intro_1.update(dt)


        # GO TO MENU
        if self.go_to_menu == True:
            self.in_menu.update(dt)
        
        
        # GO TO GAME
        if self.go_to_game == True:
            self.in_game.update(dt)
            

        # GO TO OPTIONS
        if self.go_to_options == True:
            self.in_options.update(dt)


        # GO TO HOW TO PLAY
        if self.go_to_how_to_play == True:
            self.in_how_to_play.update(dt)


        # GO TO CREDITS
        if self.go_to_credits == True:
            self.in_credits.update(dt)

        # MUTE MUSICS
        if self.in_options.music_on_off_state == 1:
            self.delay_timer_music = 10
            self.force_reload_timer = 5
   
        """ HANDLE THE MUSICS ON THE OVERALL GAME HERE """     
        # no music in intro 0
        if self.go_to_intro_0 == True:
            self.delay_timer_music = 10
        
        if self.go_to_setup_controls == True:
            self.delay_timer_music = 10
        
        # IN MENU
        if self.go_to_menu == True:
            self.select_channel = 0
            self.select_track = 0
            self.loops = -1

        # IN GAME
        # game screen 0
        if self.go_to_game == True and self.in_game.game_screen_counter == 1:

            if self.force_reload_timer > 0:
                self.force_reload_timer -= 1
                if self.force_reload_timer <= 3:
                    self.delay_timer_music = 10
                    self.loops = 0
            
    
            self.select_channel = 1
            self.select_track = 0
            
        
        # # game screen 1 in actual game
        elif self.go_to_game == True and self.in_game.game_screen_counter == 2:
            
            # get the playtime value of the track
            if self.check_playtime_value == "yes":
                self.last_playtime_value = pygame.mixer.music.get_pos() / 1000 # value in seconds

            # save the new playtime value
            self.new_playtime_value = self.last_playtime_value


            if self.in_game.level1.player.evil_zone > 3:
                if self.in_game.level1.doors.right_door_img_rect.x <= 80:
                    self.delay_timer_music = 10
                    self.select_channel = 0
                    self.select_track = 2

                    self.check_playtime_value = "no"
                    # update the new start value track
                    self.start_value_track = self.new_playtime_value
                  
            
            else:
                if self.force_reload_timer > 0:
                    self.force_reload_timer -= 1
                    if self.force_reload_timer <= 3:
                        self.delay_timer_music = 10
                        self.loops = -1
                        self.select_channel = 0
                        self.select_track = 1
            
        
        else:
            if self.go_to_game == False:
                self.force_reload_timer = 5

        # handle music
        self.delay_timer_music = self.music.handle_music(self.delay_timer_music, self.music.soundtrack[self.select_channel][self.select_track], self.loops, self.start_value_track, dt)
        
    def draw(self):
        
        if self.go_to_intro_0 == True:
            self.in_intro_0.draw()

        if self.go_to_setup_controls == True:
            self.in_setup_controls.draw()

        if self.go_to_intro_1 == True:
            self.in_intro_1.draw()
        
        if self.go_to_menu == True:
            self.in_menu.draw()
        
        if self.go_to_game == True:
            self.in_game.draw()
        
        if self.go_to_options == True:
            self.in_options.draw()
        
        if self.go_to_how_to_play == True:
            self.in_how_to_play.draw()

        if self.go_to_credits == True:
            self.in_credits.draw()
        
    
    

