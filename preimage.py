from PIL import Image,ImageDraw, ImageFont, ImageFilter
import numpy as np
import random


class ImageProcessing():
    def __init__(self,Img,tmpt2val={}):
        self.image = Img
        self.t2val = tmpt2val
        self.clearimg=""
        self.nparray=[]
        self.PictureList = []
    def twoValue(self,G):
        for y in xrange(0,self.image.size[1]):
            for x in xrange(0,self.image.size[0]):
                g = self.image.getpixel((x,y))
                if g > G:
                    self.t2val[(x,y)] = 1
                else:
                    self.t2val[(x,y)] = 0
    def clearNoise(self,N=4,Z=1):
        for i in xrange(0,Z):
            self.t2val[(0,0)] = 1
            self.t2val[(self.image.size[0] - 1,self.image.size[1] - 1)] = 1
            for x in xrange(1,self.image.size[0] - 1):
                for y in xrange(1,self.image.size[1] - 1):
                    nearDots = 0
                    L = self.t2val[(x,y)]
                    if L == self.t2val[(x - 1,y - 1)]:
                        nearDots += 1
                    if L == self.t2val[(x - 1,y)]:
                        nearDots += 1
                    if L == self.t2val[(x- 1,y + 1)]:
                        nearDots += 1
                    if L == self.t2val[(x,y - 1)]:
                        nearDots += 1
                    if L == self.t2val[(x,y + 1)]:
                        nearDots += 1
                    if L == self.t2val[(x + 1,y - 1)]:
                        nearDots += 1
                    if L == self.t2val[(x + 1,y)]:
                        nearDots += 1
                    if L == self.t2val[(x + 1,y + 1)]:
                        nearDots += 1
                    if nearDots < N:
                        self.t2val[(x,y)] = 1               
    def saveImage(self,filename,size=(100,100)):
        size = self.image.size
        tmpimage = Image.new("1",size)
        draw = ImageDraw.Draw(tmpimage)
        for x in xrange(0,size[0]):
            for y in xrange(0,size[1]):
                draw.point((x,y),self.t2val[(x,y)])
        self.clearimg = draw
        tmpimage.save(filename)
    def print_t2val(self):
        for y in self.nparray:
            print y
    def t2array(self):
        for y in xrange(0,self.image.size[1]):
            temp=[]
            for x in xrange(0,self.image.size[0]):
                temp.append(self.t2val[(x,y)]) 
            self.nparray.append(temp)
    def CharacterSegmentation(self,C=1,D=5):
        pixcount = self.image.size[0]*[0];
        for x in xrange(0,self.image.size[0]):
            for y in xrange(0,self.image.size[1]):
                if self.t2val[(x,y)] == 0:
                    pixcount[x] += 1
        if self.nparray==[]:self.t2array()
        step=maxs=0
        begin = []
        end   = []
        pixcount.append(0)
        for index,value in enumerate(pixcount):      
            if value >=C:
                if step==0:
                    begin.append(index) 
                step+=1
            if step>=D and value==0:
                if step>maxs: maxs=step
                step=0
                end.append(index) 
            if 0<step<D and value==0:
                if len(begin)>0:begin.pop()
                step=0
        a=np.array(self.nparray)
        for ii in xrange(len(begin)): 
            self.PictureList.append(a[:,begin[ii]:end[ii]])
        return self.PictureList
















