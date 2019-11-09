import warnings
warnings.simplefilter(action='ignore')
import cv2
from PIL import Image
import urllib.request
from firebase import firebase
from image_module import image_prediction as imp
firebase = firebase.FirebaseApplication('https://ultra-vision-38b0a.firebaseio.com/', None)
out = cv2.VideoWriter("FuzzyDetector/output2.avi",cv2.VideoWriter_fourcc(*"MJPG"), 10,(640,480))

n = 0
print("Begining Image Feed: ")
while n<50:
    image = Image.open(urllib.request.urlopen('http://192.168.43.184:8080/shot.jpg'))
    image = image.resize((640, 480), Image.ANTIALIAS)
    l = imp.prediction(image)
    image_np = l[1]
    fuzzy = l[0]
    data =  {'FuzzyValue': fuzzy}
    result = firebase.post('/ultra-vision-38b0a/Customer/',data)
    out.write(image_np)
    n+=1
    print("Frame ",n," Processed")