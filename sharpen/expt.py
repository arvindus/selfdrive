import cv2
import os, sys
import matplotlib.image as mpimg
import numpy as np

def sharpen(arr,fbase):
    if arr.shape[2] == 4:
        r,g,b,a = cv2.split(arr)
    else:
        r,g,b = cv2.split(arr)
    kernel = np.array([[0,-0.25,0], [-0.25,2,-0.25], [0,-0.25,0]])
    new_r = cv2.filter2D(r, -1, kernel)
    new_g = cv2.filter2D(g, -1, kernel)
    new_b = cv2.filter2D(b, -1, kernel)
    
    if arr.shape[2] == 4:
        new_arr = cv2.merge((new_r,new_g,new_b,a))
    else:
        new_arr = cv2.merge((new_r,new_g,new_b))
    mpimg.imsave(fbase+"_new.png", new_arr)
    return new_arr
    
if __name__ == "__main__":
    file = "experiment/car.png"
    img = mpimg.imread(file)
    new_img = sharpen(img,"experiment/car")
    file = "experiment/road.png"
    img = mpimg.imread(file)
    new_img = sharpen(img,"experiment/road")
    