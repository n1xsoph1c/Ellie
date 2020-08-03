''' 
Music Player | Ellie
================

It Finds all the music stored on the device and then the music
can be played by two methods :mod:`music` and :mod:`playlist`

Music
------------------
Music method plays only one given music from the whole list.

Playlist
------------
Playlist method plays all the music from the device one by one.
The name explains everything.

Usage | Music 
---------------------
>>>> import music_player
>>>> mp = music_player.music(song_name)
>>>> mp.find() # Find the song
>>>> mp.play() # Play it

Usage | Playlist
---------------------
>>>> import music_player
>>>> player = music_player.playlist(Interface Title)
>>>> player.find() #Find all the songs. Might take some time
>>>> player.play()

'''
import os
import time
import pygame
import pygame.freetype
from pygame.locals import *
from os.path import join
from multiprocessing import Process

class display:
    def __init__(self, title):
        pygame.init()
        pygame.freetype.init()

        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((490, 600))

        self.screen.fill(Color('white'))
        pygame.display.flip()
        
        self.font = pygame.freetype.Font(None, 20)
        self.font.origin = True
        self.ascender = int(self.font.get_sized_ascender() * 1.5)
        self.descender = int(self.font.get_sized_descender() * 1.5)
        self.line_height = self.ascender - self.descender

        self.image_path = os.path.join(os.getcwd(), "Lib", "Images", "MPUI")
        self.song = str()
        self.background_img = pygame.image.load(os.path.join(self.image_path,"background.png"))
        self.play_btn = pygame.image.load(os.path.join(self.image_path, "play.png"))
        self.pause_btn = pygame.image.load(os.path.join(self.image_path, "pause.png"))
        self.next_btn = pygame.image.load(os.path.join(self.image_path, "next.png"))
        self.previous_btn = pygame.image.load(os.path.join(self.image_path, "previous.png"))

        self.rect = pygame.Rect(160, 500, 200, 60)

    def write_lines(self, text, line=0):
        w, h = self.screen.get_size()
        line_height = self.line_height
        nlines = h // line_height
        if line < 0:
            line = nlines + line
        for i, text_line in enumerate(text.split('\n'), line):
            y = i * line_height + self.ascender
            # Clear the line first.
            self.screen.fill(Color('white'))

            # Write new text.
            self.font.render_to(self.screen, (15, y), text_line, Color('blue'))
        pygame.display.flip()

    def write_info(self, text):
        # self.screen.fill(Color("white"))
        self.font.render_to(self.screen, (480, 390), text, Color('dodgerblue2'))
        pygame.display.update()

    def handle_event(self, event):
        x = event.pos[0]
        y = event.pos[1]

        if not self.rect.collidepoint(event.pos):
        # if not (x > 160 and y > 500) and (x < 360 and y < 560):
            self.draw()
            self.font.render_to(self.screen, (100, 520), self.song, (240, 240, 240))
        else:
            self.draw_btn()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_btn.get_rect().collidepoint(event.pos):
                print("collided")

    def draw(self):
        self.screen.fill((50,50,50))
        self.screen.blit(self.background_img, (0,0))
        pygame.display.update()

    def draw_btn(self):
        self.screen.blit(self.pause_btn, (490/2, self.background_img.get_height() + 15))
        self.screen.blit(self.previous_btn, (490/2 - 35, self.background_img.get_height() + 15))
        self.screen.blit(self.next_btn, (490/2 + 30, self.background_img.get_height() + 15))
        pygame.display.update()

class music:
    def __init__(self, music):
        self.music_to_look_for = music
        self.song_list = list()
        self.song = ''
        self.songName = ''
        self.song_name = list()
        self.file_list = list()
        self.song_loc_in_the_file = int()

    def find(self):
        i = self.music_to_look_for.lower()
        x = i.replace('.mp3', '')
        self.song = x.split()

        for (dirname, dirs, files) in os.walk('/Users'):
            for filename in files:
                if filename.endswith('.mp3'):
                    the_file = os.path.join(dirname, filename)
                    self.file_list.append(the_file)

                    t = filename.replace('.mp3', '')
                    self.song_name.append(t)
                    g = t.lower().split()
                    self.song_list.append(g)

        for num, act in enumerate(self.song_list):
            r = self.ratio(act, self.song)
            if r > 60:
                self.song_loc_in_the_file = num
                break

        self.songName = self.song_name[self.song_loc_in_the_file]
        self.song_to_play = self.file_list[self.song_loc_in_the_file]

    def ratio(self, pre, act):

        res = set(pre).intersection(set(act))

        ress = (len(res) / len(act)) * 100

        return ress

    def play(self):
        loop = False
        SongToPlay = self.song_to_play

        if SongToPlay == None:
            print('Sorry its not in the device')
        else:
            print(f"Now playing: {self.songName}\n")
            pygame.mixer.init()
            pygame.mixer.music.load(SongToPlay)
            pygame.mixer.music.play()
            

        while True:
            t = input('Hit enter or any command: ')
            # t = '/playall'
            tmp = t.split()

            if t == '/pause':
                pygame.mixer.music.pause()
                paused = True

            if t == '/Volume':
                print(f'Volume = {pygame.mixer.music.get_volume() * 100}')

            if t == '/resume' and paused:
                pygame.mixer.music.unpause()
                paused = False

            if t == '/stop':
                pygame.mixer.music.stop()
                break

            if t == '/all':
                for name in self.song_name:
                    print(name)
                print('\n')

            if t == "/loop" and loop == False:
                loop = True
                print("\nLoop Enabled\n")
                pygame.mixer.music.play(-1)

            if t == "/loop" and loop == True:
                loop = False
                print("\nLoop Disabled\n")
                pygame.mixer.music.play()

            if t == "/playall":
                self.playlist()

            # if playlist_mode and t == '/skip':

            for numb, words in enumerate(tmp):
                if '/setVol' in words:
                    vv = ' '.join(tmp[numb + 1: numb + 2])
                    v = int(vv)
                    if v >= 0 and v <= 100:
                        vol = v / 100
                        print('Okay setting Volume to {}\n'.format(v))
                        pygame.mixer.music.set_volume(vol)
                    else:
                        print("Please enter a number between 0 to 100\n")

    def Song_Name(self):
        return self.songName

    def Song_to_play(self):
        return self.song_to_play

    def song_list(self):
        return self.file_list

class playlist:
    def __init__(self, title):
        self.song_number = 0
        self.win = display(title)
        self.file_list = list()
        self.song_name_list = list()
        self.Volume = 0

    def find(self):
        # i = self.music_to_look_for.lower()
        # x = i.replace('.mp3', '')
        # self.song = x.split()
        self.win.write_lines("Loading...............", 1)

        for (dirname, dirs, files) in os.walk('/Users'):
            for filename in files:
                if filename.endswith('.mp3'):
                    the_file = os.path.join(dirname, filename)
                    self.file_list.append(the_file)

                    song = filename.replace('.mp3', '')
                    self.song_name_list.append(song)


    def play(self):
        pygame.init()
        pygame.mixer.init()

        self.Volume = pygame.mixer.music.get_volume() * 100

        song_number = self.song_number
        song_list = self.file_list
        song_name_list = self.song_name_list
        song_amount = len(song_list)
        Volume = self.Volume

        if not song_amount > 1:
            self.win.write_lines(f"Now playing: \n{song_list[0]}", 1)
            pygame.mixer.music.load(song_list[0])
            pygame.mixer.music.play()
        else:
            songToPlay = song_list[song_number]
            songName = song_name_list[song_number]
            print(songName)
            self.win.write_lines(f"Now playing: {songName}", 1)
            self.win.song = songName
            pygame.mixer.music.load(songToPlay)
            pygame.mixer.music.set_endevent ( pygame.USEREVENT )
            pygame.mixer.music.play()
            self.win.write_info(f"Song 1/{song_amount}")

            done = False
            clock = pygame.time.Clock()

            paused = False
            auto_play = False

            while not done:
                for event in pygame.event.get():
                    self.win.draw()
                    if event.type == pygame.MOUSEMOTION:
                        self.win.handle_event(event)

                    if event.type == pygame.USEREVENT:
                        if song_number < song_amount:
                            song_number += 1
                            songToPlay = song_list[song_number]
                            songName = song_name_list[song_number]
                            self.win.write_lines(f"Now playing: {songName}", 1)
                            self.win.song = songName
                            self.win.write_info(f"Song: {song_number + 1}/{song_amount}")
                            print(f"\nNew song: {songName}")
                            pygame.mixer.music.load(songToPlay)
                            pygame.mixer.music.set_endevent(pygame.USEREVENT)
                            pygame.mixer.music.play()
                        else:
                            self.win.write_lines("No more songs to play......")
                            time.sleep(4)

                    if event.type == pygame.KEYDOWN:
                       
                        if event.key == pygame.K_RIGHT:
                            self.win.write_lines("Skipping the song........", 2)
                            pygame.mixer.music.fadeout(2000)

                            # if song_number < song_amount:
                            #     song_number += 1
                            #     songToPlay = song_list[song_number]
                            #     songName = song_name_list[song_number]
                            #     self.win.write_lines(f"Now playing: {songName}", 1)
                            #     print(f"\nNew song: {songName}")
                            #     self.win.write_info(f"Song {song_number}/{song_amount}")
                            #     pygame.mixer.music.load(songToPlay)
                            #     pygame.mixer.music.set_endevent(pygame.USEREVENT)
                            #     pygame.mixer.music.play()
                            # else:
                            #     self.win.write_lines("No more songs to play......")
                            #     time.sleep(4)
                            #     done = True
                        
                        if event.key == pygame.K_LEFT:
                            self.win.write_lines("Skipping the song........", 2)
                            pygame.mixer.music.fadeout(2000)

                            if song_number < song_amount and song_number > -1:
                                song_number -= 1
                                songToPlay = song_list[song_number]
                                songName = song_name_list[song_number]
                                self.win.write_lines(f"Now playing: {songName}", 1)
                                print(f"\nNew song: {songToPlay}")
                                pygame.mixer.music.load(songToPlay)
                                pygame.mixer.music.play()
                            else:
                                self.win.write_lines("This is the first song......", 2)
                        
                        if event.key == pygame.K_SPACE:
                            if paused:
                                self.win.write_lines("Resuming........", 2)
                                time.sleep(.5)
                                pygame.mixer.music.unpause()
                                paused = False
                                self.win.write_lines("Resumed!", 2)
                            else:
                                self.win.write_lines("Pausing........", 2)
                                time.sleep(.5)
                                pygame.mixer.music.pause()
                                self.win.write_lines("Paused!", 2)
                                paused = True

                        if event.key == pygame.K_UP:
                            if Volume < 100:
                                Volume += 10
                                self.win.write_lines(f"Volume: {Volume}", 2)
                                pygame.mixer.music.set_volume(Volume / 100)
                        
                        if event.key == pygame.K_DOWN:
                            if Volume >= 0:
                                Volume -= 10
                                self.win.write_lines(f"Volume: {Volume}", 2)
                                pygame.mixer.music.set_volume(int(Volume / 100))

                        if event.key == pygame.K_a:
                            if not auto_play:
                                self.win.write_lines(f"Auto Play: On", 3)
                                auto_play = True
                            else:
                                self.win.write_lines(f"Auto Play: Off", 3)
                                auto_play = False

                    if event.type == pygame.QUIT:
                        pygame.mixer.music.stop()
                        done = True
                pygame.display.update()
                clock.tick(30)
            pygame.quit()
        
mp = music("lofi")
mp.find()
# mp.playall()
song_list = mp.song_list()
playList = playlist(song_list)
playList.play()

# player = playlist("Music Player")
# player.find()
# player.play(player)