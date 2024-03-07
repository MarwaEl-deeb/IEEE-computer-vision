import cv2

#Reading Images
## The whole path
# ERROR: image = cv2.imread("C:\Users\marwa\OneDrive\Desktop\Bird.png")
image = cv2.imread(r"C:\Users\marwa\OneDrive\Desktop\Bird.png")
# image = cv2.imread("C:/Users/marwa/OneDrive/Desktop/Bird.png")

# Image is in a folder in the same directory of your project
image2 =  cv2.imread("Images/Tree.jpg")

# Image is in the same directory of your project
image3 = cv2.imread("Red.png")


#Showing Images
cv2.imshow("Bird", image)

cv2.imshow("Tree", image2)

cv2.imshow("Red Color", image3)

cv2.waitKey(0)  # time with ms
# cv2.waitKey(1000) # will wait for only one second

cv2.imshow("Bird", image)
cv2.waitKey(0)

cv2.imshow("Tree", image2)
cv2.waitKey(0)

cv2.imshow("Red Color", image3)
cv2.waitKey(0)


#Resizing Images
# resize -> take two parameteurs "source image" and "new dimentions"
resized_image = cv2.resize(image, (800,600))
image = cv2.resize(image, (800,600))

# x = 7
# x = 20

cv2.imshow("resized image", resized_image)
cv2.imshow("resized image", image)
cv2.waitKey(0)


# Writing Images
# Takes two parameteurs "new image name with its extention" and "source image"
cv2.imwrite("Resized Image.png", image)

