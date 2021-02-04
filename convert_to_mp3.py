# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 23:01:43 2020

@author: Envy3
"""


from os import listdir, path, system
import subprocess
import sys

def execute(folder_name):
    mp4files = [f for f in listdir('.') if str(f).endswith(".mp4")]

    for file in mp4files:
        print("Working on file:",file)
        mypath= path.abspath(file)
        ffmpeg = '\"C:\\Users\\Envy3\\Dropbox (MIT)\\MIT\\Freshman\\Summer\\ffmpeg\\bin\\ffmpeg.exe\"'
        str1 = ffmpeg +" -y -i \""+file+"\" -q:a 0 -map a \""+file.split('.mp4')[0]+".mp3\" && del /f \""+file+"\""
        #out = system(str1)
        #print(out)
        
        
        #command = [ffmpeg,'-i','\"'+mypath+'\"','-q:a','0','-map','a','\"'+mypath.split('.mp4')[0]+'.mp3\"']
        #print(' '.join(command))
        proc = subprocess.check_call(str1,shell=True,stdout=subprocess.PIPE)
    
    mov_command = "md C:\\Users\\Envy3\\Music\\LCL_Week_5\\"+folder_name+"\\ 2>nul & "+"move *.mp3 C:\\Users\\Envy3\\Music\\LCL_Week_5\\"+folder_name
    print(mov_command)
    proc = subprocess.check_call(mov_command,shell=True,stdout=subprocess.PIPE)
    
if __name__ == "__main__":
    execute(sys.argv[1])