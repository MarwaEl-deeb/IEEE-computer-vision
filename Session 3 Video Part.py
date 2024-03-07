import cv2
video = cv2.VideoCapture(r"C:\Users\marwa\Videos\2024-03-01 14-15-21.mkv")
# taking frames from your camera
video = cv2.VideoCapture(0)

while True:
    # ret stores True or False value to tell us if it's still running or not
    ret, frame = video.read()
    cv2.imshow("Video", frame)
    
    # Determine the key that we want to press to stop showing
    if cv2.waitKey(0) & 0xff == ord("q"):  # if cv2.waitKey(0)  == ord("q"):
        break

# To make sure that camera is closed
cv2.destroyAllWindows()
