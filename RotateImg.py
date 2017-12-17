import cv2
import numpy as np

img = cv2.imread('/home/nezha/Изображения/test3.png')
img_copy = img.copy()
img_copy = cv2.medianBlur(img, 5)

gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
thresh_copy = thresh.copy()
thresh = cv2.bitwise_not(thresh)

kernel = np.ones((2, 2), np.uint8)

closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)


cv2.imshow('clos', opening)

average_theta = 0
t = 0

# Calculate lines
lines = cv2.HoughLines(opening, 1, np.pi / 180, 275)

for i in range(0, len(lines)):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(img_copy, (x1, y1), (x2, y2), (0, 255, 0), 1)
        average_theta += theta
        t += 1

# Search the angle
angle = ((average_theta / t) - (np.pi / 180 * 90)) * 180 / np.pi
h, w = img.shape[:2]

# Rotated the image
M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)
rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


cv2.imshow('copy', img_copy)
cv2.imshow('rotated', rotated)


cv2.waitKey(0)
cv2.destroyAllWindows()
