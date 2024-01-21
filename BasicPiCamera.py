#This script utilizes and RTSP connection.  
#A Linux RTSP server must be setup on the device
#Takes a still capture of an image from the RTSP stream

import ffmpeg
import datetime
gdir = "/home/homeaccount/sounds/"
imagedir = "/home/homeaccount/images/"

stream_url = 'rtsp://192.168.0.158:8554/unicast'

width = 1920  # Replace with your desired width
height = 1080


def still_capture():
    xdate = datetime.datetime.now().strftime("%m%d%Y"+"-"+"%H%M%S")
    output_image = imagedir + 'snap' + xdate + '.jpg'
    ffmpeg.input(stream_url, t=0.1).output(output_image, vframes=1, vf='scale={}:{}'.format(width, height)).run()

still_capture()
