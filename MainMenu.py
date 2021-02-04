# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:49:20 2020

@author: Envy3
"""
import pygame
import tkinter as tkr
import os
import download_youtube_playlist
import convert_to_mp3
import MusicPlayer
import subprocess
import time

def execute():
    
    """create main windows"""
    player = tkr.Tk()
    
    runStat = tkr.StringVar()
    runStat.set("Status: Free")
    
    """edit window properties"""
    player.title("Mission Control")
    # width x height + x_offset + y_offset:
    player.geometry("600x700+30+30")
    
    """define actions"""
    def Submit1():
        runStat.set("Running..")
        folder_name = folder1.get("1.0","end-1c")
        #print(folder1.get("1.0","end-1c"))
        playlist_link = link1.get("1.0","end-1c")
        #print(link1.get("1.0","end-1c"))
        link_to_pass = "C:\\Users\\Envy3\\Music\\LCL_Week_5\\"+folder_name
        if not os.path.isdir(link_to_pass): 
            runStat.set("Downloading Youtube Playlist")
            download_youtube_playlist.execute(playlist_link)
            runStat.set("Converting files to mp3")
            convert_to_mp3.execute(folder_name)
        #p1 = subprocess.call(["python",'\"C:\\Users\\Envy3\\Dropbox (MIT)\\MIT\\Freshman\\Summer\\Learning Creative Learning (LCL)\\Week5.py\"',link_to_pass], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        runStat.set("Started Music Player")
        MusicPlayer.execute(link_to_pass)
        
    def Destroy():
        os.system("shutdown -l")
        print("Hello")
    """create buttons"""
    welcomelabel = tkr.Label(player, text="Welcome World Controller!",font="Helvetica 16 bold")
    welcomelabel2 = tkr.Label(player, text="What destruction will you bring today?",font="Helvetica 14 italic")
    
    title1 = tkr.Label(player, text="Music-induced Soma",font="SansSerif 14 underline")
    
    subtitle1 = tkr.Label(player, text="Playlist Link",font="SansSerif 12",anchor="w")
    subtitle2 = tkr.Label(player, text="Folder Name",font="SansSerif 12",anchor="w")
    
    link1 = tkr.Text(player, height=5, width=53, font="10")
    folder1 = tkr.Text(player, height=2, width=53, font="10")    
    submitbutton1 = tkr.Button(player,text="Initiate",font="10",command=Submit1)
    status1 = tkr.Label(player, textvariable=runStat, font="11")
    
    self_destruct = tkr.Button(player, text="Self-Destruct",font="Helvetica 11 italic",command=Destroy)
    
    """packing"""
    welcomelabel.pack(pady=(10,0))
    welcomelabel2.pack(pady=(0,10))
    title1.pack(pady=(0,5))
    subtitle2.pack(fill="both",padx=60)  
    folder1.pack(padx=10,pady=5)
    subtitle1.pack(fill="both",padx=60)    
    link1.pack(padx=10,pady=10)
    submitbutton1.pack(ipadx=5,ipady=3)   
    status1.pack(ipadx=10,ipady=5)
    
    self_destruct.pack(pady=30,side=tkr.BOTTOM)
    """run"""
    player.mainloop()
    
if __name__ == "__main__":
    execute()