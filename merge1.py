import cv2

img = cv2.imread('robot.jpg')

img2 = cv2.imread('opencv.png')
img = cv2.resize(img, (400,400))
img2 = cv2.resize(img2, (400,400))

dst = cv2.add(img,img2);

cv2.imshow('image', dst)
cv2.waitKey()
