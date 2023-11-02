import cv2
import numpy as np
from find_rgb import load_rgb_files

# Load data

r, g, b = load_rgb_files("test_images/makerspace")

# Convert each image to grayscale, and to floating point values

r = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY).astype(float)
g = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY).astype(float)
b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY).astype(float)

# Create image by combining the three channels, rotate
big_uncorrected = cv2.merge((b, g, r))
big_uncorrected = cv2.rotate(big_uncorrected , cv2.ROTATE_90_COUNTERCLOCKWISE)

# Small one for
display_size=(700, 500)
small_unbalanced = None

window_name = "Combined Image"


def calculate_images(r_white, g_white, b_white, chroma_factor):
    global big_unbalanced, big_uncorrected, small_unbalanced

    #
    # This part increases the colourfulness, without changing the intensity
    # Best explained with a diagram really.
    #

    # Make an image which is just the intensity
    white = (r+b+g)/3
    white3 = cv2.merge((white, white, white))


    # Remove intensity, leaving colours in r,g,b = 0 plane
    diffs = big_uncorrected - white3

    # Scale the chromatic part
    diffs *= chroma_factor

    # Create image to show by adding back the intensity
    big_unbalanced = white3 + diffs

    # image used for doing interactive white balance
    small_unbalanced = cv2.resize(big_unbalanced, display_size)



    #
    # Output stuff
    #

    cv2.resize(big_unbalanced, display_size)

    # Make sure output is a uint8
    # Scale to roughly [0, 255]

    max_intensity = 1.1 * np.max(np.sum(small_balanced))  # For later

    small_output = base*255/max_intensity
    # Bits less than 0 go to 0
    small_output[small_output < 0] = 0
    # Bits more than 255 go to 255
    small_output[small_output > 255] = 255
    # Convert to uint8
    small_output = np.array(small_output, dtype=np.uint8)

    return show

def callback(event, x, y, flags, *params):
    global show
    global base

    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicky")
        b_white, g_white, r_white = base[y, x, :]
        print(r_white, g_white, b_white)
        base[:,:,0] /= b_white
        base[:,:,1] /= g_white
        base[:,:,2] /= r_white

        show = make_show_image()


while True:
    # Show
    cv2.imshow(window_name, show)
    cv2.setMouseCallback(window_name, callback)

    # Wait for user to press key
    cv2.waitKey(10)

