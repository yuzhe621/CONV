#coding:utf-8
import cv2
import numpy as np

path = r'./work/1.jpeg'
img = cv2.imread(path)

shape = np.array(
    [
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ]
                 )

shape1 = np.array(
    [
        [1/16, 2/16, 1/16],
        [2/16, 4/16, 2/16],
        [1/16, 2/16, 1/16]

    ]
)

H,W = img.shape[0:2]
h,w = shape.shape
conv = np.zeros([H - h + 1, W - w + 1, 3], "int")

for k in range(3):
    for i in range(H - h + 1):
        for j in range(W - w + 1):
            conv[i, j, k] = sum(sum(img[i:i+h, j:j+w, k] * shape1))

# image = conv.astype(np.uint8)
img_8u = cv2.normalize(conv, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

cv2.imwrite(r'./work/2.jpeg', img_8u)
cv2.imshow("img", img_8u)
cv2.waitKey()
cv2.destroyAllWindows()
