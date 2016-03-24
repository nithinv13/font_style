import Image
import numpy as np
import scipy.misc
import webbrowser
from skimage.io import imread

filename = "test_document.jpg"
webbrowser.open(filename)

im = imread("test_document.jpg")
for i in range(1):
 for j in range(1):
  print(im[i][j])

print(im.shape)
im1 = np.random.randint(0, 255, (36, 90,3))

#scipy.misc.imsave('outfile.jpg', im1)
#webbrowser.open("outfile.jpg")

#im1=im
for i in range(36):
 for j in range(30):
  for k in range(3):
   im1[i][j][k]=im[i][j][k]

scipy.misc.imsave('outfile1.jpg', im1)
webbrowser.open("outfile1.jpg")   

#for i in range(1):
#for j in range(30):
# print(im1[15][j])

print(im1.shape)  
