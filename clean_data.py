from preimage import ImageProcessing
from PIL import Image,ImageDraw, ImageFont, ImageFilter
import numpy as np
import random

import glob  
picture=glob.glob('/mnt/hgfs/data/yixin/testset/*') 

traindata=[]
labe=[]
for pic in picture:
    pp = ImageProcessing(Image.open(pic).convert("L"))
    pp.twoValue(254)
    pp.clearNoise(N=3)
    feature=pp.CharacterSegmentation(C=1,D=4)
    if len(feature)==4:
        labe.extend([s.lower() for s in pic[29:33]])
        traindata.extend(feature)


ii=random.randint(0,100)
traindata[ii]
labe[ii]

len(traindata)
len(labe)

x=[]
maxstep=max([len(ii[0]) for ii in traindata])
for temp in traindata:
    completion=np.c_[temp[:,:],np.ones((30,maxstep-(len(temp[0]))),dtype=np.int32)]
    x.append(np.reshape(completion, (1, completion.shape[0]*completion.shape[1]))[0])

# for ii in xrange(0,len(x[0]),11):
#     print x[0][ii:ii+11]


import pickle
pickle.dump(x, open('/mnt/hgfs/data/yixin/traindata.pkl', 'wb'))
pickle.dump(labe, open('/mnt/hgfs/data/yixin/labe.pkl', 'wb'))


traindata = pickle.load(open('/mnt/hgfs/data/yixin/traindata.pkl', 'rb'))
labe      = pickle.load(open('/mnt/hgfs/data/yixin/labe.pkl', 'rb'))
