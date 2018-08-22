from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
import mahotas
import numpy

import matplotlib.pyplot as plt

src = '/Users/mko_san/Downloads/e76fdf_ship_map.png'

from PIL import Image

old_im = Image.open(src)
old_size = old_im.size

new_size = (int(old_size[0]*1.1),int(old_size[1]*1.1))
new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
new_im.paste(old_im, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))

image = numpy.array(new_im)
image_gray = rgb2gray(image)
blobs_log = blob_log(image_gray, min_sigma=14, max_sigma=30, num_sigma=10, threshold=.07)
# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
print len(blobs_log)