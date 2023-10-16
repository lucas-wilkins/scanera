import cv2
import numpy as np


r = cv2.imread("test_images/first/red.jpg")
g = cv2.imread("test_images/first/green.jpg")
b = cv2.imread("test_images/first/blue.jpg")


r = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY).astype(float)
g = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY).astype(float)
b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY).astype(float)


white = (r+b+g)/3
white3 = cv2.merge((white, white, white))

max_intensity = 1.1*np.max(white)

bgr = cv2.merge((b, g, r))

diffs = bgr - white3
diffs *= 10

show = white3 + diffs

show = cv2.rotate(show, cv2.ROTATE_90_COUNTERCLOCKWISE)

show *= 255/max_intensity
show[show < 0] = 0
show[show > 255] = 255
show = np.array(show, dtype=np.uint8)
show = cv2.resize(show, (700, 500))

cv2.imshow("im", show)

cv2.waitKey()