from imgaug import augmenters as iaa
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib
from scipy.ndimage import rotate


filename = 'mel-is9.jpg'

img = Image.open( "melanoma/" + filename )
img_array = np.array( img, dtype='uint8' )

img_name ="melanoma/aug" + filename

rot = rotate(img_array, 180, reshape=False)


matplotlib.image.imsave(img_name, rot)


#img_array = np.load(filename + '.npy')
#
#plt.imshow(img_array)



#seq = iaa.Sequential([
#    iaa.Crop(px=(0, 16)), # crop images from each side by 0 to 16px (randomly chosen)
#    iaa.Fliplr(0.5), # horizontally flip 50% of the images
#    iaa.GaussianBlur(sigma=(0, 3.0)) # blur images with a sigma of 0 to 3.0
#])
#
#for batch_idx in range(1000):
#    # 'images' should be either a 4D numpy array of shape (N, height, width, channels)
#    # or a list of 3D numpy arrays, each having shape (height, width, channels).
#    # Grayscale images must have shape (height, width, 1) each.
#    # All images must have numpy's dtype uint8. Values are expected to be in
#    # range 0-255.
#    images = load_batch(batch_idx)  # you have to implement this function
#    images_aug = seq.augment_images(images)  # done by the library
#    train_on_images(images_aug)  # you have to implement this function
#
#def load_batch(batch_idx):


