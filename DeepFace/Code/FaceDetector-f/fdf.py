import sys, getopt
import cv2
from deepface import DeepFace
import numpy as numpy
import pandas as pd

def main (argv):
    img_src = ''

    try:
        opts, args = getopt.getopt(argv,"hi:",["imgsrc="])
    except getopt.GetoptError:
        print ('fdf.py -i <img_src>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <img_src>')
            sys.exit()
        elif opt in ("-i", "--imgsrc"):
            img_src = arg
    
    anll = DeepFace.analyze(img_src,actions=['emotion', 'age', 'gender', 'race'], models={},enforce_detection=False)

    anl = pd.DataFrame(anll)
    result = anl.to_json(orient="index")
#img_path="S:/Captura/recibido/hugo1.jpg"
    #print ("result")
    print (result)
    return result

if __name__ == "__main__":
    main(sys.argv[1:])