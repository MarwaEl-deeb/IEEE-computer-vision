"""
########################################
       Thresholding on images
########################################
"""
import cv2
img = cv2.imread("Images/House.webp")
image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("HOUSE", image)

#Global Thresholding
# Any value less than thresh value will convert into black and any value more than it will convert into white
ret1, Gthreshold1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret2, Gthreshold2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Global Thresholding", Gthreshold1)
cv2.imshow("Inverted Global Thresholding", Gthreshold2)
cv2.waitKey(0)

# Otsu Thresholding
ret, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu Thresholding", otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Adaptive Thresholding
adaptive1 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 2)
adaptive2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 2)
adaptive3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 5)
cv2.imshow("HOUSE", image)
cv2.imshow("Adaptive Thresholding 9", adaptive1)
cv2.imshow("Adaptive Thresholding 13", adaptive2)
cv2.imshow("Adaptive Thresholding 13 C: 5", adaptive3)
cv2.waitKey(0)