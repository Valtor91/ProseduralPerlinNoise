from PIL import Image, ImageDraw, ImageFont
from Noise import *


image = (1000, 500)
intervale = 10
img = Image.new("RGB", image, "white")
draw = ImageDraw.Draw(img)

PerlinNoise = Perlin(image,intervale,img,draw)


#PerlinNoise.grille()
PerlinNoise.Vecteur()





# Sauvegarder
img.save("dessin.png")
