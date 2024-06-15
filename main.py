# Main File
from setup import *
from parallel import *
from extract_audio import *
from transcribe_audio import *
from analyse_sentiments import *
from translate_text import *


def main():
    # defined text file name
    filename='video_urls.txt'

    #Task 3
    #parallel_download(filename, output_dir)

    #Task 5
    video_folder= "./parallel_download_outputs"
    sub_directory = "./Task5_downloads"

    #audio_extraction(video_folder, sub_directory)
    #audio_transcription(sub_directory)
    sentiment_analysis(sub_directory)
    translate_to_spanish(sub_directory)
    
    
if __name__=="__main__":
    main()