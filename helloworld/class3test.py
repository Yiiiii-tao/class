import os
from PIL import Image
from skimage import exposure
import numpy as np
import matplotlib.pyplot as plt
img = Image.open('/home/vincent/Pictures/work/Unequalized_Hawkes_Bay_NZ.jpg')
img = np.array(img)
img_eq = exposure.equalize_hist(img)
img_adapteq = exposure.equalize_adapthist(img, clip_limit=0.04)
plt.figure(0)
plt.imshow(img)
plt.title('low contrast image')
plt.figure(1)
plt.imshow(img_eq)
plt.title('high constrast image using normal histogram equalization')
plt.figure(2)
plt.imshow(img_adapteq)
plt.title('high constract image using adaptive histogram euqalization')
plt.show()
