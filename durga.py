# -*- coding: utf-8 -*-
"""Durga.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dPxtoQCdKUECnYmaxf_XTp-lFHJDQ750
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

input_img=cv2.imread('/content/IMG_20220623_020416 (1).jpg')
input_img.ndim
input_img.shape
plt.figure(figsize=(20,8))
plt.imshow(input_img)

# Converting 3 dim to 2dim
img2d = input_img[:,:,0]
plt.figure(figsize=(20,8))
plt.imshow(img2d)

img_gray=cv2.cvtColor(input_img,cv2.COLOR_RGB2GRAY)
median_blur= cv2.medianBlur(img_gray,5)

# applying laplacian
laplacian_out = cv2.Laplacian(median_blur,cv2.CV_8U,-1)
laplacian_out.shape

plt.figure(figsize=(20,8))
plt.imshow(laplacian_out)

# sharpening image
img_sharpened = img2d + laplacian_out

plt.figure(figsize=(20,8))
plt.imshow(img_sharpened)

slobex=cv2.Sobel(median_blur,cv2.CV_16S,1,0,ksize=-1)
slobex_16S=np.absolute(slobex)
slobex_8U=np.uint8(slobex_16S)
slobex_8U.shape

mask_image =  img_sharpened * slobex_8U
plt.figure(figsize=(20,8))
plt.imshow(mask_image)

final = mask_image/255+img_sharpened/128
plt.figure(figsize=(20,8))
plt.imshow(final)