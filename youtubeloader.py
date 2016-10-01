#! -*- coding:utf-8 -*-

# tubeloader.py

import threading
import queue

import sys

from pytube import YouTube

__all__ =["YtDownLoader"]
def ytdownload(target_url, out_dir):

    yt = YouTube()
    yt.url = target_url
    video = yt.get('mp4')
    video.download(out_dir)
    print(" -- ytdownload fin.. {} --".format(target_url))
    return 'Finish'

class YtDownloader(threading.Thread):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.queue = queue.Queue()

    def download(self, url, out_dir):
        self.queue.put((url, out_dir))

    def run(self):
        print("run")
        while True:
            url, out_dir = self.queue.get()
            # download処理
            print("run {}".format(url))
            ytdownload(url, out_dir)


if __name__ == '__main__':
    url1 = 'https://www.youtube.com/watch?v=GHhD4PD75zY'
    url2 = 'https://www.youtube.com/watch?v=TN5ltss0NMA'
    url3 = 'https://www.youtube.com/watch?v=jQMU-Paa7sc'
    target_urls = [url1,url2,url3]

    out_dir = './'

    downloader = YtDownloader()
    downloader.start()

    # for target_url in target_urls:
    #     downloader.download(target_url, out_dir)

    print("Thread Start")
    # import time
    # time.sleep(60)
    # sys.eixt()
    while True:
        pass



