'''
1: function to create a text file from a list of URL 
2: function that reads the text file 
3: function to download a url
'''
from pytube import YouTube
import time
import threading
from log_download import *

# TASK 1: defined list of 10 URLs
url_list = [ 
'https://www.youtube.com/watch?v=HisYsqqszq0&ab_channel=Daretodo.Motivation',
'https://www.youtube.com/watch?v=nwPMKcYEkmw&ab_channel=WaltDisneyStudios',
'https://www.youtube.com/watch?v=Tk2lvByDN_g',
'https://www.youtube.com/watch?v=4x5kjvpQZ-4',
'https://www.youtube.com/watch?v=t5khm-VjEu4',
'https://www.youtube.com/watch?v=ndMKTnSRsKM&ab_channel=BBCEarth',
'https://www.youtube.com/watch?v=QF-oyCwaArU&ab_channel=WarnerBros.Pictures',
'https://www.youtube.com/watch?v=C8lm8MC6QOQ&ab_channel=SupermarketGuru',
'https://www.youtube.com/watch?v=rLXcLBfDwvE&ab_channel=TEDxTalks',
'https://www.youtube.com/watch?v=0aqiPyTJv8E&ab_channel=BBCNews'
]
# generates a text file of a list of urls
def create_file(urllist, file_name):
    # creates video_urls.txt file
    with open(file_name, 'w', encoding='utf-8') as urlfile:
        for text in urllist:
            urlfile.write(text + '\n')


# TASK 2: reads urls from the txt file
def readfile(file_name):
    print(f"\n Extracting urls....")
    with open(file_name, 'r') as readurlfile:
        url_list = [url.strip() for url in readurlfile.readlines()]
        for url in url_list:
            print(url)
    print(f'Extraction Completed.\n')


# # TASK 3: setup for single video download 
# def video_download(url, download_path, semaphore=None):

#     # calls the thread that is downloading current video
#     threadname = threading.current_thread().name

#     try:   
#         yt = YouTube(url)
        
#         # acquires semaphore before download starts when semaphore available
#         if semaphore:
#             semaphore.acquire()

#         # downloads a video
#         stream = yt.streams.get_highest_resolution()
#         print(f"Download started at: {time.strftime('%H:%M:%S')} ..........{yt.title}")
#         stream.download(output_path=download_path)
#         print(f"{yt.title} Download completed ")

#         # adds log to the logging txt file wghen download successful
#         log_of_downloads(url, download_success=True, thread_name=threadname)
    
#     except Exception as e:
#         # returns exception for unsuccessful downloads
#         log_of_downloads(url, download_success=False, thread_name=threadname)

#     finally:
#         # releases semaphore after download when semaphore available
#         if semaphore:
#             semaphore.release()





