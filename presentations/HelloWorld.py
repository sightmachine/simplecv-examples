from SimpleCV import Image, Display, Color, Camera
cam = Camera(0)                     # Get the first camera
disp = Display((640,480))           # Create a 640x480 display
while( disp.isNotDone() ):          # While we don't exit the display
    img = cam.getImage().binarize() # Get an image and make it black and white
    # Draw the text "Hello World" at (40,40) in red.
    img.drawText("Hello World!",40,40,
                 fontsize=60,color=Color.RED ) 
    img.save(disp)                  # Save it to the screen
    
