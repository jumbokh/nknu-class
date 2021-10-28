# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:06:47 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
#输出边缘和结构信息
import cv2
import numpy as np
o = cv2.imread('G-Plant2_0616_98.jpg')  
cv2.imshow("original",o)
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,100,120,cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  
n=len(contours)
contoursImg=[]
for i in range(n):
    temp=np.zeros(o.shape,np.uint8)
    contoursImg.append(temp)
    contoursImg[i]=cv2.drawContours(
            contoursImg[i],contours,i,(255,255,255),5) 
    cv2.imshow("contours[" + str(i)+"]",contoursImg[i])    
cv2.waitKey()
cv2.destroyAllWindows()