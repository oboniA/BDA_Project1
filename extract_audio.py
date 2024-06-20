import moviepy.editor as mp
import threading
import os
import time


def extraction(videofile, video_location):
    """audio extraction process for each video file"""

    try:
        # constructs video path using folder and file name
        print(f" Start extracting audio for {videofile}....")
        video_path = os.path.join(video_location, videofile) 

        # extracts audio from video path
        video= mp.VideoFileClip(video_path) 
        audio = video.audio

        # constructs output file path in .wav format
        out_filename= os.path.splitext(videofile)[0] + ".wav"
        print(f" Saving {out_filename}.......")
        out_path= os.path.join(video_location, out_filename)
        audio.write_audiofile(out_path, codec='pcm_s16le') # pcm_s16le for 16-bit WAV output
        print(f' Extraction complete; Audio file saved; Worker thread: {threading.current_thread().name}')

    except Exception as e:
        print(f' An error occured while processing {videofile}: {e}')
    
    print(f" Done")

   
def audio_extraction(video_location):
    """ Uses Threads to extract audios from every video file"""

    # lists all the videos in a specific directory
    # list comprehension: generates list of all subdirectories in a specified directory
    subdirs= [os.path.join(video_location, d) for d in os.listdir(video_location) 
              if os.path.isdir(os.path.join(video_location, d))]

    start=time.perf_counter()

    # creates threads for each process
    threads=[]
    for subdir in subdirs:
        # thread= threading.Thread(target=extraction, args=(videofile, video_location))
        # threads.append(thread)
        # thread.start()
        video_files= [file for file in os.listdir(subdir) 
                      if file.endswith('.mp4')]
        for video_file in video_files:
            thread= threading.Thread(target=extraction, args=(video_file, subdir))
            threads.append(thread)
            thread.start()

    # waits for all threads to complete operation
    for thread in threads:
        thread.join()
    
    end=time.perf_counter()
    print(f' Audio Extraction finished in {end-start} seconds\n')


    


