import sys
import os
import cv2
import PIL.Image
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from ImagePrediction import image_predictor
from VideoPrediction import video_predictor
# from LivePrediction import live_predictor

root = Tk()

root.title("UltraVision Detector")
root.geometry("400x400")

def ImagePrediction():
    ifile = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    path = ifile.name
    op = image_predictor(path)
    show_image()
    
    

def VideoPrediction():
    ifile = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    path = ifile.name
    op = video_predictor(path)
    print(op)
    

def LivePrediction():
    ip = simpledialog.askstring("IP Address", "Enter IP address")
    live_predictor(ip)




button1 = Button(root, text ="Image Prediction", command = ImagePrediction)
button2 = Button(root, text ="Video Prediction", command = VideoPrediction)
button3 = Button(root, text ="Live Prediction", command = LivePrediction)


button1.pack()
button2.pack()
button3.pack()
root.mainloop()
