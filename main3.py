# AmethystImpala
# 10/08/17
# Challenge 3
# Sources:
# https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder
# https://stackoverflow.com/questions/8783261/python-math-module
# Lecture Slides

from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
from PIL import Image
import os

# Get the Threshold Value
thresh = raw_input("Enter a threshold value [0-255]: ")
thresh = float(thresh)
while (thresh < 0.0) | (thresh > 255.0):
	print "Value is not in range. "
	thresh = raw_input("Enter a threshold value [0-255]: ")
	thresh = float(thresh)


# make a list of all the filenames
path = 'AmethystImpala/starbucks'
data = []
for filename in os.listdir(path):
	data.append(filename)
	
del data[0]

# Calculate the average image
avgImg = Image.open("AmethystImpala/starbucks/starbucks_0.jpg")
for x in range(len(data) - 1):
	img = Image.open("AmethystImpala/starbucks/" + data[x + 1])
	img = np.float64(img)
	avgImg += img

avgImg = avgImg / len(data)	
avgImg = np.clip(avgImg, 0, 255)

# Calculate the standard deviation image
sdImg = Image.open("AmethystImpala/starbucks/starbucks_0.jpg")
sdImg = np.float64(sdImg)
sdImg = sdImg - sdImg
for x in range(len(data)):
	img = Image.open("AmethystImpala/starbucks/" + data[x])
	img = np.float64(img)
	sdImg += pow(img - avgImg, 2)

sdImg = sdImg / (len(data) - 1)
sdImg = np.sqrt(sdImg)
sdImg = np.clip(sdImg, 0, 255)

# Highlighting the pixels in the threshold
for row in range(len(avgImg)):
	for col in range(len(avgImg[0])):
		value = sdImg[row][col][0] + sdImg[row][col][1] + sdImg[row][col][2]
		if value/3 > thresh:
			avgImg[row][col] = [255.0, 0, 0]

# Printing out the image
avgImg = np.uint8(avgImg)

mplot.imshow(avgImg)
mplot.show()
