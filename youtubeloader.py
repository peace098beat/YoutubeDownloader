#! -*- coding:utf-8 -*-

# tubeloader.py

import threading
import queue

import sys

from pytube import YouTube

__all__ = ["YtDownLoader"]

from sys import stdout
from time import clock


def print_status(progress, file_size, start):

    percent_done = int(progress) * 100. / file_size
    dt = (clock() - start)
    if dt > 0:
        stdout.write("{:0.0f}% {:0.0f}[s]\n".format(percent_done, dt))
    stdout.flush()

class YtDownloader(threading.Thread):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.daemon = True
        self.queue = queue.Queue()

    def download(self, url, out_dir):
        self.queue.put((url, out_dir))

    def run(self):
        print("run")
        while True:
            url, out_dir = self.queue.get()
            # download処理
            print("run {}".format(url))
            yt = YouTube()
            yt.url = url
            video = yt.get('mp4')
            video.download(path=out_dir,
                           force_overwrite=True,
                           on_progress=print_status,
                           on_finish=None)

    def stop(self, *args, **kw):
        # self.join()
        self._stop()
        pass

if __name__ == '__main__':
    url1 = 'https://www.youtube.com/watch?v=kdCaBvN4GcE'
    # url2 = 'https://www.youtube.com/watch?v=TN5ltss0NMA'
    target_urls = [url1]

    out_dir = './'

    downloader = YtDownloader()
    # downloader.daemon = True
    downloader.start()

    for target_url in target_urls:
        downloader.download(target_url, out_dir)

    print("Thread Start")
    import time
    time.sleep(4)

    sys.exit()
    # while True:
    # pass
