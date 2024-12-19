# Import(s)
import os
import numpy as np
from PIL import Image


# get_arr function
def get_arr(img):
    with Image.open(img, "r") as f:
        return np.asarray(f)


# Main function
def main():
    # Paths
    cwd = os.getcwd()
    img_file = "baboon.png"
    img_dir = os.path.join(cwd, "Images")
    img = os.path.join(img_dir, img_file)

    # Call get_arr to get numpy list of pixel values
    np_arr = get_arr(img)

    # Print np_arr
    print(np_arr)


# Call main
main()