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


def plot_best_img_corners(img, num_corners):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, num_corners, 0.01, 10)
    corners = np.int0(corners)

    # TODO: Divide resolution of img by arbitrary value to
    # find a suitable value for corner dot size, round to next
    # highest integer, if val < 0, val = 1

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 2, 255, -1)

    plt.imshow(img), plt.show()
