import numpy as np
import cv2 as cv


def ponto_img(img):
    tamanho = img.shape
    retorno = np.zeros(tamanho, dtype=np.uint8)

    STEP = 4
    JITTER = 3
    RAIO = 4

    xrange = np.arange(0, tamanho[0]-STEP, STEP) + STEP // 2
    yrange = np.arange(0, tamanho[1]-STEP, STEP) + STEP // 2

    np.random.shuffle(xrange)
    for i in xrange:
        np.random.shuffle(yrange)
        for j in yrange:
            x = i + np.random.randint((2 * JITTER) - JITTER + 1)
            y = j + np.random.randint((2 * JITTER) - JITTER + 1)
            cor = img[x, y]
            retorno = cv.circle(retorno, (y, x), RAIO, (int(cor[0]), int(cor[1]), int(cor[2])), -1, lineType=cv.LINE_AA)

    return retorno