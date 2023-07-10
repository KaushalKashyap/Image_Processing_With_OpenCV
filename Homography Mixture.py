# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 02:24:41 2023

@author: RANGER
"""
"""
Homography describes the relationship between two planes. This means a straight line in one plane can be mapped out in another.
 Applied to an image, we can map points from the original image to another. This technique can be applied when doing image stitching,
 alignment, and object tracking.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2gray
from matplotlib.patches import Circle
from skimage import transform

# Load image
board_img = imread('snakeandladder.jpg')

# Plot
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax.imshow(board_img)
ax.set_title('Original Image of Snakes and Ladders Game')
ax.set_axis_off()
plt.show()

# We will generate a new image that is a top view of this snake & ladders board for our case. 
# To do this, we need points in the original images that can be mapped to the second image. 
# These points must be at least three noncolinear points. This will serve as anchors to the transformation. 
# We need to find the coordinate of these points. For simplicity and easy tracking, we will get the points that are the corners of the board.

# Get coordinates corners of the board
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax.imshow(board_img)
circ = Circle((360, 138), 10, fill=True, color='darkorange')
ax.add_patch(circ)
circ = Circle((892, 257), 10, fill=True, color='darkorange')
ax.add_patch(circ)
circ = Circle((725, 856), 10, fill=True, color='darkorange')
ax.add_patch(circ)
circ = Circle((62, 602), 10, fill=True, color='darkorange')
ax.add_patch(circ)
ax.set_axis_off()
ax.set_title('Board with Markers on the Corners (basis for transformation)')
plt.show()

# Next, we will get the coordinate we want to map these four points onto the 2nd image. 
# Since we want the top view, these four points must form a square. Also, the order by which these points 
# are arranged in the source image must be the same in the transformed image.

# Source image coordinates
src = np.array([360, 138,
                725, 856,
                62, 602,
                892, 257,]).reshape((4, 2))

# Destination image coordinates
dst = np.array([100, 100,
                650, 650,
                100, 650,
                650, 100,
]).reshape((4, 2))

# Calculate homography matrix and apply it to the image
tform = transform.estimate_transform('projective', src, dst)
tf_img = transform.warp(board_img, tform.inverse)

# Cut the image to show only the board
tf_img = tf_img[70:680, 70:680]

# Plot
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax.imshow(tf_img)
ax.set_title('Projective Transformation of Image')
plt.show()

"""
After the transformation, we have a new image that is the top view of the board of the original image. 
It is not that noticeable here but objects NOT on the same plane as the chosen points are stretched. 
The farther the object is on the same plane as the chosen points, the more stretched out.
"""