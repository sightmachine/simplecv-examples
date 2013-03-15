from SimpleCV import Image, Display, Color, Camera
cam = Camera(0) #Get the first camera
disp = Display((640,480)) # Create a 640x480 Display
while( disp.isNotDone() ):
    img = cam.getImage().binarize() # get an image
    img.drawText("Hello World!",40,40,
                 fontsize=60,color=Color.RED ) 
    img.save(disp) # show it
    