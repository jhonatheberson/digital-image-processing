import numpy as np
import cv2 as cv


def bordar_random(img, fundo, fator=20):
    retorno = fundo.copy()

    for i in range(6, 0, -1):
        pontos = cv.Canny(img, i*fator, i*fator*3)
        pontos = np.where(pontos != 0)
        cordenadas = zip(pontos[0], pontos[1])

        for p in cordenadas:
            cor = img[p]
            retorno = cv.circle(retorno, (p[1], p[0]), i,  (int(cor[0]), int(cor[1]), int(cor[2])), -1, lineType=cv.LINE_AA)

    return retorno
  
  