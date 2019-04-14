#!/usr/bin/env python3

import cv2 as cv
import numpy as np
from scipy import ndimage

def test():
    kernel_3x3 = np.array([[-1, -1, -1],
                           [-1,  8, -1],
                           [-1, -1, -1]])

    kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                           [-1,  1,  2,  1, -1],
                           [-1,  2,  4,  2, -1],
                           [-1,  1,  2,  1, -1],
                           [-1, -1, -1, -1, -1]])

    img = cv.imread("./pictures/test_1.jpg", cv.IMREAD_GRAYSCALE) 
    cv.namedWindow("Image")
    cv.imshow("Image", img) 

    k3 = ndimage.convolve(img, kernel_3x3)
    k5 = ndimage.convolve(img, kernel_5x5)

    blurred = cv.GaussianBlur(img, (11, 11), 0)
    g_hpf = img - blurred

    cv.namedWindow("k3")
    cv.imshow("k3", k3)

    cv.namedWindow("k5")
    cv.imshow("k5", k5)

    cv.namedWindow("g_hpf")
    cv.imshow("g_hpf", g_hpf)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    test()

