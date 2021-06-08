#from process.CubeController import CubeController
from process.ImageParser import prepare_image, image_as_subregions
import numpy as np

# cube = CubeController()
# cube.run()
x = prepare_image("C:/Users/moezb/OneDrive/Desktop/Python Projects/RubikMosaic/statics/test.jpg", 4)
for i, arr in enumerate(image_as_subregions(x[1])):
    print(f"Subregion {i+1}:")
    print(arr)
    print("\n\n\n")

# [[[255 165   0]
#   [255 165   0]
#   [255 165   0]
#   [255 165   0]
#   [255 165   0]
#   [255 165   0]]
#
#  [[255 165   0]
#   [246   0   0]
#   [255 165   0]
#   [  0   0 179]
#   [246   0   0]
#   [255 165   0]]
#
#  [[255 165   0]
#   [246   0   0]
#   [246   0   0]
#   [246   0   0]
#   [246   0   0]
#   [  0   0 179]]
#
#  [[255 165   0]
#   [246   0   0]
#   [246   0   0]
#   [246   0   0]
#   [246   0   0]
#   [  0   0 179]]
#
#  [[  0   0 179]
#   [246   0   0]
#   [246   0   0]
#   [246   0   0]
#   [246   0   0]
#   [  0   0 179]]
#
#  [[  0   0 179]
#   [  0   0 179]
#   [  0   0 179]
#   [  0   0 179]
#   [  0   0 179]
#   [  0   0 179]]]