import speech_recognition as sr
import os


def speech_from_audio(audio_location, speech_location):

    # directory will be created for speech from audios
    os.makedirs(speech_location, exist_ok=True)

    recognizer = sr.Recognizer()

    # loops through the audio older
    for audio_title in os.listdir(audio_location):

        # constructs path with folder name and file name
        audio_path= os.path.join(audio_location, audio_title)

        try:
            # opens an audio file
            with sr.AudioFile(audio_path) as source:
                audio = recognizer.record(source)

            # Recognize the speech in the audio file using Google Web Speech API
            text = recognizer.recognize_google(audio)

        except Exception as e:
            # exception handling
            print(f"Error while processing file {audio_title}: {e}")
            text = ""

        # constructs output file path
        text_file = os.path.splitext(audio_title)[0] + '.txt'
        out_path = os.path.join(speech_location, text_file)

        with open(out_path, 'w') as f:
            f.write(text)
        
        print(f'Speech extraction Successful for {audio_title}')
    
    print(f'Audio Transcription Complete.')
    


