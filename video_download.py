# TASK 3
import time
import os
import threading 
from pytube import YouTube
from concurrent.futures import ThreadPoolExecutor
from log_download import *


def folder_by_title(download_path, video_title):
    """Creates a folder for each video"""

    video_folder= video_title.rsplit('.', 1)[0]
    folder_path= os.path.join(download_path, video_folder)
    os.makedirs(folder_path, exist_ok=True)
    
    return folder_path


# TASK 3: setup for single video download 
def video_download(url, download_path, semaphore=None, download_mode='parallel'):
    """Downloads a video using a YouTube URL"""

    # calls the thread that is downloading current video
    threadname = threading.current_thread().name

    try:   
         # downloads a video
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        # makes folder by title of video and downloaded video saved in the folder
        video_title= stream.default_filename
        folder_path= folder_by_title(download_path, video_title)
        print(f" Download started at: {time.strftime('%H:%M:%S')} ..........{yt.title}")

        if semaphore:
             semaphore.acquire()

        if download_mode == 'parallel':
            video_filename= os.path.splitext(video_title)[0] + '_parallel.mp4'
        elif download_mode == 'serial':
            video_filename= os.path.splitext(video_title)[0] + '_serial.mp4'
        else:
            print(f"Download mode unavailable.")

        
        stream.download(output_path=folder_path, filename=video_filename)
        print(f" {yt.title} Download completed ")

        if download_mode == 'parallel':
            # adds log to the logging txt file wghen download successful
            log_of_downloads(url, download_success=True, thread_name=threadname)
    
    except Exception as e:
        # returns exception for unsuccessful downloads
        log_of_downloads(url, download_success=False, thread_name=threadname)
        print(f" Download uncessessful! Error: {e}")

    finally:
        # releases semaphore after download when semaphore available
        if semaphore:
            semaphore.release()

        
        
# Test SERIAL video download from txt file 
def serial_download(video_list, download_path):
     print(f' Serial Download Started....')
     start=time.perf_counter()
     
     # extract youtube URLs to download each serially
     with open(video_list, 'r') as readurlfile:
        url_list = [url.strip() for url in readurlfile.readlines()]
        for url in url_list:
            video_download(url, download_path, download_mode='serial')

     end=time.perf_counter()
     print(f' Serial download finished in {end-start} seconds\n')



# PARALLEL video download from txt file 
def parallel_download(video_list, download_path):
     """performs concurrent execution with threads to download videos from video_urls.txt"""
     
     # loads youtube URLs before downloading
     with open(video_list, 'r') as readurlfile:
        url_list = [url.strip() for url in readurlfile.readlines()]

     # 5 concurrent download using semaphore and same no. of worker threads
     max_download=5  
     p_semaphore = threading.BoundedSemaphore(max_download)
     start=time.perf_counter()
     print(f' PARALLEL Download Started....')

     # submits video_download func to execute concurrently using thread-pool
     with ThreadPoolExecutor(max_workers=max_download) as executor:
         parallel_downloads = [executor.submit(video_download, url, download_path, p_semaphore, download_mode='parallel') 
                                 for url in url_list]
         
         # main thread waits for all submitted downloads to be completed before moving on
         for download in parallel_downloads:
            download.result()
     
     end=time.perf_counter()
     print(f' Parallel download finished in {end-start} seconds\n')