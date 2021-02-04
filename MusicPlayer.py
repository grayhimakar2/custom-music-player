# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:47:39 2020

@author: HuyDai
"""
import pygame
import tkinter as tkr
import os
import sys

def execute(folder_path):
    global is_pause
    is_pause = False
    """create main windows"""
    player = tkr.Tk()
    
    
    """edit window properties"""
    player.title("The Best App")
    # width x height + x_offset + y_offset:
    player.geometry("600x700+30+30")
    
    """get playlist songs"""
    #os.chdir(r"C:\Users\Envy3\Dropbox (MIT)\MIT\Freshman\Summer\Learning Creative Learning (LCL)\Week5\PlaylistSongs")
    os.chdir(folder_path)
    songlist = os.listdir()
    #print(songlist)
    
    """create volume slider"""
    def changeVolume(vol):
        pygame.mixer.music.set_volume(int(vol)/100)
        
    volumeLevel = tkr.Scale(player,from_=0, to_=100,orient=tkr.HORIZONTAL, resolution = 10, \
        label='Volume:',activebackground="blue",command=changeVolume,bg="violet",fg="black") 
        #set bound of volume level and allow change by 10% each time
    
    """create playlist"""
    playlist = tkr.Listbox(player,highlightcolor="green",selectmode=tkr.SINGLE) #restrict you to one selection
    
    pos = 0
    for song in songlist:
        playlist.insert(pos,song)
        pos += 1
    
    """pygame init"""
    pygame.init()
    pygame.mixer.init()
    
    """define commands"""
    
    def Play():
        global is_pause
        if not is_pause:
            pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
            pygame.mixer.music.set_volume(volumeLevel.get()/100)
            pygame.mixer.music.play()
            titlevar.set(playlist.get(tkr.ACTIVE)) #modify the titlevar holding current song title with tkr.ACTIVE
        else:
            pygame.mixer.music.unpause()
            is_pause = False
    def Pause():
        global is_pause
        is_pause = True
        pygame.mixer.music.pause()
        
    def UnPause():
        pygame.mixer.music.unpause()
    
    def Stop():
        pygame.mixer.music.stop()    
    
    """create buttons"""
    button1 = tkr.Button(player,bg="pale green", width=5,height=3, text="Play",command=Play)
    button3 = tkr.Button(player,bg="turquoise2",fg="black", width=5,height=3, text="Pause",command=Pause)
    button2 = tkr.Button(player,bg="chartreuse4",fg="white",width=5,height=3, text="Stop",command=Stop)
    button4 = tkr.Button(player,bg="black", width=5,height=3, text="Unpause",command=UnPause)
    
    
    """announce current song name"""
    #label1 = tkr.LabelFrame(player, text="Song Name") #create label frame
    #label1.pack(fill="both", expand="yes") #fill everything after stop button
    #contents1 = tkr.Label(label1, text=file1)
    titlevar = tkr.StringVar()
    songtitle = tkr.Label(player, textvariable=titlevar)
    
    
    """packing"""
    songtitle.pack(fill="x",padx=40)
    button1.pack(fill="x",padx=40, pady=5) #stretch the button to fill width of 
    volumeLevel.pack(fill="x",padx=40, pady=5)
    button3.pack(fill="x",padx=40, pady=5)
    #button4.pack(fill="x")
    button2.pack(fill="x", padx=40, pady=5)
    playlist.pack(fill="x",padx=40)
    
    """run"""
    player.mainloop()
    
if __name__ == "__main__":
    execute(sys.argv[1])