import cv2
import numpy as np

def getthresholdedimg(hsv):
    pink = cv2.inRange(hsv,np.array((339,91,55)),np.array((360,100,100)))
    return pink

c = cv2.VideoCapture(0)
#width,height = c.get(3),c.get(4)
#print "frame width and height : ", width, height

while True:
    _,f = c.read()
    f = cv2.flip(f,5)
    blur = cv2.medianBlur(f,7)
    hsv = cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
    pink = getthresholdedimg(hsv)
    erode = cv2.erode(pink,None,iterations = 4)
    dilate = cv2.dilate(erode,None,iterations = 10)

    contours,hierarchy = cv2.findContours(dilate,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        #cx,cy = x+w/2, y+h/2
        #if 100 < hsv.item(cy,cx,0) < 120:
        cv2.rectangle(f,(x,y),(x+w,y+h),(255,0,0),2)
        print "pink :", x,y,w,h

    cv2.imshow('img',f)

    if cv2.waitKey(25) == 27:
        break

cv2.destroyAllWindow
	
