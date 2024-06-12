import moviepy.editor as mp
import os


def audio_extraction(video_location, audio_location):

    # directory will be created for audios
    os.makedirs(audio_location, exist_ok=True)

    # loops through the video volder
    for title in os.listdir(video_location):
         
        # constructs path with folder name and file name
        video_path = os.path.join(video_location, title)

        # constructs output file path
        out_filename= os.path.splitext(title)[0] + ".wav"
        out_path= os.path.join(audio_location, out_filename)

        # extracts audio from video
        video= mp.VideoFileClip(video_path)
        # pcm_s16le foir 16-bit WAV output
        video.audio.write_audiofile(out_path, codec='pcm_s16le')

        print(f'extraction complete')
    
    
    print(f'extracted Audio files saved to {audio_location}.')
