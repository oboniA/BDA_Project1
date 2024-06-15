import moviepy.editor as mp
import threading
import os
import time


def folder_by_title(folder, folder_name):
    path= os.path.join(folder, folder_name)
    os.makedirs(path, exist_ok=True)
    return path


def extraction(videofile, video_location, audio_location):
    """audio extraction process for each video file"""

    try:
        # creates a folder for subtasks for the video
        video_name= os.path.splitext(videofile)[0]
        save_folder=folder_by_title(audio_location, video_name)
            
        # constructs output file path in .wav format
        out_filename= os.path.splitext(videofile)[0] + ".wav"
        out_path= os.path.join(save_folder, out_filename)
        
        video_path = os.path.join(video_location, videofile) # constructs video path using folder and file name
        video= mp.VideoFileClip(video_path) # extracts audio from video path
        video.audio.write_audiofile(out_path, codec='pcm_s16le') # pcm_s16le for 16-bit WAV output
        print(f' Extraction complete; Audio files saved; Worker thread: {threading.current_thread().name}')

    except Exception as e:
        print(f'An error occured while processing {videofile}: {e}')
    
    print(f"Done")

   
def audio_extraction(video_location, audio_location):
    """ Uses Threads to extract audios from every video file"""

    # lists all the videos in a specific directory
    video_list= [video_name for video_name in os.listdir(video_location)]

    start=time.perf_counter()

    # creates threads for each process
    threads=[]
    for videofile in video_list:
        thread= threading.Thread(target=extraction, args=(videofile, video_location, audio_location))
        threads.append(thread)
        thread.start()

    # waits for all threads to complete operation
    for thread in threads:
        thread.join()
    
    end=time.perf_counter()
    print(f'Audio Extraction finished in {end-start} seconds\n')


    


