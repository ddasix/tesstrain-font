import numpy as np
import cv2
import string
from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image

def write_text(img, text, x, y, font, color=(50, 50, 255), font_size = 32):
    font = ImageFont.truetype(font, font_size)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x, y - font_size), text, font = font, fill = color)
    img_tmp = np.array(img_pil)
    return img_tmp

def bounding_box(result, img, i, color = (0, 255, 0)):
    x = result['left'][i]
    y = result['top'][i]
    width = result['width'][i]
    height = result['height'][i]

    cv2.rectangle(img, (x, y), (x + width, y + height), color, 2)

    return x, y, img
def display(img, cmap='gray'):
    fig = plt.figure(figsize=(11.69,8.27), dpi=300) # A4 사이즈
    # fig = plt.figure(figsize=(16.53, 11.69), dpi=300)
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')

def clean_text(txt):
    whitespace = string.whitespace
    punctuation = "!#$%&\'()*+;<=>?[\\]^`{|}~“"
    table_whitespace = str.maketrans('', '', whitespace)
    table_punctuation = str.maketrans('', '', punctuation)
    text = str(txt)
    # text = text.lower()
    remove_whitespace = text.translate(table_whitespace)
    remove_punctuation = remove_whitespace.translate(table_punctuation)

    return str(remove_punctuation)
