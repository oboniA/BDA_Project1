from textblob import TextBlob
import os
import threading
import time


def text_analysis(speech_file, speech_location):
    """sentiment analysis process from each transciption file"""

    try:
        # constructs text path from folder name and file name
        speech_path= os.path.join(speech_location, speech_file)
    
        # read speech file containing audio transcription
        with open(speech_path, 'r') as sfile:
            text = sfile.read()

        # sentiment extraction from transcription
        blob = TextBlob(text)
        sentiments = blob.sentiment
        sentiment_text= f"'File': {speech_file}\n'Polarity': {sentiments.polarity}\n'Subjectivity': {sentiments.subjectivity}"

        # constructs output file path
        text_file = os.path.splitext(speech_file)[0] + '_sentiment_analysis.txt'
        out_path = os.path.join(speech_location, text_file)
        with open(out_path, 'w') as f:
            f.write(sentiment_text) # generates text file with analysis result
        print(f'\nSentiment Analysis complete for {speech_file}; Worker Thread: {threading.current_thread().name}')

    except Exception as e:
        print(f'Error while sentiment analysis for {speech_file}: {e}')
    

def sentiment_analysis(speech_location):
    """ Uses Threads for sentiment analysis from every transcription file"""

    # list comprehension: generates list of all subdirectories in a specified directory
    subdirs= [os.path.join(speech_location, d) for d in os.listdir(speech_location) 
              if os.path.isdir(os.path.join(speech_location, d))]
    
    threads=[]
    start= time.perf_counter()
    for subdir in subdirs:
        text_files= [file for file in os.listdir(subdir) 
                     if file.endswith('.txt') 
                     and '_sentiment_analysis.txt' not in file
                     and '_Spanish.txt' not in file
                     and '_emotions.txt' not in file] 
        for text_file in text_files:
            thread= threading.Thread(target=text_analysis, args=(text_file, subdir))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    end=time.perf_counter()
    print(f'Sentiment analysis finished in {end-start} seconds\n')
    


    