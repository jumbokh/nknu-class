# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:19:45 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
o=cv2.imread("00047.jpg",cv2.IMREAD_UNCHANGED)
k=np.ones((5,5),np.uint8)
r=cv2.morphologyEx(o,cv2.MORPH_GRADIENT,k)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()
