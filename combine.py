import cv2
import numpy as np
from find_rgb import load_rgb_files

# Load data

r, g, b = load_rgb_files("test_images/makerspace")

# Convert each image to grayscale, and to floating point values

r = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY).astype(float)
g = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY).astype(float)
b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY).astype(float)

# greyworld white balance
r /= np.sum(r)
g /= np.sum(g)
b /= np.sum(b)

# Create image by combining the three channels
bgr = cv2.merge((b, g, r))

#
# Next part increases the colourfulness, without changing the intensity
# Best explained with a diagram really.
#

# Make an image which is just the intensity
white = (r+b+g)/3
white3 = cv2.merge((white, white, white))

max_intensity = 1.1*np.max(white)  # For later

# Remove intensity, leaving colours in r,g,b = 0 plane
diffs = bgr - white3

# Scale the chromatic part
diffs *= 3

# Create image to show by adding back the intensity
show = white3 + diffs

#
# Output stuff
#

# Rotate
show = cv2.rotate(show, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Make sure output is a uint8
# Scale to roughly [0, 255]
show *= 255/max_intensity
# Bits less than 0 go to 0
show[show < 0] = 0
# Bits more than 255 go to 255
show[show > 255] = 255
# Convert to uint8
show = np.array(show, dtype=np.uint8)

# Scale to 700 by 500 image
show = cv2.resize(show, (700, 500))

# Show
cv2.imshow("im", show)

# Wait for user to press key
cv2.waitKey()