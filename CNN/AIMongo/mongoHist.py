# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 08:16:09 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import matplotlib.pyplot as plt
o=cv2.imread("G-Plant2_0616_98.jpg")
histb = cv2.calcHist([o],[0],None,[256],[0,255])
histg = cv2.calcHist([o],[1],None,[256],[0,255])
histr = cv2.calcHist([o],[2],None,[256],[0,255])
plt.plot(histb,color='b')
plt.plot(histg,color='g')
plt.plot(histr,color='r')
plt.show()

