import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

def resize_to_screen(src, maxw=1380, maxh=600, copy=False):

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

image = cv2.imread(args["image"])
image = resize_to_screen(image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)

canny = cv2.Canny(blurred, 30, 150)

(_, cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print "Contours in the image, %d" % (len(cnts))

shape = image.copy()
cv2.drawContours(shape, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Edges", shape)
cv2.imwrite("canny_edge_img.jpg", shape)

cv2.waitKey(0)
