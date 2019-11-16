import sys, getopt
import cv2
import urllib.request

from tkinter import *
from PIL import Image
from datetime import datetime
#from firebase import firebase
from image_module import image_prediction as imp
#firebase = firebase.FirebaseApplication('https://ultra-vision-38b0a.firebaseio.com/', None)

def image_predictor(path):

    print("Processing Image: ")
    image = Image.open(path)
    image = image.resize((640, 480), Image.ANTIALIAS)
    l = imp.prediction(image)
    image_np = l[1]
    morpho = l[0]
    #data =  { 'MorphologicalValue': morpho}
    #result = firebase.post('/ultra-vision-38b0a/Customer/',data)
    image = Image.fromarray(image_np)
    image_path = "./output/image/"+str(datetime.now())+".png"
    image.save(image_path)
    print(morpho)
    print("Done")