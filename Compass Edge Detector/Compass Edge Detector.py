import cv2
import numpy as np


# rotate function for rotate compass matrix 45 degrees
def rotateMatrix(mat):
    if not len(mat):
        return

    top = 0
    bottom = 2

    left = 0
    right = 2

    while left < right and top < bottom:

        prev = mat[top + 1][left]

        for i in range(left, right + 1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr

        top += 1

        for i in range(top, bottom + 1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr

        right -= 1

        for i in range(right, left - 1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr

        bottom -= 1

        for i in range(bottom, top - 1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr

        left += 1

    return mat


# Compass Edge Detector
def CompassEdgeDetector(image):
    compassMatrix = [[-1, -1, -1], [1, -2, 1], [1, 1, 1]]
    newImage = np.zeros((image.shape[0], image.shape[1]))

    for l in range(0, 8):
        for i in range(1, image.shape[0] - 1):
            for j in range(1, image.shape[1] - 1):
                temp = (image[i - 1, j - 1] * compassMatrix[0][0]) + (image[i, j - 1] * compassMatrix[1][0]) + (
                            image[i + 1, j - 1] * compassMatrix[2][0]) + (image[i - 1, j] * compassMatrix[0][1]) + (
                                   image[i, j] * compassMatrix[1][1]) + (image[i, j + 1] * compassMatrix[1][2]) + (
                                   image[i - 1, j + 1] * compassMatrix[0][2]) + (
                                   image[i + 1, j] * compassMatrix[2][1]) + (image[i + 1, j + 1] * compassMatrix[2][2])
                if temp > newImage[i, j]:
                    newImage[i, j] = temp
        compassMatrix = rotateMatrix(compassMatrix)

    # Image thresholding
    for i in range(1, newImage.shape[0] - 1):
        for j in range(1, newImage.shape[1] - 1):
            if newImage[i, j] > 100:
                newImage[i, j] = 255
            else:
                newImage[i, j] = 0

    cv2.imwrite("Compass_Edge_Detector.jpg", newImage)
    cv2.imshow("Compass Edge Detector", newImage)


# read image
image = cv2.imread("example.png", 0)

CompassEdgeDetector(image)

cv2.imshow("Original image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()