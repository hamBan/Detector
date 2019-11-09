import sys, getopt
import cv2
from PIL import Image
import urllib.request
#from firebase import firebase
from image_module import image_prediction as imp
#firebase = firebase.FirebaseApplication('https://ultra-vision-38b0a.firebaseio.com/', None)

print("Processing Image: ")
image = Image.open("test/testImage4.jpg")
image = image.resize((640, 480), Image.ANTIALIAS)
l = imp.prediction(image)
image_np = l[1]
fuzzy = l[0]
#data =  { 'FuzzyValue': fuzzy}
#result = firebase.post('/ultra-vision-38b0a/Customer/',data)
image = Image.fromarray(image_np)
image.save("output3.jpg")
print(fuzzy)
print("Done")