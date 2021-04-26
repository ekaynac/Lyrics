# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:23:33 2021

@author: enes_
"""


import spotipy
import tkinter as tk

token = spotipy.util.prompt_for_user_token(username="pvtqqmad0m5cy9u18wasficu6",client_id='e441790dbf264ebd8f2d8d66b1a070bf',
                           client_secret='39ecb39fda5d4afa8ead68459d80d4ce',redirect_uri="http://localhost:8080",scope="user-read-currently-playing")

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-follow-read'
sp = spotipy.Spotify(auth=token)

import lyricsgenius
token = "zUlnosicoueSA3l0i_wOVgxLIdt2FzXL1xfaVxqNWoPH6V2lIJiLYQVW8DE7T74Q"
genius = lyricsgenius.Genius(token)

def Findlyrics():
    currently_playing_dict = sp.current_user_playing_track()
    
    currently_playing_song = currently_playing_dict["item"]["name"]
    currently_playing_artist = currently_playing_dict["item"]["artists"][0]["name"]
    
    song = genius.search_song(currently_playing_song, currently_playing_artist)
    
    return song.lyrics, currently_playing_artist, currently_playing_song

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x1000")
        self.text = tk.Text(self.root,height = 100, width = 100)
        self.button = tk.Button(self.root,
                                text="Yenile",
                                command=self.changeText)
        self.button.pack()
        self.text.pack(side="left")
        self.root.mainloop()
        

    def changeText(self):
        current_list = Findlyrics()
        self.text.delete(1.0,tk.END)
        self.text.insert(tk.END, current_list[0])

Test()