# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt



# %%
img = cv.imread(cv.samples.findFile("./assets/bolhas.png"),0) # get picture grayscale = 0


if img is None: #checks picture has been apened 
    sys.exit("Could not read the image.")

img_modify = img.copy()


# %%

img_modify[200:210, 10:200] = 0

plt.subplot(231),plt.imshow(img, 'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(img_modify, 'gray'),plt.title('MODIFY')
plt.show()


# %%
img = cv.imread(cv.samples.findFile("./assets/bolhas.png"),1) # get picture color = 1

if img is None: #checks picture has been apened 
    sys.exit("Could not read the image.")

img_modify = img.copy()

img_modify[200:210, 10:200, 0] = 255 #R - red
img_modify[200:210, 10:200, 1] = 0 #B - black
img_modify[200:210, 10:200, 2] = 0 #G - green

plt.subplot(231),plt.imshow(img,),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(img_modify,),plt.title('MODIFY')
plt.show()


# %%



