import warnings
warnings.simplefilter(action='ignore')
import cv2
from PIL import Image
from image_module import image_prediction as imp
from datetime import datetime

video_path = "./output/video/"+str(datetime.now())+".avi"
out = cv2.VideoWriter(".output/video/output.avi",cv2.VideoWriter_fourcc(*"MJPG"), 10,(640,480))
def video_predictor(path):
    cap = cv2.VideoCapture(path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    n = 0
    print("Begining Image Feed: ")
    while True:
        ret,image = cap.read()
        if ret==False:
            break
        image = Image.fromarray(image)
        image = image.resize((640, 480), Image.ANTIALIAS)
        l = imp.prediction(image)
        image_np = l[1]
        fuzzy = l[0]
        out.write(image_np)
        n+=1
        print("Frame ",n," Processed of",length)