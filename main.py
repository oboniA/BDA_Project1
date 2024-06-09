# Main File
from setup import *
from parallel import *

def main():
    # defined text file name
    filename='video_urls.txt'

    #Task 3
    parallel_download(filename, output_dir)
    
    
if __name__=="__main__":
    main()