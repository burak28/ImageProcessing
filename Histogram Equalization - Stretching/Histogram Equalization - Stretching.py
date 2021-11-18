import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt

toStretchMinValue = 50
toStretchMaxValue = 250
stretchMinValue = 100
stretchMaxValue = 200

# read image
image = cv2.imread("example.png", 0)

# convert image to array and create histogram
matrix = np.array(image)
histogram = np.zeros(256)
histData = []
for i in matrix:
    for j in i:
        histData.append(j)
        histogram[j] = histogram[j] + 1
fig, ax = plt.subplots(3, 1, figsize=(10, 10))
ax[0].hist(x=histData, density=True, bins=25)
ax[0].set_title("Original Histogram")

# histogram stretching
i = stretchMinValue
oldAndNewValueOfHistogram = dict()
while i <= stretchMaxValue:
    newValue = int(((toStretchMaxValue - toStretchMinValue) / (stretchMaxValue - stretchMinValue)) * (
            i - stretchMinValue) + toStretchMinValue)
    oldAndNewValueOfHistogram[i] = newValue
    i = i + 1

histData = []
for i in range(0, np.size(matrix, 0)):
    for j in range(0, np.size(matrix, 1)):
        if list(oldAndNewValueOfHistogram.keys()).count(matrix[i][j]) != 0:
            matrix[i][j] = oldAndNewValueOfHistogram[matrix[i][j]]
        histData.append(matrix[i][j])

ax[1].hist(x=histData, density=True, bins=25)
ax[1].set_title("After Stretching")

# convert image to array and create histogram
matrixEqualization = np.array(image)
histogramEqualization = np.zeros(256)
for i in matrixEqualization:
    for j in i:
        histogramEqualization[j] = histogramEqualization[j] + 1

# histogram equalization
sumOfPixels = matrixEqualization.size
pixelPositions = []
sumOfPossibility = 0

for i in range(256):
    result = np.where(matrixEqualization == i)
    pixelPositions.append(list(zip(result[0], result[1])))

for i in range(256):
    possibility = histogramEqualization[i] / sumOfPixels
    sumOfPossibility = sumOfPossibility + possibility
    newPixelPosition = round(sumOfPossibility * 255)
    for coordinate in pixelPositions[i]:
        matrixEqualization[coordinate] = newPixelPosition
    i = i + 1

histData = []
for i in range(0, np.size(matrixEqualization, 0)):
    for j in range(0, np.size(matrixEqualization, 1)):
        histData.append(matrixEqualization[i][j])

ax[2].hist(x=histData, density=True, bins=25)
ax[2].set_title("After Equalization")

cv2.imshow("Original image", image)
cv2.imshow("Stretching histogram", matrix)
cv2.imshow("Histogram equalization", matrixEqualization)
plt.show()

fig.savefig("histogram.png")
cv2.imwrite("Stretching_histogram.jpg", matrix)
cv2.imwrite("Histogram_equalization.jpg", matrixEqualization)

print('Successfully saved')
cv2.waitKey(0)
cv2.destroyAllWindows()
