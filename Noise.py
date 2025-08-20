from PIL import Image, ImageDraw, ImageFont
import random
import math

class Perlin:


    def __init__(self,image,intervale,img,draw):
        self.image = image
        self.intervale = intervale
        self.img = img
        self.draw = draw
        self.vecteur = {}
        self.coins =[]
        self.ProduitScalaire = []
        self.pixel = []

    # def grille(self):
    #     for i in range(0, self.image[0], self.intervale):
    #         self.draw.line((i, 0, i, self.image[1]), fill="black", width=3)
    #     for i in range(0, self.image[1], self.intervale):
    #         self.draw.line((0, i, self.image[0], i), fill="black", width=3)

    def RandomPoint(self,x,y):
        theta = random.uniform(0, 2 * math.pi)
        return (math.cos(theta), math.sin(theta))


    def scalaire(self,v1,v2):
        return v1[0] * v2[0] + v1[1] *v2[1]



    def Vecteur(self):
        # for x in range(0, self.image[0], self.intervale):
        #     for y in range(0, self.image[1], self.intervale):
        #         px, py = self.RandomPoint(x, y)
        #         self.vecteur.append(((x, y), (px, py)))

        for cell_x in range(0, self.image[0], self.intervale):
            for cell_y in range(0, self.image[1], self.intervale):

                    # bornes de la cellule en pixels

                """x0, y0 = cell_x, cell_y
                x1, y1 = cell_x + self.intervale, cell_y + self.intervale"""
                self.draw.line((cell_x, 0, cell_x, self.image[1]), fill="black", width=3)
                self.draw.line((0, cell_y, self.image[0], cell_y), fill="black", width=3)



                Gx, Gy = self.RandomPoint(cell_x, cell_y)

                #self.coins.append([(x0, y0), (x1, y0), (x0, y1), (x1, y1)])
                #self.vecteur.append((Gx, Gy))
                self.vecteur[(cell_x, cell_y)] = (Gx, Gy)


                Gx = cell_x + Gx * self.intervale / 2
                Gy = cell_y+ Gy * self.intervale / 2
                self.draw.line((cell_x, cell_y, Gx, Gy), fill="red", width=3)

        for px in range(0,self.image[0]):
            for py in range(0,self.image[1]):
                cellu_x = (px // self.intervale) * self.intervale
                cellu_y = (py // self.intervale) * self.intervale

                x0, y0 = cellu_x, cellu_y
                x1, y1 = cellu_x + self.intervale, cellu_y + self.intervale
                self.pixel = []

                for i in [(x0, y0), (x1, y0), (x0, y1), (x1, y1)]:
                    if i in self.vecteur:
                        gradient = self.vecteur[i]
                        distance = px - i[0], py - i[1]
                        scalaire = self.scalaire(gradient, distance)
                        self.pixel.append(scalaire)


                moyenne = sum(self.pixel) / 4

                max_val = self.intervale / 2
                intensité = int((moyenne + max_val) / (2 * max_val) * 255)
                intensité = max(0, min(255, intensité))

                self.img.putpixel((px, py), (intensité, intensité, intensité))

#         for i,j in self.coins,self.vecteur:
#             Gradiant = [(i[0] - j[0], i[1] - j[1])]
#
#         for x in range(0,self.image[0]):
#             for y in range(0, self.image[0]):
#
#
#
#                         # boucle sur chaque pixel de la cellule
#                     """for px in range(x0, min(x1, self.image[0])):
#                         for py in range(y0, min(y1, self.image[1])):
#                             self.pixel = []
#                             for coin in self.coins:
#
#                                 dx = px - coin[0]
#                                 dy = py - coin[1]
#                                 scalaire = self.scalaire((Gx, Gy), (dx, dy))
#                                 self.pixel.append(scalaire)"""
#
#
#
# """"
#                             moyenne = (self.pixel[0]+self.pixel[1]+self.pixel[2]+self.pixel[3])/4
#
#                             max_val = self.intervale/2
#                             intensité = int((moyenne + max_val) / (2 * max_val) * 255)
#                             self.img.putpixel((px, py), (intensité, intensité, intensité))
# """
#
#
#
#
#
#
#                 # x0 = x
#                 # y0 = y
#                 # x1 = x + self.intervale
#                 # y1 = y + self.intervale
#                 #
#                 # self.coins.extend([(x0, y0), (x1, y0), (x0, y1), (x1, y1)])
#                 #
#                 #
#                 #
#                 #
#                 #
#                 # for i in [(x0, y0), (x1, y0), (x0, y1), (x1, y1)]:
#                 #     self.draw.line((i[0], i[1], px, py), fill="blue", width=3)
#                 #     scalaire1 = px * py + x1 * y0
#                 #     scalaire2 = px * py + x0 * y0
#                 #     scalaire3 = px * py + x1 * y1
#                 #     scalaire4 = px * py + x0 * y1
#
#
#
#
#
#
#
#
#
#
#                 #self.draw.line((x, y, px, py), fill="red", width=3)
#
#
#

