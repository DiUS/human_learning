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

images = []
for root, dirnames, filenames in os.walk(dirname):
    for filename in filenames:
        if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            filepath = os.path.join(root, filename)

            img = Image.open( filepath )
            img_array = np.array( img, dtype='uint8' )
            img_name = dirname + "_augmented/" + "aug_" + filename
            rot = rotate(img_array, 180, reshape=False)
            matplotlib.image.imsave(img_name, rot)


