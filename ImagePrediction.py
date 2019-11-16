import sys, getopt
import cv2
from PIL import Image
import urllib.request
#from firebase import firebase
from image_module import image_prediction as imp
#firebase = firebase.FirebaseApplication('https://ultra-vision-38b0a.firebaseio.com/', None)

print("Processing Image: ")
image = Image.open("testImage2.jpg")
image = image.resize((640, 480), Image.ANTIALIAS)
l = imp.prediction(image)
image_np = l[1]
morpho = l[0]
#data =  { 'MorphologicalValue': morpho}
#result = firebase.post('/ultra-vision-38b0a/Customer/',data)
image = Image.fromarray(image_np)
image.save("outputx2.jpg")
print(morpho)
print("Done")