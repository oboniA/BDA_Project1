# Main File
from load_videos import *
from video_download import *
from extract_audio import *
from transcribe_audio import *
from analyse_sentiments import *
from translate_text import *
from extract_emotions import *


def main():
    # defined text file name
    filename='video_urls.txt'
    sub_folder= "./downloads"
    compare_log= 'compare_processes.txt'

    # Task 1
    create_file(url_list, filename)

    # task 2
    readfile(filename)

    #Task 3 and 4
    serial_download(filename, sub_folder)
    parallel_download(filename, sub_folder)

    # #Task 5
    audio_extraction_multiprocessing(sub_folder)
    audio_extraction_serial(sub_folder)
    audio_extraction_threads(sub_folder)
    audio_extraction_concurrency(sub_folder)
    compare_processes(compare_log)

    audio_transcription(sub_folder)
    sentiment_analysis(sub_folder)
    translate_to_spanish(sub_folder)
    emotion_extraction(sub_folder)

    
if __name__=="__main__":
    main()