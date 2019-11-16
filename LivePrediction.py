from datetime import datetime
import warnings
warnings.simplefilter(action='ignore')
import cv2
from PIL import Image
import urllib.request
from firebase import firebase
from image_module import image_prediction as imp
#firebase = firebase.FirebaseApplication('https://ultra-vision-38b0a.firebaseio.com/', None)
firebase = firebase.FirebaseApplication('https://supravision-detector.firebaseio.com/', None)

out = cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc(*"MJPG"), 10,(640,480))
n = 0
print("Begining Image Feed: ")
while n<50:
    image = Image.open(urllib.request.urlopen(""))
    image = image.resize((640, 480), Image.ANTIALIAS)
    l = imp.prediction(image)
    image_np = l[1]
    fuzzy = l[0]
    now = datetime. now()
    timestamp = datetime. timestamp(now)
    data =  {'FuzzyValue': fuzzy,'TimeStamp': timestamp}
    #result = firebase.post('/ultra-vision-38b0a/Customer/',data)
    result = firebase.post('supravision-detector/damageReport/',data)
    out.write(image_np)
    n+=1
    print("Frame ",n," Processed")