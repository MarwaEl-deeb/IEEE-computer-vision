import cv2
"""
#####################################
        Images Noting Logic
#####################################
"""
# Reading images
white = cv2.imread("Images\white.png")
bridge = cv2.imread("Images\Bridge.jpeg")
tree = cv2.imread("Images\Tree.jpg")

# Resizing images
r_white = cv2.resize(white, (600, 400))
r_tree = cv2.resize(tree, (600, 400))
r_bridge = cv2.resize(bridge, (600, 400))

# Subtracting from white image
sbct_tree = cv2.subtract(r_white, r_tree)
sbct_bridge = cv2.subtract(r_white, r_bridge)

cv2.imshow("Noted tree by white image", sbct_tree)
cv2.imshow("Noted bridge by white image", sbct_bridge)
cv2.waitKey(0)


# NOTing images
not_tree = cv2.bitwise_not(r_tree)
not_bridge = cv2.bitwise_not(r_bridge)

cv2.imshow("NOTed Tree", not_tree)
cv2.imshow("NOTed Bridge", not_bridge)
cv2.waitKey(0)