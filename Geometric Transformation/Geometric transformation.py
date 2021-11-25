import cv2
import numpy as np
import math


def TranslationImage(image, x, y):
    newImage = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    translationMatrix = np.matrix([[1, 0, x], [0, 1, y], [0, 0, 1]])
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            result = np.matmul(translationMatrix, np.matrix([[i], [j], [1]]))
            if (result[0, 0] >= 0 and result[0, 0] < image.shape[0]) and (
                    result[1, 0] >= 0 and result[1, 0] < image.shape[1]):
                newImage[result[0, 0], result[1, 0]] = image[i, j]

    return newImage


def ScalingImage(image, x, y):
    newImage = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    scalingMatrix = np.matrix([[x, 0, 0], [0, y, 0], [0, 0, 1]])
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            result = np.matmul(scalingMatrix, np.matrix([[i], [j], [1]]))
            if ((result[0, 0] >= 0 and result[0, 0] < image.shape[0]) and (
                    result[1, 0] >= 0 and result[1, 0] < image.shape[1])):
                newImage[result[0, 0], result[1, 0]] = image[i, j]

    return newImage


def RotationImage(image, angle):
    newImage = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    a = math.cos(angle)
    b = math.sin(angle)
    cx = image.shape[0] // 2
    cy = image.shape[1] // 2
    rotationMatrix = [
        [a, b, (1 - a) * cx - b * cy],
        [-b, a, b * cx + (1 - a) * cy],
        [0, 0, 1]
    ]
    M = np.matrix([[math.cos(angle), math.sin(angle),
                    (1 - math.cos(angle) * image.shape[0] // 2 - math.sin(angle) * image.shape[1] // 2)],
                   [-math.sin(angle), math.cos(angle),
                    math.sin(angle) * image.shape[0] // 2 + (1 - math.cos(angle)) * image.shape[1] // 2], [0, 0, 1]])
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            result = np.matmul(rotationMatrix, np.matrix([[i], [j], [1]]))
            if ((abs(result[0, 0]) >= 0 and abs(result[0, 0]) < image.shape[0]) and (
                    abs(result[1, 0]) >= 0 and abs(result[1, 0]) < image.shape[1])):
                newImage[abs(int(result[0, 0])), abs(int(result[1, 0]))] = image[i, j]

    return newImage


# read image
image = cv2.imread("example.png", 0)

while (True):
    print("1.Translation")
    print("2.Scaling")
    print("3.Rotation")
    print("4.Exit")
    selection = int(input("Write your selection:"))

    if (selection == 1):
        x = int(input("X:"))
        y = int(input("Y:"))
        image = TranslationImage(image, x, y)
        cv2.imshow("Original image", image)
        cv2.imwrite("Translation_image.jpg", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif (selection == 2):
        x = int(input("X:"))
        y = int(input("Y:"))
        image = ScalingImage(image, x, y)
        cv2.imshow("Original image", image)
        cv2.imwrite("Scaling_image.jpg", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif (selection == 3):
        angle = float(input("Rotation Angle:"))
        image = RotationImage(image, angle)
        cv2.imshow("Original image", image)
        cv2.imwrite("Rotation_image.jpg", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        break
