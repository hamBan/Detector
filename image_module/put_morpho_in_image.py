from PIL import Image, ImageDraw, ImageFont

def put_morpho_in_image(image,morpho):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf",size=20)
    (x, y) = (10, 10)
    message = str(morpho)
    color = 'rgb(255, 0, 0)'
    draw.text((x, y), message, fill=color, font=font)
    return image