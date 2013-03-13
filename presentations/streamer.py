from SimpleCV import *
import webbrowser
import time
cam = JpegStreamCamera('http://192.168.1.1:8080/videofeed')
output = JpegStreamer("localhost:8888",st=0.1)
webbrowser.open("http://localhost:8888")
while True:
    img = cam.getImage()
    img.edges().invert().scale(2).dilate().save(output)
    time.sleep(0.01)
