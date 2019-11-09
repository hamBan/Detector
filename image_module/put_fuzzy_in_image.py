from PIL import Image, ImageDraw, ImageFont

def put_fuzzy_in_image(image,fuzzy):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf",size=20)
    (x, y) = (10, 10)
    message = str(fuzzy)
    color = 'rgb(128, 128, 127)'
    draw.text((x, y), message, fill=color, font=font)
    return image