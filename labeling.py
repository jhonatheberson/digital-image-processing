from cv2 import *
import numpy as np

image = imread('bolhas.png', IMREAD_GRAYSCALE)

realce = np.zeros(image.shape, image.dtype)

if not image.data:
    print('Imagem não carregou corretamente')

width, height = image.shape
print(f'{width} x {height}')

mask = np.zeros((height + 2, width + 2), image.dtype)

nObjects = 0
for i in range(height):
    for j in range(width):
        if image[i][j] == 255:
            nObjects += 1
            floodFill(image, mask, (j,i),nObjects)

print(f'a figura tem {nObjects} bolhas')
equalizeHist(image, realce)
imshow('image', image)
imshow('realce', realce)
imwrite('labeling.png', image)
waitKey()
