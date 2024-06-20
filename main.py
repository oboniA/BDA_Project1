# Main File
from setup import *
from parallel import *
from extract_audio import *
from transcribe_audio import *
from analyse_sentiments import *
from translate_text import *
from extract_emotions import *


def main():
    # defined text file name
    filename='video_urls.txt'
    sub_folder= "./parallel_downloads"

    #Task 3
    parallel_download(filename, sub_folder)

    #Task 5
    audio_extraction(sub_folder)
    audio_transcription(sub_folder)
    sentiment_analysis(sub_folder)
    translate_to_spanish(sub_folder)
    emotion_extraction(sub_folder)

    audio_extraction_serial(sub_folder)
    audio_extraction_multiprocessing(sub_folder)
    audio_extraction_concurrency(sub_folder)
    

if __name__=="__main__":
    main()