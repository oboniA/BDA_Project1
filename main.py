# Main File
from setup import *
from parallel import *
from extract_audio import *


def main():
    # defined text file name
    filename='video_urls.txt'

    #Task 3
    parallel_download(filename, output_dir)

    # Task4
    video_folder= os.path.join(".", "parallel_download_outputs")
    audio_folder= os.path.join(".", "audio_outputs")
    audio_extraction(video_folder, audio_folder)
    
    
if __name__=="__main__":
    main()