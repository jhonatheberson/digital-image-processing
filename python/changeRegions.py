# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np # import numpy
import cv2 as cv #import OpenCV 
from matplotlib import pyplot as plt #import pyplot




# %%
img = cv.imread(cv.samples.findFile('./assets/biel.png'),0) #get picture in grayscale

if img is None: #checks picture has been apened 
    sys.exit("Could not read the image.")


img_modify = img.copy()


# %%
data_img = img_modify.shape
mid_x = data_img[0]/2
mid_y = data_img[0]/2


print(mid_x)


# %%


part_0 = img[0:int(mid_x), 0:int(mid_x)]
part_1 = img[0:int(mid_x), int(mid_y):data_img[1]]
part_2 = img[int(mid_x):data_img[0], 0:int(mid_y)]
part_3 = img[int(mid_x):data_img[0], int(mid_y):data_img[1]]

img_modify[0:int(mid_x), 0:int(mid_y)] = part_3
img_modify[0:int(mid_x), int(mid_y):data_img[1]] = part_2
img_modify[int(mid_x):data_img[0], 0:int(mid_y)] = part_1
img_modify[int(mid_x):data_img[0], int(mid_y):data_img[1]] = part_0


plt.subplot(231),plt.imshow(img, 'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(img_modify, 'gray'),plt.title(' CHANGE REGIONS')
plt.show()


# %%



