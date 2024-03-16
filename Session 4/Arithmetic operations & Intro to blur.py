## Printing blue & red image and checking output
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("binary.png")
image_plot = plt.imshow(image)
plt.show()

## Arithmetic operations on images

# Read Images
tree = cv2.imread("Images\Tree.jpg")
bridge = cv2.imread("Images\Bridge.jpeg")

# Resize Images
# operating on images without resizing there will be an error (input size doesn't match)
r_tree = cv2.resize(tree, (600, 400))
r_bridge = cv2.resize(bridge, (600,400))
cv2.imshow("Tree", r_tree)
cv2.imshow("Bridge", r_bridge)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Adding Images
add = cv2.add(r_tree, r_bridge)
cv2.imshow("Added images", add)
cv2.waitKey(0)

# Subtracting Images
subtract = cv2.subtract(r_tree, r_bridge)
subtract2 = cv2.subtract(r_bridge, r_tree)
cv2.imshow("Subtracted images", subtract)
cv2.imshow("Subtracted images 2", subtract2)
cv2.waitKey(0)

# Multiplicating Images
multiply = cv2.multiply(r_tree, r_bridge)
cv2.imshow("Multiplicated images", multiply)
cv2.waitKey(0)

# Dividing Images
divide = cv2.divide(r_tree, r_bridge)
divide2 = cv2.divide(r_bridge, r_tree)
cv2.imshow("Divided images", divide)
cv2.imshow("Divided images 2", divide2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Noting Images
not_tree = cv2.bitwise_not(r_tree)
not_bridge = cv2.bitwise_not(r_bridge)
cv2.imshow("NOTed Tree", not_tree)

cv2.imshow("NOTed Bridge", not_bridge)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ORing Images
or1 = cv2.bitwise_or(r_tree, r_bridge)
or2 = cv2.bitwise_or(not_tree, not_bridge)
or3 = cv2.bitwise_or(r_tree, not_bridge)
or4 = cv2.bitwise_or(not_tree, r_bridge)
cv2.imshow("Oring Original Images", or1)
cv2.imshow("Oring NOTed Images", or2)
cv2.imshow("Oring Original tree NOTed bridge", or3)
cv2.imshow("Oring NOTed tree Original bridge", or4)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ANDing Images
and1 = cv2.bitwise_and(r_tree, r_bridge)
and2 = cv2.bitwise_and(not_tree, not_bridge)
and3 = cv2.bitwise_and(r_tree, not_bridge)
and4 = cv2.bitwise_and(not_tree, r_bridge)
cv2.imshow("ANDing Original Images", and1)
cv2.imshow("ANDing NOTed Images", and2)
cv2.imshow("ANDing Original tree NOTed bridge", and3)
cv2.imshow("ANDing NOTed tree Original bridge", and4)
cv2.waitKey(0)
cv2.destroyAllWindows()

# XORing Images
xor1 = cv2.bitwise_xor(r_tree, r_bridge)
xor2 = cv2.bitwise_xor(not_tree, not_bridge)
xor3 = cv2.bitwise_xor(r_tree, not_bridge)
xor4 = cv2.bitwise_xor(not_tree, r_bridge)
cv2.imshow("XORing Original Images", xor1)
cv2.imshow("XORing NOTed Images", xor2)
cv2.imshow("XORing Original tree NOTed bridge", xor3)
cv2.imshow("XORing NOTed tree Original bridge", xor4)
cv2.waitKey(0)


## Blurring images
image = cv2.imread("blur.jpg")

def average(image):
    avg_blur = np.hstack([image,
                          cv2.blur(image, (3,3)),
                          cv2.blur(image, (5, 5)),
                          cv2.blur(image, (7,7)),
                          cv2.blur(image, (9,9))]
    )
    cv2.imshow("Average blur", avg_blur)
    cv2.waitKey(0)

average(image)

# doing blur without the function
blur1 = cv2.blur(img, (3,3))
blur2 = cv2.blur(img, (5,5))
blur3 = cv2.blur(img, (7,7))

cv2.imshow("Blur kernal 3*3", blur1)
cv2.imshow("Blur kernal 5*5", blur2)
cv2.imshow("Blur kernal 7*7", blur3)
cv2.waitKey(0)
