#-*-coding:utf8-*-
#!/usr/bin/python
# Author : Jeonghoonkang, github.com/jeonghoonkang

import sys, os
sys.path.insert(0, '/home/pi/Downloads/github/RaspberryPi')
#import textindex

from time import strftime, localtime, sleep
import picamera
import datetime

pic = '/home/pi/Downloads/github/RaspberryPi/%s_cam_shot.jpg'

if len(sys.argv) is 1:
	print '   *****'
	print '    A picture has default file name in default path.'
	print '     '+pic
	print '   *****'

elif len(sys.argv) > 2:
	print '   Insert only the file name with directory where you want to save a picture in'
	print '   default :'+pic

else:
	pic = sys.argv[1]


foto_cnt = 0

camera =  picamera.PiCamera() 
camera.resolution = (1280, 720)
camera.rotation = 0
_num = 137

while True:
    _num += 1
    camera.start_preview()
    sleep(3)
    camera.stop_preview()
    time = strftime("%Y-%m%d-%H:%M", localtime())
    #print(type(time))
    #print(pic)
    camera.capture(pic %_num)
    print '\n A picture was saved at ' + pic %_num

    sleep(0.1)
