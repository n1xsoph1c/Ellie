''' 
Youtube
==========
Downloads video from youtube and saves the video
on the video directory
:meth:`Ellie/E3P/Videos`
'''

import pytube 
import os

from urllib.request import Request, urlopen

VIDEO_DOWNLOADED = False

class YouTube_Downloader:
    def __self__(self):
        pass
        

    def get_video(self, url):
        global VIDEO_DOWNLOADED
        
        link = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        yt = pytube.YouTube(link.get_full_url())
        # yt = pytube.YouTube(url)
        # print("Downloading the video")
        # stream = yt.streams.first()
        self.name = yt.title
        # # print(self.name)
        # stream.download(f"{os.path.dirname(__file__)}\\Videos")
        # print(f"Video Downloaded to {os.getcwd()}\\Videos")
        # VIDEO_DOWNLOADED = True
 
    def get_video_name(self):
        return self.name
