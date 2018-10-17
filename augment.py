import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib
from scipy.ndimage import rotate
import os
import re
import sys


label = sys.argv[1]
print("This is the directory I will augment: ", label)

dirname = "images/" + label

aug_dir = dirname + "_augmented/"

if (os.path.exists(aug_dir) == False):
  os.mkdir(aug_dir)

images = []
for root, dirnames, filenames in os.walk(dirname):
    for filename in filenames:
        if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            filepath = os.path.join(root, filename)

            img = Image.open( filepath )
            img_array = np.array( img, dtype='uint8' )

            img_name = aug_dir + filename
            matplotlib.image.imsave(img_name, img_array)

            img_name90 = aug_dir + "aug90_" + filename
            rot = rotate(img_array, 90, reshape=False)
            matplotlib.image.imsave(img_name90, rot)

            img_name180 = aug_dir + "aug180_" + filename
            rot = rotate(img_array, 180, reshape=False)
            matplotlib.image.imsave(img_name180, rot)

            img_name270 = aug_dir + "aug270_" + filename
            rot = rotate(img_array, 270, reshape=False)
            matplotlib.image.imsave(img_name270, rot)


