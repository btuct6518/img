from PIL import Image 
import os



image_file = Image.open("curry.png") # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('result.png')