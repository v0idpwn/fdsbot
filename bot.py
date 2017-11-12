from datetime import datetime
from time import sleep
from random import choice
from os import listdir
from botUtils import *
from videoUpload import *


while datetime.today().weekday() != 4:
    print "Apparently, it is still not SEXTA FEIRA, SUA LINDA. Gotta sleep a little more..."
    sleep(43200)

print "FINALLY ITS sexta feira!!!!!"
videoTweet = VideoTweet(gifToClip("gif/" + choice(listdir("gif/"))))
videoTweet.upload_init()
videoTweet.upload_append()
videoTweet.upload_finalize()
videoTweet.tweet()
sleep(43200)
