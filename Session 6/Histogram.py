"""
##########################################
       Histogram of Gray Images
##########################################
"""
import cv2
import matplotlib.pyplot as plt
image = cv2.imread("Blur images/lena.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Tree", image)
cv2.waitKey(0)


histo = cv2.calcHist(image, [0], None, [256], [0,256])
plt.plot(histo, color="Purple")
plt.show()

"""
##########################################
    Histogram of BGR Images
##########################################
"""
import cv2
import matplotlib.pyplot as plt
image = cv2.imread("Blur images/lena.jpg")
cv2.imshow("Lena", image)
cv2.waitKey(0)

blue = image[:, :, 0]
green = image[:, :, 1]
red = image[:, : ,2]

b_histo = cv2.calcHist(blue, [0], None, [256], [0,256])
g_histo = cv2.calcHist(green, [1], None, [256], [0,256])
r_histo = cv2.calcHist(red, [2], None, [256], [0,256])
plt.figure(figsize=(3,1))
plt.plot(b_histo, color="Blue")
plt.plot(g_histo, color = "Green")
plt.plot(r_histo, color= "Red")
plt.show()