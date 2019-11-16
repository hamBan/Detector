import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from tkinter import Label

def show_image(path="./output/image/2019-11-16 20:35:42.200105.png",msg=""):
    # Create a window
    window = tkinter.Tk()
    window.title("Image and Morpho")

    # Load an image using OpenCV
    cv_img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)

    # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
    height, width, no_channels = cv_img.shape

    # Create a canvas that can fit the above image
    label = Label(window, text=msg)
    canvas = tkinter.Canvas(window, width = width, height = height)
    canvas.pack()
    label.pack()

    # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
    photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))

    # Add a PhotoImage to the Canvas
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    # Run the window loop
    window.mainloop()
