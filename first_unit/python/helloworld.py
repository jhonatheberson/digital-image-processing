# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2 as cv #import opencv 
import sys #import sys the system for 
img = cv.imread(cv.samples.findFile("assets/biel.png")) # open picture
if img is None: #checks picture has been apened 
    sys.exit("Could not read the image.")
cv.imshow("Display window", img) #show picture
cv.imwrite("assets/starry_night.jpeg", img) #save picture


# %%
import cv2 as cv #import opencv 
import sys #import sys the system for 
img = cv.imread(cv.samples.findFile("assets/biel.png")) # open picture
if img is None: #checks picture has been apened 
    sys.exit("Could not read the image.")
cv.imshow("Display window", img) #show picture
cv.imwrite("assets/starry_night.jpeg", img) #save picture


# %%



