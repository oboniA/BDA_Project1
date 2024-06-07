import time
import os
from setup import *

# videos downloaded serially in the directory
output_dir='serial_outputs_test'
os.makedirs(output_dir, exist_ok=True)

# SERIAL video download from txt file 
def serial_download(video_list, output_dir):
     
     print(f'Serial Download Started....')
     start=time.perf_counter()
     
     # extract youtube URLs to download each serially
     with open(video_list, 'r') as readurlfile:
        url_list = [url.strip() for url in readurlfile.readlines()]
        for url in url_list:
            video_download(url, output_dir)

     end=time.perf_counter()
     print(f'Serial download finished in {end-start} seconds')


if __name__=="__main__":
    
    # defined text file name
    filename='video_urls.txt'
    
    # Task 1
    create_file(url_list, filename)

    #Task 3: serial download Testing
    serial_download(filename, output_dir)
