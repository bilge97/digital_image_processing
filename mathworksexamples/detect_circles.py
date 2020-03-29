import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('DetectCirclesExample.png', 0)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(img, (3, 3))

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred,
                                    cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                    param2=30, minRadius=1, maxRadius=40)
#gray: Input image (grayscale).
#circles: A vector that stores sets of 3 values: xc,yc,r for each detected circle.
#HOUGH_GRADIENT: Define the detection method. Currently this is the only one available in OpenCV.
#dp = 1: The inverse ratio of resolution.
#min_dist = gray.rows/16: Minimum distance between detected centers.
#param_1 = 200: Upper threshold for the internal Canny edge detector.
#param_2 = 100*: Threshold for center detection.
#min_radius = 0: Minimum radius to be detected. If unknown, put zero as default.
#max_radius = 0: Maximum radius to be detected. If unknown, put zero as default.

# Draw circles
if detected_circles is not None:
    # Convert the circle parameters a, b and r to integers. a and b is center of circle. r is radius
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        x, y, r = pt[0], pt[1], pt[2]

        # Draw circle when detect circle
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)

        # Draw a small circle to show the center.
        cv2.circle(img, (x, y), 1, (0, 0, 255), 3) #radius 1
cv2.imshow('gray', gray_blurred)
cv2.imshow("Detected Circle", img)
cv2.waitKey(0)