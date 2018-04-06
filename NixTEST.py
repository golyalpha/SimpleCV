import SimpleCV
cam = SimpleCV.Camera()
disp = SimpleCV.Display()
while disp.isNotDone():
    cam.getImage().save(disp)
