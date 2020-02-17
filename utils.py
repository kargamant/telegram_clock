from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from pytz import timezone

def form_time():
    return datetime.now(timezone('Europe/Moscow')).strftime('%H:%M')

def draw_avatar(text):
    image = Image.new('RGB', (500, 500), color='yellow')
    W, H = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='static/ds-digit.ttf', size=212)
    wt, ht = draw.textsize(text, font=font)
    draw.text(((W-wt)/2 , (H-ht)/2), text, font=font, fill='#A901DB')
    image.save('image_time.jpg')
