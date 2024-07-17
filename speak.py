import pygame
from os.path import exists, dirname,join
import os
from gtts import gTTS
from pygame.locals import *
import requests
#from message import Message

script_dir = dirname(__file__)
target_dir = join(script_dir, '.\sounds')

class Speak:
    def __init__(self):

        if not exists(target_dir):
            os.mkdir(target_dir)

        if exists(target_dir):
            if self.has_internet_connection():
                pass
            else:
                #self.msg.show_message_box("No Internet", "You are not connected to the internet")
                print("You are not connected to the internet")
                        


    def has_internet_connection(self) -> bool:
        """
        Function to check internet connectivity.
        :return: True if internet is available, False otherwise
        """
        try:
            requests.get("http://www.google.com", timeout=5)
            return True
        except requests.ConnectionError as e:
            return False
        
    def save_mp3(self, phrase):
        mp3_path = join(target_dir, f'{phrase}.mp3')
        try:
            tts = gTTS(text=phrase, lang='en')
            tts.save(mp3_path)
            print(mp3_path)
            return True
        except Exception as e:
            print(f"Could not save {phrase}: {e} ")
            return False

    def play_mp3(self,word) -> None:
        """
        Function to play the saved mp3 file that matches the word
        :param word: the word that wants to be played
        """
        try:
            if word != "":
                pygame.mixer.pre_init(13000, -16, 2, 2048) # setup mixer to avoid sound lag
                pygame.init()
                pygame.mixer.init()
                script_dir = dirname(__file__)
                mp3_path = join(script_dir, '.\sounds', f'{word}.mp3')
                pygame.mixer.music.load(mp3_path)
                pygame.mixer.music.play()
                return
        except Exception as e:
            print(f'Could not play {word}: {e}')  
            return
