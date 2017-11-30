from datetime import datetime
from time import sleep
from random import choice
from os import listdir
from os.path import join
from botUtils import *
from videoUpload import *

while True:
    while datetime.now().weekday() != 4:
        print "Apparently, it is still not SEXTA FEIRA, SUA LINDA..."
        sleep(28800)

    print "FINALLY ITS sexta feira!!!!!"
    while  datetime.today().hour != 18: 
        print "Still not HORA DO FINAL DO EXPEDIENTE..."
        sleep(1200)
    
    gif_path = join("gif", choice(listdir("gif"))) 
    video_tweet = VideoTweet(gif_to_clip(gif_path))
    video_tweet.upload_init()
    video_tweet.upload_append()
    video_tweet.upload_finalize()
    video_tweet.tweet()

    print "Posted. Time to sleep again..."
    sleep(86400)
