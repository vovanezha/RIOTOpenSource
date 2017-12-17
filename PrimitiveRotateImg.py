import numpy as np 
import argparse 
import cv2 

# construct the argument parse
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="path to input image file")
# args = vars(ap.parse_args())

# load the image from disk
image = cv2.imread('/home/nezha/Изображения/test4.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# grab (x, y) and use these coordinates to compute rotated bounding box
coords = np.column_stack(np.where(thresh > 0))

angle = cv2.minAreaRect(coords)[-1]      # the "cv2.minAreaRect" return values in the range [-90, 0);

if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle

# rotate the image
(h, w) = image.shape[:2]

M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)

rotated = cv2.warpAffine(
    image,
    M, (w, h),
    flags=cv2.INTER_CUBIC,
    borderMode=cv2.BORDER_REPLICATE
)


cv2.imshow('Original', image)
cv2.imshow('rotated', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
