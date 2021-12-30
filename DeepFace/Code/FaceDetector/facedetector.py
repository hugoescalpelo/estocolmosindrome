import cv2
from deepface import DeepFace
import numpy as numpy

img_path="S:/Captura/recibido/hugo1.jpg"

#analyze = DeepFace.analyze(imgpath,actions=['emotion'],enforce_detection=True)
anll = DeepFace.analyze(img_path,actions=['emotion', 'age', 'gender', 'race'],models={},enforce_detection=True)
print ("result")
print (anll)
