import speech_recognition as sr
import threading
import multiprocessing
import os
import time


def transcribe_audio(audio_file, audio_location):
    """audio transcription process from each audio file"""

    try:
        # constructs audio path from folder name and file name
        audio_path= os.path.join(audio_location, audio_file)
        
        print(f" Started extracting {audio_file}...")
        # opens an audio file and recognises it
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)

        # Recognize the speech in the audio file using Google Web Speech API
        text = recognizer.recognize_google(audio)

    except Exception as e:
        # exception handling
        print(f" Error while processing file {audio_file}: {e}")
    
    # constructs output file path in .txt format
    text_file = os.path.splitext(audio_file)[0] + '_.txt'
    out_path = os.path.join(audio_location, text_file)

    try:
        # writes the audio transcription in the .txt file
        with open(out_path, 'w') as file:
            file.write(text)

    except Exception as e:
        print(f' Error in writing transcription for {audio_file}')
   
    print(f' Successful for {audio_file}')
    

def audio_transcription(audio_location):
    """ Uses multiprocessing to extract texts from every audio file"""
    
    # list comprehension: generates list of all subdirectories in a specified directory
    subdirs= [os.path.join(audio_location, d) for d in os.listdir(audio_location) 
              if os.path.isdir(os.path.join(audio_location, d))]

    processes=[]
    start=time.perf_counter()
    print(f' Download started using MULTIPROCESSING......')
    for subdir in subdirs:
        audio_files= [file for file in os.listdir(subdir) 
                      if file.endswith('_.wav')]
        for audio_file in audio_files:
            process = multiprocessing.Process(target=transcribe_audio, args=(audio_file, subdir))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()

    end=time.perf_counter()
    print(f' Audio Transcription finished in {end-start} seconds\n')


