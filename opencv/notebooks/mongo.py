# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:50:21 2018

@author: 李立宗 lilizong@gmail.com
"""

import cv2
o=cv2.imread("00047.jpg",cv2.IMREAD_GRAYSCALE)
r1=cv2.Canny(o,128,200)
r2=cv2.Canny(o,32,128)
cv2.imshow("original",o)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()
