import argparse
import cv2
import numpy as np

def resize_to_screen(src, maxw=1280, maxh=700, copy=False):

    height, width = src.shape[:2]

    scl_x = float(width)/maxw
    scl_y = float(height)/maxh

    scl = int(np.ceil(max(scl_x, scl_y)))

    if scl > 1.0:
        inv_scl = 1.0/scl
        img = cv2.resize(src, (0, 0), None, inv_scl, inv_scl, cv2.INTER_AREA)
    elif copy:
        img = src.copy()
    else:
        img = src

    return img

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = resize_to_screen(image)
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(grayscale, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

sobelx = cv2.Sobel(grayscale, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(grayscale, cv2.CV_64F, 0, 1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
sobelcombined = cv2.bitwise_or(sobelx, sobely)
#cv2.imshow("sobel combined", sobelcombined)

(_, cnts, _) = cv2.findContours(sobelcombined.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print "Contours in the image, %d" % (len(cnts))

shape = image.copy()
cv2.drawContours(shape, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Edges", shape)
cv2.imwrite("output.jpg", shape)

cv2.waitKey(0)
