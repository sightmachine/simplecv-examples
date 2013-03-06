from SimpleCV import *
scaler = 0.5
cam = Camera()
disp = Display((640,480))
last = cam.getImage().scale(scaler)
sz = last.width/10
while disp.isNotDone():
    img = cam.getImage().scale(scaler)
    motion = img.findMotion(last,sz,method='HS')
    motion.draw(color=Color.RED,width=3)
    img.save(disp)
    last = img