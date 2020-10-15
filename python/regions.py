# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# %%
img = cv.imread(cv.samples.findFile('./assets/biel.png'),0) #get picture in grayscale

if img is None: #checks picture has been apened 
    sys.exit("Could not read the image.")


img_modify = img.copy()


# %%
P1 = input()
P2 = input() # get point cartesian

V1 = P1.split(',')
V2 = P2.split(',') # string in list, split the ','


img_modify[int(V1[0]):int(V2[0]), int(V1[1]):int(V2[1])] = 255-img_modify[int(V1[0]):int(V2[0]), int(V1[1]):int(V2[1])]  # set negative img -> img = 255-img


plt.subplot(231),plt.imshow(img, 'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(img_modify, 'gray'),plt.title(' NEGATIVE')
plt.show()


# %%



