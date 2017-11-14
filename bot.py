from datetime import datetime
from time import sleep
from random import choice
from os import listdir
from botUtils import *
from videoUpload import *

while True:
    while datetime.now().weekday() != 4:
        print "Apparently, it is still not SEXTA FEIRA, SUA LINDA. Gotta sleep a little more..."
        sleep(28800)

    print "FINALLY ITS sexta feira!!!!!"
    while  datetime.today().hour != 18: 
        print "Still not HORA DO FINAL DO EXPEDIENTE..."
        sleep(1200)
    videoTweet = VideoTweet(gifToClip("gif/" + choice(listdir("gif/"))))
    videoTweet.upload_init()
    videoTweet.upload_append()
    videoTweet.upload_finalize()
    videoTweet.tweet()
    print "Posted. Time to sleep again..."
    sleep(86400)
