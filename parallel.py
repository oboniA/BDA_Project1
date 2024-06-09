# TASK 3
from setup import *
import time
import os
import threading 
from concurrent.futures import ThreadPoolExecutor

# generated directory to store downloaded videos
output_dir='parallel_download_outputs'
os.makedirs(output_dir, exist_ok=True)

# PARALLEL video download from txt file 
def parallel_download(video_list,output_dir):
     
     # loads youtube URLs before downloading
     with open(video_list, 'r') as readurlfile:
        url_list = [url.strip() for url in readurlfile.readlines()]

     print(f'Parallel Download Started....')
     start=time.perf_counter()

     # 5 concurrent download
     max_download=5  
     p_semaphore = threading.BoundedSemaphore(max_download)
     
     # sets up worker threads to download 
     with ThreadPoolExecutor(max_workers=max_download) as executor:
         # submits video downloading to thread-pool
         download_in_parallel = [executor.submit(video_download, url, output_dir, p_semaphore) for url in url_list]
         
         # main thread waits for all submitted downloads to be completed before moving on
         for v_download in download_in_parallel:
            v_download.result()
    
     end=time.perf_counter()
     print(f'Parallel download finished in {end-start} seconds')