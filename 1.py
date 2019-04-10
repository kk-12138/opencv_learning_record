#!/usr/bin/env python3
 
import numpy as np
from cv2 import cv2 #if you use "import cv2", it will occurs some error prompt in vscode.
 
def test():
    img = np.zeros(shape = (300, 400), dtype = np.uint8)
 
    print(img.shape)    #output 300x400
    print(img.size)
    print(img.dtype)
    print(img)
 
    #save img to file. I don't know why can't use "~/Pictures/gray_img.jpg".
    cv2.imwrite("/home/kyle/Pictures/gray_img.jpg", img)
 
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    print(img.shape)    #output 300x400x3, 3 channel.
    print(img.size)
    print(img.dtype)
    print(img)
 
    #img[:, :] = 200    #change the value of all channels to 200.
    img[:, :, 1] = 200    #change the value of channel 1 to 200. 
    cv2.imwrite("/home/kyle/Pictures/color_img.jpg", img)
    print(img)
 
    img[90:190, 30:120, 0] = 255
 
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
 
    grayImage = cv2.imread("/home/kyle/Pictures/test.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("/home/kyle/Pictures/test_gray.png", grayImage)
    cv2.namedWindow("Image2")
    cv2.imshow("Image2", grayImage)
 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    test()
