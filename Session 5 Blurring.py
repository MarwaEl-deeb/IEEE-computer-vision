import cv2
"""
#######################################################
      Blurring techniques without using NumPy
#######################################################
"""
bug = cv2.imread("Blur images/bug.jpg")

# Average Blur
avg1 = cv2.blur(bug, (3,3))
avg2 = cv2.blur(bug, (5,5))
avg3 = cv2.blur(bug, (3,5))
avg4 = cv2.blur(bug, (7,7))
cv2.imshow("Original bug", bug)
cv2.imshow("Average blur 3", avg1)
cv2.imshow("Average blur 5", avg2)
cv2.imshow("Average blur 3*5", avg3)
cv2.imshow("Average blur 7", avg4)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Gaussian Blur
gausin1 = cv2.GaussianBlur(bug, (3,3), 0)
gausin2 = cv2.GaussianBlur(bug, (5,5), 0)
gausin3 = cv2.GaussianBlur(bug, (3,5), 0)
gausin4 = cv2.GaussianBlur(bug, (7,7), 0)
cv2.imshow("Original bug", bug)
cv2.imshow("Gaussian blur 3", gausin1)
cv2.imshow("Gaussian blur 5", gausin2)
cv2.imshow("Gaussian blur 3*5", gausin3)
cv2.imshow("Gaussian blur 7", gausin4)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Median Blur
median1 = cv2.medianBlur(bug, 3)
median2 = cv2.medianBlur(bug, 5)
median3 = cv2.medianBlur(bug, 7)
median4 = cv2.medianBlur (bug, 9)
cv2.imshow("Original bug", bug)
cv2.imshow("Median blur 3", median1)
cv2.imshow("Median blur 5", median2)
cv2.imshow("Median blur 7", median3)
cv2.imshow("Median blur 9", median4)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Bilateral Blur
bilaterial1 = cv2.bilateralFilter(bug, 5, 75, 75)
bilaterial2 = cv2.bilateralFilter(bug, 9, 75, 75)
bilaterial3 = cv2.bilateralFilter(bug, 9, 95, 95)
bilaterial4 = cv2.bilateralFilter(bug, 11, 75, 75)
cv2.imshow("Original bug", bug)
cv2.imshow("Bilateral blur 5", bilaterial1)
cv2.imshow("Bilateral blur 9 75", bilaterial2)
cv2.imshow("Bilateral blur 9 95", bilaterial3)
cv2.imshow("Bilateral blur 11", bilaterial4)
cv2.waitKey(0)


"""
####################################################
      Blurring techniques using NumPy
####################################################
"""
import numpy as np
bug = cv2.imread("Blur images/bug.jpg")
eye = cv2.imread("Blur images/eye.jpg")
photo = cv2.imread("Blur images/photographer.jpg")

# Average Blur
def avg_blur(image):
    average = np.hstack([image,
                         cv2.blur(image, (3, 3)),
                         cv2.blur(image, (3, 5)),
                         cv2.blur(image, (5, 5)),
                         cv2.blur(image, (7, 7))])
    cv2.imshow("Average Blur", average)
    cv2.waitKey(0)

# Gaussian Blur
def gaussian_blur(image):
    gaussian = np.hstack([image,
                          cv2.GaussianBlur(image, (3, 3), 0),
                          cv2.GaussianBlur(image, (3, 5), 0),
                          cv2.GaussianBlur(image, (5, 5), 0),
                          cv2.GaussianBlur(image, (7, 7), 0)])
    cv2.imshow("Gaussian Blur", gaussian)
    cv2.waitKey(0)

# Median Blur
def median_blur(image):
    median = np.hstack([image,
                        cv2.medianBlur(image, 3),
                        cv2.medianBlur(image, 5),
                        cv2.medianBlur(image, 7),
                        cv2.medianBlur(image, 9)])
    cv2.imshow("Median Blur", median)
    cv2.waitKey(0)

#Bilateral Blur
def bilateral_blur(image):
    bilateral = np.hstack([image,
                           cv2.bilateralFilter(image, 3, 75, 75),
                           cv2.bilateralFilter(image, 5, 75, 75),
                           cv2.bilateralFilter(image, 7, 75, 75),
                           cv2.bilateralFilter(image, 9, 75, 75)])
    cv2.imshow("Bilateral Blur", bilateral)
    cv2.waitKey(0)

avg_blur(bug)
gaussian_blur(bug)
median_blur(bug)
bilateral_blur(bug)

avg_blur(eye)
gaussian_blur(eye)
median_blur(eye)
bilateral_blur(eye)

avg_blur(photo)
gaussian_blur(photo)
median_blur(photo)
bilateral_blur(photo)
