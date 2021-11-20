import cv2
import numpy as np
import math


# Prewit Edge Detector Function
def PrewitEdgeDetector(image):
    prewitImage = np.zeros((image.shape[0], image.shape[1]))
    # Image masking
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            xSum = int(image[i - 1, j + 1]) + int(image[i, j + 1]) + int(image[i + 1, j + 1]) - int(
                image[i - 1, j - 1]) - int(image[i, j - 1]) - int(image[i + 1, j - 1])
            ySum = int(image[i - 1, j - 1]) + int(image[i - 1, j]) + int(image[i - 1, j + 1]) - int(
                image[i + 1, j - 1]) - int(image[i + 1, j]) - int(image[i + 1, j + 1])
            prewitImage[i, j] = int(round(math.sqrt((xSum * xSum) + (ySum * ySum))))

    cv2.imwrite("Prewit_Edge_Detector_before_thresholding.jpg", prewitImage)

    # Image thresholding
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            if prewitImage[i, j] >= 55:
                prewitImage[i, j] = 255
            else:
                prewitImage[i, j] = 0

    cv2.imwrite("Prewit_Edge_Detector.jpg", prewitImage)


# Robert Edge Detector Function
def RobertEdgeDetector(image):
    # Image masking
    robertImage = np.zeros((image.shape[0], image.shape[1]))
    for i in range(0, image.shape[0] - 1):
        for j in range(0, image.shape[1] - 1):
            robertImage[i, j] = int(round(math.sqrt(((int(image[i, j]) - int(image[i + 1, j + 1])) ** 2) + (
                        (int(image[i + 1, j]) - int(image[i, j + 1])) ** 2))))

    cv2.imwrite("Robert_Edge_Detector_before_thresholding.jpg", robertImage)

    # Image thresholding
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            if robertImage[i, j] > 18:
                robertImage[i, j] = 255
            else:
                robertImage[i, j] = 0

    cv2.imwrite("Robert_Edge_Detector.jpg", robertImage)


# Main function and calling functions which are created
# read image
image = cv2.imread("example.png", 0)

RobertEdgeDetector(image)
PrewitEdgeDetector(image)

cv2.imshow("Original image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()