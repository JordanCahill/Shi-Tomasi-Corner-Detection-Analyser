import st_corner_detector as st
import cv2
import os
from matplotlib import pyplot as plt

# TODO: Add documentation


def load_images(folder):
    img_array = []
    supported = [".jpg", ".png"]
    for filename in os.listdir(folder):
        if any(x in filename for x in supported):
            img_in = cv2.imread(os.path.join(folder, filename))
            img_array.append((filename, img_in))
    return img_array


def plot_performance_v_res(list_in):
    new_list = []
    for a, b, c in list_in:
        new_list.append((str(c), b))
    plt.scatter(*zip(*new_list))  # zip(*list) separates the tuples into listd=s
    plt.xticks(rotation=45)
    plt.xlabel("Resolution")
    plt.ylabel("Corners Detected")
    for a, b in (new_list):
        plt.annotate(b, (a, b), xytext=(6, 6), textcoords='offset pixels')
    plt.show()
    #plt.savefig('plot.png', bbox_inches='tight')


def get_key(arr):
    return arr[1]


if __name__ == "__main__":
    images = load_images(os.getcwd() + "/images")
    results = []
    for img_name, img in images:
        resolution = (len(img[0]), len(img))
        results.append((img_name, st.get_num_corners(img), resolution))
    results.sort(key=get_key, reverse=True)

    highest_num_corners = results[0][1]

    for name, num_corners, res in results:
        percentage = round((num_corners / highest_num_corners) * 100, 2)
        print("Image: '{0}' | Corners detected: {1} | {2}% of full quality image | Resolution: {3}"
              .format(name, num_corners, percentage, res))
    plot_performance_v_res(results)