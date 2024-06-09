# TASK 4
import threading
from datetime import datetime

# destination file for downloaded logs
logfile= 'download_log.txt'

# mutex initiated
mutex= threading.Lock()

# function to entry the log in log file 
def log_of_downloads(url, download_success, thread_name, error_msg=None):

    # current date (of download)
    timestamp= datetime.now().strftime('%H:%M:%S, %d %B %Y')

    # cases when video is downloaded or failed
    if download_success:
        entry_log = f'"Thread_ID": {thread_name}, "TimeStamp": {timestamp}, "URL": "{url}", "Download": True\n'
    else:
        entry_log = f'"TimeStamp": {timestamp}, "URL": "{url}", "Download": False \n'

    # acquires lock
    mutex.acquire()
    try: 
        # updates log file after each download
        with open(logfile, 'a') as filelog:
            filelog.write(entry_log)
    finally:
        # releases lock
        mutex.release()



        

    

    
