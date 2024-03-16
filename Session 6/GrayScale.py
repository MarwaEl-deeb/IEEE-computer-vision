"""
##########################################################
       Convert RGB images to Grayscale using NumPy
##########################################################
"""
import numpy as np
import matplotlib.pyplot as plt

#                    R   G    B
image = np.array([[[255, 45, 10],
                   [58, 210, 67],
                   [0, 0, 38]],

                  [[64, 250, 180],
                   [200, 35, 158],
                   [74, 23, 86]],

                  [[77, 0, 0],
                   [0, 105, 220],
                   [20, 65, 10]]])

imageplot = plt.imshow(image)
plt.show()

# Separating each channel alone R, G, B
red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

# Printing each color (channel) alone
print("Red", red)
print("Blue", blue)
print("Green", green)

# r = 0.299, g = 0.587, b = 0.114
# generating one channel image
image_1D = 0.114 * blue + 0.587 * green + 0.299 * red

# Showing Gray image using matplotlib
grayplot = plt.imshow(image_1D, cmap="gray")
plt.show()


"""
##########################################################
       Convert BGR images to Grayscale using Open-CV
##########################################################
"""
import cv2
image = cv2.imread("palastine.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original image", image)
cv2.imshow("Gray image", gray_image)
cv2.waitKey(0)