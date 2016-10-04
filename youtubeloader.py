#! -*- coding:utf-8 -*-

# tubeloader.py

import sys
import queue
import threading

from pytube import YouTube

__all__ = ["YtDownLoader"]


def item_settext_closer(func):
    setText = func
    if func is None:
        return None

    def wrapper(args):
        setText(args)

    return wrapper


class YtDownloader(threading.Thread):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.daemon = True
        self.queue = queue.Queue()

    def download(self, url, out_dir, progress=None, finish=None):
        self.queue.put((url, out_dir, progress, finish))

    def run(self):
        while True:
            url, out_dir, progress, finish = self.queue.get()

            yt = YouTube()
            yt.url = url
            video = yt.get('mp4')
            video.download(path=out_dir,
                           force_overwrite=True,
                           on_progress=item_settext_closer(progress),
                           on_finish=item_settext_closer(finish)
                           )
            self.queue.task_done()

    def stop(self, *args, **kw):
        # self.join()
        self._stop()


if __name__ == '__main__':
    url1 = 'https://www.youtube.com/watch?v=RvVfgvHucRY'
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
