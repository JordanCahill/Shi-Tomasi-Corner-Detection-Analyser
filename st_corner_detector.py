import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_num_corners(img):
    """
    Finds the maximum number of corners detected by the Shi-Tomasi algorithm on an image to a maximum threshold of 5000

    :param img: input image to apply algorithm to
    :return: number of corners detected
    """

    # Convert to grayscale and apply ST
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 5000, 0.01, 10)

    # 'if' loop accounts for 0 corners detected and returns the value 0 as opposed to Nonetype
    if corners is not None:
        corners = np.int0(corners)
        return len(corners)
    else:
        return 0


def plot_img_corners(img, num_corners=100):
    """
    Applies Shi-Tomasi corner detection to an image and displays the result

    :param img: input image to apply algorithm to
    :param num_corners: ST returns the best n points detected, this parameter defines n (default=100)
    """

    # Convert image to grayscale, apply ST and convert resulting array to ints
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, num_corners, 0.01, 10)
    corners = np.int0(corners)

    # Mark detected points on image
    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 2, 255, -1)

    plt.imshow(img), plt.show()
