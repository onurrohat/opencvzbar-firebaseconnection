from pickle import FALSE, TRUE
import cv2
import numpy as np
from pyzbar.pyzbar import decode


#test1 = cv2.imread('logo.png')

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

cap.set(3,640)
cap.set(4,480)
with open('myDataFile.text') as f :
    myDataList=f.read().splitlines()


while True:


    success,test1 = cap.read()
    for barcode in decode(test1):
       

        myData= barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList :
            print('verifiziert')
        else :
             print('nicht verifiziert')

             
        pts =np.array([barcode.polygon],np.int32)
        #BoundingBoxes
        pts=pts.reshape((-1,1,2))
        cv2.polylines(test1,[pts],True,(255,0,255),5)
        #Messages On Stream
        pts2= barcode.rect
        cv2.putText(test1,myData(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
        0.9,(255,0,255),2)
