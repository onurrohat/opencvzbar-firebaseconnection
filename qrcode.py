import cv2
import numpy as np
from pyzbar.pyzbar import decode
import pandas as pd

import os
from firebase import firebase

fb_app = firebase.FirebaseApplication('https://mec427inventorymanagement-default-rtdb.europe-west1.firebasedatabase.app/',None)



#test1 = cv2.imread('logo.png')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap.set(3,640)
cap.set(4,480)

outputlist = []
        
while True:

    success,test = cap.read()
    
    grayscale=cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)
    for barcode in decode(grayscale):
       

        myData= barcode.data.decode('utf-8')
        #print(myData)
        #barcodedata = pd.DataFrame(myData)
        #file_name = 'Kitap1.xlsx'

        #barcodedata.to_excel('Kitap.xlsx',sheet_name="Sheet1")
        #print('Data exported into database succesfully')
        #barcodedata(barcodedata)
        #barcodedata.count()

        pts =np.array([barcode.polygon],np.int32)
        #BoundingBoxes
        pts=pts.reshape((-1,1,2))
        cv2.polylines(grayscale,[pts],True,(255,0,255),5)
        #Messages On Stream
        pts2= barcode.rect
        cv2.putText(grayscale,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
        0.9,(255,0,255),2)
        
        outputlist.append(myData)
        outputlist=list(dict.fromkeys(outputlist)) #delete duplicates from a list
        
        productsnumber = len(outputlist) 

        print(outputlist)
        print(productsnumber)

        mystring =''
        for x in outputlist :
            mystring += "     "+ x+  "     "

        print(mystring)
        #outputlist.append(myData)
        #if(outputlist.sort!=outputlist.sort):
                #send list again to firebase
                #outputlist.append(myData)
                #print(outputlist)
                #print(productsnumber)
        #else:
            #print("No Change Detected")
        send_to_firebase = fb_app.post("/QR Code/totalnum",productsnumber)
        
        send_to_firebase = fb_app.post("/QR Code/outputs",mystring)

        
       
            
            
        

        


    cv2.imshow('Result',grayscale)
    cv2.waitKey(30)

    

   










