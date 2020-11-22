import cv2
import os
import numpy as np
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create()
path='dataset'
def getImagewithId(path):
    imagepaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    
    
    for imagepath in imagepaths:
        faceimg=Image.open(imagepath).convert('L')
        faceNP=np.array(faceimg,'uint8')
        print(imagepath)
        ID=int(os.path.split(imagepath)[-1].split(".")[1])
        faces.append(faceNP)
        IDs.append(ID)
        cv2.imshow("training",faceNP)
        cv2.waitKey(10)
    return np.array(IDs),faces
Ids,faces=getImagewithId(path)
recognizer.train(faces,Ids)
recognizer.save('training_data.yml')
cv2.destroyAllWindows()