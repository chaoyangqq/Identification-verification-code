from preimage import ImageProcessing
from PIL import Image,ImageDraw, ImageFont, ImageFilter
import numpy as np
from sklearn.externals import joblib
allclc = joblib.load('/mnt/hgfs/data/yixin/allclc.pkl')

import glob  
picture=glob.glob('/mnt/hgfs/data/yixin/predict/*') 

traindata=[]
for pic in picture:
    pp = ImageProcessing(Image.open(pic).convert("L"))
    pp.twoValue(254)
    pp.clearNoise(N=3)
    # pp.saveImage("/mnt/hgfs/data/yixin/testset/tmp.jpg")
    # Image.open("/mnt/hgfs/data/yixin/testset/tmp.jpg").show()
    feature=pp.CharacterSegmentation(C=1,D=4)
    if len(feature)==4:
        traindata.append(feature)


result=[]
maxstep=41
for data in traindata:
    retemp=[]
    for temp in data:
        if len(temp[0])<maxstep:
            completion=np.c_[temp[:,:],np.ones((30,maxstep-(len(temp[0]))),dtype=np.int32)]
            retemp.append(np.reshape(completion, (1, completion.shape[0]*completion.shape[1]))[0])
        else:
            completion=temp[:,:maxstep]
            retemp.append(np.reshape(completion, (1, completion.shape[0]*completion.shape[1]))[0])
    result.append(retemp)


labe=[]
for one in result:
    labe.append("".join(list(allclc.predict(one))))





