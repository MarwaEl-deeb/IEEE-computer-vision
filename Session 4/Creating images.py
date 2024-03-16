# Creating images with numpy and show them with matplotlib

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

# Creating Black & White Pixels Image
BandW = np.array([[[255,255,255],
                   [0,0,0]],
                 [[0,0,0],
                 [255,255,255]]])
                 
image_plot2 = plt.imshow(BandW)
plt.show()


# how to plot images with matplotlib
image2 = cv2.imread("binary.png")
image_plot = plt.imshow(image2)
plt.show()
