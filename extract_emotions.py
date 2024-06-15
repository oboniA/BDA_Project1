import os
import threading
import time
import spacy, nltk
from nrclex import NRCLex

nlp= spacy.load('en_core_web_sm')
nltk.download('punkt')

def text_emotion(speech_file, speech_location):
    """Translation process for each transciption file to spanish"""

    try:
        # constructs text path from folder name and file name
        speech_path= os.path.join(speech_location, speech_file)

        # read speech file containing audio transcription
        with open(speech_path, 'r') as sfile:
            text = sfile.read()

        doc = nlp(text)
        full_text = ' '.join([sent.text for sent in doc.sents])
        emotion = NRCLex(full_text)
        emo_freq= f"Detected Emotional Frequencies:\n{emotion.affect_frequencies}"

        # constructs output file path
        text_file = os.path.splitext(speech_file)[0] + '_Emotions.txt'
        out_path = os.path.join(speech_location, text_file)
        with open(out_path, 'w', encoding="utf-8") as f:
            f.write(emo_freq)
        print(f'\nEmotion Extraction complete for {speech_file}; Worker Thread: {threading.current_thread().name}')

    except Exception as e:
        print(f'Error in Translating {speech_file}: {e}')


def emotion_extraction(speech_location):
    """ Uses Threads to extract emotions of every transcripted file"""

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
            thread= threading.Thread(target=text_emotion, args=(text_file, subdir))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    end=time.perf_counter()
    print(f'Emotion Extraction finished in {end-start} seconds\n')
