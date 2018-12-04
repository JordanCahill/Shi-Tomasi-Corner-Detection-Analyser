import st_corner_detector as st
import cv2
import os
from PIL import Image
from matplotlib import pyplot as plt

# TODO: Add documentation


def resize_10(original_img):

    img_array = []
    img_array.append(original_img)
    for i in range(10):
        if i is not 0:
            resized = cv2.resize(original_img, None, fx=i / 10, fy=i / 10, interpolation=cv2.INTER_AREA)
            img_array.append(resized)
    return img_array


def plot_performance_v_res(list_in, **kwargs):
    new_list = []
    for a, b, in list_in:
        new_list.append((str(b), a))
    plt.scatter(*zip(*new_list))  # zip(*list) separates the tuples into listd=s
    plt.xticks(rotation=45)
    plt.xlabel("Resolution")
    plt.ylabel("Corners Detected")
    for a, b in (new_list):
        plt.annotate(b, (a, b), xytext=(6, 6), textcoords='offset pixels')

    for key in kwargs:
        if (key == 'save') and (kwargs[key] == 'yes'):
            plt.savefig('plot.png', bbox_inches='tight')

    plt.show()


def get_key(arr):
    return arr[1]


if __name__ == "__main__":

    # TODO: Add kwargs for different runs - Clean up main
    # Seperate functionality into different methods with a different
    # kwarg to call each one

    img = cv2.imread("images/boxes624.jpg") # Default TODO: Add user input
    images = resize_10(img)
    #images = load_images(os.getcwd() + "/images")

    results = []
    for img in images:
        resolution = (len(img[0]), len(img))
        results.append((st.get_num_corners(img), resolution))
    print(results)
    results.sort(key=get_key, reverse=True) # Sort by highest res
    print(results)
    highest_num_corners = results[0][0]

    for num_corners, res in results:
        percentage = round((num_corners / highest_num_corners) * 100, 2)
        print("Corners detected: {0} | {1}% of full quality image | Resolution: {2}"
              .format(num_corners, percentage, res))
    plot_performance_v_res(results,save='no')