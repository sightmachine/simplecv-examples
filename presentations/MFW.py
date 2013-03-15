from SimpleCV import *
import webbrowser
apikey="6b5d123910612ee2902df3ba088dbcb8"
face_count = 10
mfw = ImageSet()
cam = Camera()
count = 0

while count < face_count:
    img = cam.getImage()
    faces = img.findHaarFeatures('face')
    if faces is not None:
        faces[-1].draw(width=5)
        print count 
        mfw.append(faces[-1].crop().resize(128,128))
        count = count + 1
    img.show()

print "ALL DONE!"
mfw.save('myfacewhen.gif')
temp = Image('myfacewhen.gif')
urls = temp.upload('imgur',apikey)
webbrowser.open('http://www.twitter.com/')
webbrowser.open(urls[1])

