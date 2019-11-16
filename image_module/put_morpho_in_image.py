import platform
from PIL import Image, ImageDraw, ImageFont

def put_morpho_in_image(image,morpho):
    draw = ImageDraw.Draw(image)
    font_name = ""
    sys_type = platform.system()
    if(sys_type == "Linux"):
        font_name = "Ubuntu-R.ttf"
    elif(sys_type == "Windows"):
        font_name = "arial.ttf"
    else:
        font_name = "DroidSansFallbackFull.ttf"
   
    font = ImageFont.truetype(font_name,size=20)
    (x, y) = (10, 10)
    message = str(morpho)
    color = 'rgb(255, 0, 0)'
    draw.text((x, y), message, fill=color, font=font)
    return image