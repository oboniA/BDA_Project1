# list of 12 URLs from youtube 
url_list = [ 
'https://www.youtube.com/watch?v=HisYsqqszq0&ab_channel=Daretodo.Motivation',
'https://www.youtube.com/watch?v=nwPMKcYEkmw&ab_channel=WaltDisneyStudios',
'https://www.youtube.com/watch?v=Tk2lvByDN_g',
'https://www.youtube.com/watch?v=4x5kjvpQZ-4',
'https://www.youtube.com/watch?v=t5khm-VjEu4',
'https://www.youtube.com/watch?v=eyIvcxeMEs8',
'https://www.youtube.com/watch?v=ndMKTnSRsKM&ab_channel=BBCEarth',
'https://www.youtube.com/watch?v=AMvOp5noJS8',
'https://www.youtube.com/watch?v=QF-oyCwaArU&ab_channel=WarnerBros.Pictures',
'https://www.youtube.com/watch?v=C8lm8MC6QOQ&ab_channel=SupermarketGuru',
'https://www.youtube.com/watch?v=rLXcLBfDwvE&ab_channel=TEDxTalks',
'https://www.youtube.com/watch?v=0aqiPyTJv8E&ab_channel=BBCNews'
]


def create_file(urllist, file_name):
    """function to create a text file from a list of URL """

    print(f' Creating Text file: video_urls.txt')
    # creates video_urls.txt file
    with open(file_name, 'w', encoding='utf-8') as urlfile:
        for text in urllist:
            urlfile.write(text + '\n')
    print(f" Text file created with YouTube Video URLs\n")


def readfile(file_name):
    """reads the text file"""

    print(f" Read URLs....")
    with open(file_name, 'r') as readurlfile:
        url_list = [url.strip() for url in readurlfile.readlines()]
        for url in url_list:
            print(url)
    print(f' URLs loaded Successfully.\n')








