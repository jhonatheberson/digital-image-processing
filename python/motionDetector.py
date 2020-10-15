# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
from cv2 import *
from matplotlib import pyplot as plt
import os


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
    ret, frame_1 = cap.read()

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

    img = imread('./assets/bolhas.png',IMREAD_GRAYSCALE)


    # frame = flip(frame, 0)
    # write the flipped frame
    # out.write(frame)
    # Our operations on the frame come here

    # Our operations on the frame come here
    gray_1 = cvtColor(frame_1, COLOR_BGR2GRAY)
    equ_1 = equalizeHist(gray_1) # histogram equalization
    histgray_1 = calcHist([equ_1],[0],None,[256],[0,256])
    
    ret, frame_2 = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray_2 = cvtColor(frame_2, COLOR_BGR2GRAY)
    equ_2 = equalizeHist(gray_2) # histogram equalization
    histgray_2 = calcHist([equ_2],[0],None,[256],[0,256])



    # detecte moviment
    # print((histgray_2 != histgray_1).any())
    if (histgray_2 != histgray_1).any():
        print('motion detected')
        os.system("beep")
        
        

    # [b,g,r]
    
    res = np.hstack((equ_1,equ_2)) #stacking images side-by-side
    imshow('histogram equalization', res)
    if waitKey(1) == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
destroyAllWindows()


# %%



