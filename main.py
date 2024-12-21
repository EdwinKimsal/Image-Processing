# Import(s)
import os
import numpy as np
from PIL import Image


def mutate_arr(arr, padding):
    """
    Mutate np arr with proper
    padding
    """

    # Iterate for each padding needed
    for i in range(padding):
        for j in range(arr[i]):
            print(arr[i][j])
            arr[i][j] = "Null"


def calc_padding(kernal):
    """
    Calculate and return needed padding to
    perform convolutions on img
    """

    # Num must be odd
    if kernal % 2 == 0:
        raise TypeError("Error: Kernal must be odd")

    # Calc padding needed to keep convolution same size
    padding = (kernal - 1) // 2

    # Return padding
    return padding


def get_arr(img):
    """
    Open img and return np arr
    of pixel values
    """

    # Open arrgument img
    with Image.open(img, "r") as f:
        # Return np arr of pixel values
        return np.asarray(f)


def main():
    # Kernal length (square)
    kernal = 5

    # Paths
    cwd = os.getcwd()
    img_file = "black_white.png"
    img_dir = os.path.join(cwd, "Images")
    img = os.path.join(img_dir, img_file)

    # Calc padding
    padding = calc_padding(kernal)

    # Call get_arr to get numpy list of pixel values
    np_arr = get_arr(img)

    # Mutate arr based on padding
    mutate_arr(np_arr, padding)

    # Print np_arr, padding
    print(np_arr, padding)


# Call main
main()