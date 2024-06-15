from textblob import TextBlob
import os
import threading
from googletrans import Translator
import time


def text_translation(speech_file, speech_location):
    """Translation process for each transciption file to spanish"""

    try:
        # constructs text path from folder name and file name
        speech_path= os.path.join(speech_location, speech_file)

        # read speech file containing audio transcription
        with open(speech_path, 'r') as sfile:
            text = sfile.read()

        # translation process
        blob = TextBlob(text)
        translator= Translator()
        blob_translated=translator.translate(blob.raw, dest='es') # translated result
        translated_str= str(blob_translated.text) # string format

        # constructs output file path
        text_file = os.path.splitext(speech_file)[0] + '_Spanish.txt'
        out_path = os.path.join(speech_location, text_file)
        with open(out_path, 'w', encoding="utf-8") as f:
            f.write(translated_str)
        print(f'\nTranslation complete for {speech_file}; Worker Thread: {threading.current_thread().name}')
            
    except Exception as e:
        print(f'Error in Translating {speech_file}: {e}')


def translate_to_spanish(speech_location):
    """ Uses Threads to translate every transcripted file"""

    # list comprehension: generates list of all subdirectories in a specified directory
    subdirs= [os.path.join(speech_location, d) for d in os.listdir(speech_location) 
              if os.path.isdir(os.path.join(speech_location, d))]
    
    threads=[]
    start= time.perf_counter()
    for subdir in subdirs:
        text_files= [file for file in os.listdir(subdir) 
                     if file.endswith('.txt') 
                     and '_sentiment_analysis' not in file
                     and '_Spanish.txt' not in file
                     and '_emotions.txt' not in file] 
        for text_file in text_files:
            thread= threading.Thread(target=text_translation, args=(text_file, subdir))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    end=time.perf_counter()
    print(f'Translation finished in {end-start} seconds\n')

    



