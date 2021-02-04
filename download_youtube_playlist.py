# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:53:08 2020

@author: Envy3


from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=nMUDnF9m94A')
# print(yt.title)
stream = yt.streams.first()
stream.download()
"""

import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
import urllib.request
import json
import urllib
import os
from pytube import YouTube
import sys

def execute(play_url):
    #extract playlist id from url
    #'https://www.youtube.com/playlist?list=PLrP8RyFc20FREdIi4cnVhWUFIVRh7dYds'
    url = str(play_url)
    query = parse_qs(urlparse(url).query, keep_blank_values=True)
    playlist_id = query["list"][0]
    
    print(f'get all playlist items links from {playlist_id}')
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "INSERT_YOUR_KEY_HERE")
    
    request = youtube.playlistItems().list(
        part = "snippet",
        playlistId = playlist_id,
        maxResults = 50
    )
    response = request.execute()
    
    playlist_items = []
    while request is not None:
        response = request.execute()
        playlist_items += response["items"]
        request = youtube.playlistItems().list_next(request, response)
    
    print(f"total: {len(playlist_items)}")
    playlist = [ f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
        for t in playlist_items]
    
    
    for link in playlist:
        #parse URl and query link
        title = ""
        params = {"format": "json", "url": link}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string
        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            title = data['title']
        
        #Make title Windows friendly
        title = title.strip()
        invalid_chars = ["<",">",":","\"","/","\\","|","?","*","(",")","."]
        for char in invalid_chars:
            title = title.replace(char,"")
        print("Title:",title)
    
        
        #download video
        yt = YouTube(link)
        
        if not os.path.exists(str(yt.streams.first().title+'.mp4')) and not os.path.exists(title+'.mp4'):
            stream = yt.streams.first()
            stream.download()
            if os.path.exists("Youtube.mp4"):
                os.rename(yt.streams.first().title+".mp4", title+".mp4")
        else:
            print("The file already exists.")
        
if __name__ == "__main__":
    execute(sys.argv[1])
        
