import st_corner_detector as st
import cv2
from matplotlib import pyplot as plt

# TODO: Add documentation


def resize_10(original_img):
    """
    Takes an image argument and resizes it 10 times. Each image in the output array is 1 to 10 times lower resolution
    than the input image.

    :param original_img: image to be resized
    :return: array of 10 lower resolution images
    """

    img_array = []
    img_array.append(original_img)
    for i in range(10):
        if i is not 0:
            resized = cv2.resize(original_img, None, fx=i / 10, fy=i / 10, interpolation=cv2.INTER_AREA)
            img_array.append(resized)
    return img_array


def plot_res_v_corners_detected(list_in, save=False):
    """
    Plots the resolution of a list of images vs the number of corners detected by ST

    :param list_in: Array of tuples in the form (resolution, corners detected),
    :param save:
    """

    data = []
    for res, corners in list_in:
        data.append((str(res), corners))

    plt.scatter(*zip(*data))  # zip(*list) separates the tuples into list
    plt.xticks(rotation=45)
    plt.xlabel("Resolution")
    plt.ylabel("Corners Detected")

    for res, corners in data:
        plt.annotate(corners, (res, corners), xytext=(6, 6), textcoords='offset pixels')

    if save is True:
        plt.savefig('plot.png', bbox_inches='tight')

    plt.show()


def analyse_corners(images):
    """
    Takes an array of images and applies ST corner detection to each, prints the performance results

    :param images: array of images (at different resolutions)
    :return: array of tuples (a,b) where a is image resolution and b is the number of corners detected, array sorted by
    resolution in descending order
    """

    # Populate array of tuples (a,b) where a is the number of corners detected, and b is the image resolution
    results = []
    for i in images:
        resolution = (len(i[0]), len(i))
        results.append((resolution, st.get_num_corners(i)))

    # TODO: Add option for Harris corner detection

    # Sort array by image resolution in descending order
    results.sort(reverse=True)

    # Calculate and print the performance of the corner detection at each resolution
    highest_num_corners = results[0][1]
    for res, num_corners in results:
        percentage = round((num_corners / highest_num_corners) * 100, 2)
        print("Corners detected: {0} | {1}% of full quality image | Resolution: {2}"
              .format(num_corners, percentage, res))

    return results


if __name__ == "__main__":

    img = cv2.imread("images/boxes624.jpg")  # Default TODO: Add user input
    resized_images = resize_10(img)

    corner_array = analyse_corners(resized_images)

    plot_res_v_corners_detected(corner_array, save=False)
