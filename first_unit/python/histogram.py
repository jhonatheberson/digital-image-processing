# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
from cv2 import *
from matplotlib import pyplot as plt


# %%
histR = np.zeros(64)
histG = np.zeros(64)
histB = np.zeros(64)
nbins = 64
histrange = range(0,256)
histWidth = int(nbins)
histheight = int(nbins/2)


# %%
# create a mask
mask = np.zeros((histheight,histWidth), np.uint8)
mask[0:histheight, 0:histWidth] = 255
histImgR = np.zeros((histheight,histWidth), np.uint8)
histImgG = np.zeros((histheight,histWidth), np.uint8)
histImgB = np.zeros((histheight,histWidth), np.uint8)


# %%

cap = VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Define the codec and create VideoWriter object
# fourcc = VideoWriter_fourcc(*'XVID')
# out = VideoWriter('output.avi', fourcc, 20.0, (640,  480))


# %%
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    cap.set(CAP_PROP_FRAME_WIDTH, 640)
    cap.set(CAP_PROP_FRAME_HEIGHT, 480)

    width = cap.get(CAP_PROP_FRAME_WIDTH)
    height = cap.get(CAP_PROP_FRAME_HEIGHT)

    # print('width: ', width)
    # print('heigth', height)
    

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break




    # frame = flip(frame, 0)
    # write the flipped frame
    # out.write(frame)
    # Our operations on the frame come here

    
    
    # [b,g,r]
    
    histB = calcHist([frame],[0],None,[nbins],[0,256])
    histG = calcHist([frame],[1],None,[nbins],[0,256])
    histR = calcHist([frame],[2],None,[nbins],[0,256])
    
    mask_default = np.zeros((histheight, nbins), np.uint8)
    mask_B = merge((mask_default,mask_default,mask_default))
    mask_G = merge((mask_default,mask_default,mask_default))
    mask_R = merge((mask_default,mask_default,mask_default))

    # mask_default_b = np.zeros((nbins, 1), np.uint8)
    # print(mask_default_b.shape)
    # print(histB.shape)

    normalize(histB,histB,0, histheight, NORM_MINMAX, -1)
    normalize(histG,histG,0, histheight, NORM_MINMAX, -1)
    normalize(histR,histR,0, histheight, NORM_MINMAX, -1)

    print(histB)

    for i in range(nbins):
        line(mask_B, (i, histheight), (i,int(histB[i])), (255,0,0), 1)
        line(mask_G, (i, histheight), (i,int(histG[i])), (0,255,0), 1)
        line(mask_R, (i, histheight), (i,int(histR[i])), (0,0,255), 1)

    
    
    frame[0:histheight,0:nbins] = mask_B
    frame[histheight:2*histheight,0:nbins] = mask_G
    frame[2*histheight:3*histheight,0:nbins] = mask_R

    imshow('frame', frame)
    if waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
destroyAllWindows()


# %%



