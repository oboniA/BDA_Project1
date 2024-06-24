import moviepy.editor as mp
import threading
import multiprocessing
import os
import time
import concurrent.futures


def extraction(videofile, video_location, exe_mode='threads'):
    """audio extraction process for each video file"""

    try:
        # constructs video path using folder and file name
        print(f" Start extracting audio for {videofile}....")
        video_path = os.path.join(video_location, videofile) 
        # extracts audio from video path
        video= mp.VideoFileClip(video_path) 
        audio = video.audio

        # constructs output file path 
        if exe_mode == 'multiprocessing':
            out_filename= os.path.splitext(videofile)[0] + "_.wav"
        elif exe_mode == 'serial':
            out_filename= os.path.splitext(videofile)[0] + "_serial.wav"
        elif exe_mode == 'threads':
            out_filename= os.path.splitext(videofile)[0] + "_threads.wav"
        elif exe_mode == 'concurrency':
            out_filename= os.path.splitext(videofile)[0] + "_concurrency.wav"
        else:
            raise ValueError(f'Invalid execution mode!')
        
        print(f" Saving {out_filename}.......")
        out_path= os.path.join(video_location, out_filename)
        audio.write_audiofile(out_path, codec='pcm_s16le') # pcm_s16le for 16-bit WAV output
        print(f' Extraction complete.')

    except Exception as e:
        print(f' An error occured while processing {videofile}: {e}')
    


def audio_extraction_multiprocessing(video_location):
    """ Uses Multiprocessing to extract audios from every video file"""

    # list comprehension: generates list of all subdirectories in a specified directory
    subdirs= [os.path.join(video_location, d) 
              for d in os.listdir(video_location) 
              if os.path.isdir(os.path.join(video_location, d))]
    
    processes=[]
    start=time.perf_counter()
    print(f' Download started using MULTIPROCESSING......')
    for subdir in subdirs:
        video_files= [file for file in os.listdir(subdir) 
                      if file.endswith('_parallel.mp4')]
        for video_file in video_files:
            process = multiprocessing.Process(target=extraction, args=(video_file, subdir, 'multiprocessing'))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()
    
    print(f' Download complete.')
    end=time.perf_counter()
    time_taken=end-start
    compare_time_log(time_taken, 'Audio Extraction Using Multiprocessing')
    print(f' Audio Extraction using MULTIPROCESSING finished in {time_taken} seconds\n')
   

def audio_extraction_threads(video_location):
    """ Uses Threads to extract audios from every video file"""

    subdirs= [os.path.join(video_location, d) 
              for d in os.listdir(video_location) 
              if os.path.isdir(os.path.join(video_location, d))]

    # creates threads for each process
    start=time.perf_counter()
    threads=[]
    for subdir in subdirs:
        video_files= [file for file in os.listdir(subdir) 
                      if file.endswith('_parallel.mp4')]
        for video_file in video_files:
            thread= threading.Thread(target=extraction, args=(video_file, subdir, 'threads'))
            threads.append(thread)
            thread.start()

    # waits for all threads to complete operation
    for thread in threads:
        thread.join()
    
    end=time.perf_counter()
    time_taken=end-start
    compare_time_log(time_taken, 'Audio Extraction Using Threads')
    print(f' Audio Extraction using THREADS finished in {time_taken} seconds\n')



def audio_extraction_serial(video_location):
    """ Serially extract audios from every video file"""

    subdirs= [os.path.join(video_location, d) 
              for d in os.listdir(video_location) 
              if os.path.isdir(os.path.join(video_location, d))]
    
    start=time.perf_counter()
    print(f' SERIAL download started......')
    for subdir in subdirs:
        for video in os.listdir(subdir):
            if video.endswith('_parallel.mp4'):
                extraction(video, subdir, exe_mode='serial')
    
    print(f' Download complete.')
    end=time.perf_counter()
    time_taken=end-start
    compare_time_log(time_taken, 'Audio Extraction Serially')
    print(f' Audio Extraction in SERIAL finished in {time_taken} seconds\n')



# def audio_extraction_multiprocessing(video_location):
#     """ Uses Multiprocessing to extract audios from every video file"""

#     subdirs= [os.path.join(video_location, d) 
#               for d in os.listdir(video_location) 
#               if os.path.isdir(os.path.join(video_location, d))]
    
#     processes=[]
#     start=time.perf_counter()
#     print(f' Download started using MULTIPROCESSING......')
#     for subdir in subdirs:
#         video_files= [file for file in os.listdir(subdir) 
#                       if file.endswith('_parallel.mp4')]
#         for video_file in video_files:
#             process = multiprocessing.Process(target=extraction, args=(video_file, subdir, 'multiprocessing'))
#             processes.append(process)
#             process.start()

#     for process in processes:
#         process.join()
    
#     print(f' Download complete.')
#     end=time.perf_counter()
#     time_taken=end-start
#     compare_time_log(time_taken, 'Audio Extraction Using Multiprocessing')
#     print(f' Audio Extraction using MULTIPROCESSING finished in {time_taken} seconds\n')



def audio_extraction_concurrency(video_location):
    """ Concurrently extract audios from every video file"""

    subdirs= [os.path.join(video_location, d) 
              for d in os.listdir(video_location) 
              if os.path.isdir(os.path.join(video_location, d))]
    
    print(f" CONCURRENT download started ......")
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for subdir in subdirs:
            video_files= [file for file in os.listdir(subdir) 
                    if file.endswith('_parallel.mp4')]
            for video_file in video_files:
                executor.submit(extraction, video_file, subdir, 'concurrency')
    
    print(f' Download complete.')
    end=time.perf_counter()
    time_taken=end-start
    compare_time_log(time_taken, 'Audio Extraction Using Concurrency')
    print(f' Audio Extraction using CONCURRENCY finished in {time_taken} seconds\n')



def compare_time_log(time_taken, method):
    """Creates a log file that records the time taken to execute each process
    Serial, Multiprocessing, Threads, and Concurrency"""

    logfile= 'compare_processes.txt'
    with open(logfile, 'a') as file:
        file.write(f' {method} : Extraction completed in {time_taken} seconds\n')


def compare_processes(cmp_filename):

    with open(cmp_filename, 'r') as readcmp:
        cmplist = [cmp.strip() for cmp in readcmp.readlines()]
        for cmp in cmplist:
            print(cmp)

    






    


