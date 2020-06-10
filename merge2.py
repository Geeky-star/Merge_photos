import cv2

img = cv2.imread('i5.jpg')
img2 = cv2.imread('opencv.png')
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

img = cv2.resize(img, (400,400))
img2 = cv2.resize(img2, (400,400))
dst = cv2.addWeighted(img, 0.9, img2, 0.5, 0.9);

cv2.imshow('image', dst)
cv2.waitKey()
