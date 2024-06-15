# Main File
from setup import *
from parallel import *
from extract_audio import *
from transcribe_audio import *


def main():
    # defined text file name
    filename='video_urls.txt'

    #Task 3
    parallel_download(filename, output_dir)

    #Task 5
    video_folder= "./parallel_download_outputs"
    audio_folder= "./Task5_downloads"
    
    audio_extraction(video_folder, audio_folder)
    audio_transcription(audio_folder)
    

if __name__=="__main__":
    main()