import os
import sys

import cv2
import numpy as np

from find_rgb import load_rgb_files_as_bgr_image

# source = sys.argv[1]

source = "test_images/makerspace"

#
# Parameters
#

window_title = "Colour Merger"

#
# Main part
#

if os.path.exists(source) and os.path.isdir(source):
    directory = source
    prefix = ""
else:
    directory = os.path.basename(source)
    prefix = os.path.dirname(source)

im = load_rgb_files_as_bgr_image(directory, prefix)

# rotate
im = cv2.rotate(im, cv2.ROTATE_90_COUNTERCLOCKWISE)


print(np.max(im), np.min(im))

chroma_factor = 1.0

color_correction_r = 1/3
color_correction_g = 1/3
color_correction_b = 1/3

color_correction_input_amount = 0.01

def normalise_color_correction():
    """ Happens for all colour correction changes"""
    global color_correction_r, color_correction_g, color_correction_b

    total = color_correction_r + color_correction_g + color_correction_b

    color_correction_r /= total
    color_correction_g /= total
    color_correction_b /= total

    print("Color correction (r,g,b):", color_correction_r, color_correction_g, color_correction_b)

def to_displayable(im, chroma_factor=1.0):
    """Create the image we want to show"""

    # Make an image which is just the intensity
    white = np.sum(im, axis=2)/3
    white3 = cv2.merge((white, white, white))

    # Remove intensity, leaving colours in r,g,b = 0 plane
    diffs = im - white3


    # Scale the chromatic part
    diffs *= chroma_factor

    # Create image to show by adding back the intensity
    float_output = white3 + diffs

    #
    # Output stuff
    #

    # Make sure output is a uint8
    # Scale to roughly [0, 255]

    float_output[:,:,2] *= color_correction_r
    float_output[:,:,1] *= color_correction_g
    float_output[:,:,0] *= color_correction_b

    max_intensity = 1.1 * np.max(float_output)


    output = float_output*255/max_intensity

    # Bits less than 0 go to 0
    output[output < 0] = 0
    # Bits more than 255 go to 255
    output[output > 255] = 255
    # Convert to uint8
    output = np.array(output, dtype=np.uint8)

    return output

# Interface loop
while True:
    show = to_displayable(im, chroma_factor=chroma_factor)

    cv2.imshow(window_title, show)
    key = cv2.waitKey()

    # Keyboard controls

    # Decrease chroma
    if key == ord('q'):
        chroma_factor /= 1.1
        print("Chroma Factor:", chroma_factor)

    # Increase chroma
    elif key == ord('w'):
        chroma_factor *= 1.1
        print("Chroma Factor:", chroma_factor)

    # Increase red
    elif key == ord('r'):
        color_correction_r += color_correction_input_amount
        normalise_color_correction()

    # Decrease red
    elif key == ord('e'):
        color_correction_r -= color_correction_input_amount
        normalise_color_correction()

    # Increase green
    elif key == ord('g'):
        color_correction_g += color_correction_input_amount
        normalise_color_correction()

    # Decrease green
    elif key == ord('f'):
        color_correction_g -= color_correction_input_amount
        normalise_color_correction()

    # Increase blue
    elif key == ord('b'):
        color_correction_b += color_correction_input_amount
        normalise_color_correction()

    # Decrease blue
    elif key == ord('v'):
        color_correction_b -= color_correction_input_amount
        normalise_color_correction()

    else:
        pass