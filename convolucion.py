import numpy as np
import cv2
#Ioriginal = matriz original
def convolucion(Ioriginal, kernel):
    '''Método encargado de realizar una convolución a una imagen
    Entrada:
    Ioriginal - imagen original en forma de matríz
    kernel - kernel para barrer la imagen
    Salida:
    res - imagen resultante'''
    #fr - filas, cr - columnas
    fr = len(Ioriginal)-(len(kernel)-1)
    cr = len(Ioriginal[0])-(len(kernel[0])-1)
    res = np.zeros((fr, cr), np.uint8)

    #filas, matríz resultado
    for i in range(len(res)):
        #columnas, matríz resultado
        for j in range(len(res[0])):
            suma = 0
            #filas, kernel
            for m in range(len(kernel)):
                #columnas, kernel
                for n in range(len(kernel[0])):
                    suma += kernel[m][n] * Ioriginal[m+i][n+j]
            if suma<=255:
                res[i][j]=round(suma)
            else:
                res[i][j]=255

    return res

K = [[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]#kernel
I = [[2,0,1,1,1],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]]#prototipo de imagen

#conversión de arrays a numpy arrays
In = np.array(I)
Kn = np.array(K)

IRGB = cv2.imread('004.jpg')
IGS= cv2.cvtColor(IRGB, cv2.COLOR_BGR2GRAY)
print(IGS.shape)
#llamado de la función e impresión del resultado
R = convolucion(IGS, Kn)
print(R)
print(R.shape)
cv2.imwrite('004C.jpg',R)
