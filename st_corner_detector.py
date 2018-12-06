import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_num_corners(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 5000, 0.01, 10)
    if corners is not None:
        corners = np.int0(corners)
        return len(corners)
    else:
        return 0


def detect_img_corners(img, **kwargs):

    num_corners = 100  # Default
    for key in kwargs:
        if (key == 'corners') and (kwargs[key] == 'yes'):
            num_corners = kwargs[key]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, num_corners, 0.01, 10)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 2, 255, -1)

    plt.imshow(img), plt.show()
