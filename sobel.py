import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.signal
import matplotlib.image as mpimg
import sys

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def main(argv1,argv2):
    arv1 = str(argv1)
    # Load an image
    f = np.array(Image.open(argv1))

    print(f.shape)
    print(f)
    print "\n"

    filter_gx_sobel = np.array([
            [1.0, 0.0, -1.0],
            [2.0, 0.0, -2.0],
            [1.0, 0.0, -1.0],
        ])

    filter_gy_sobel = np.array([
            [1.0, 2.0, 1.0],
            [0.0, 0.0, 0.0],
            [-1.0, -2.0, -1.0],
        ])

    if(len(f.shape)<3):
          print 'gray'
    elif len(f.shape)==3:
          f = rgb2gray(f)

    sobel_x = []
    sobel_y = []

    sobel_x = scipy.signal.convolve2d(f, filter_gx_sobel, mode='same')
    sobel_y = scipy.signal.convolve2d(f, filter_gy_sobel, mode='same')

    sobelmag = np.sqrt(sobel_x * sobel_x + sobel_y * sobel_y)

    sobelmag_max = np.max(sobelmag)
    threshold = float(argv2) * sobelmag_max #calculate threshold value

    h,w = sobelmag.shape

    for i in range(0,h):
        for j in range(0,w):
            if(sobelmag[i][j]>=threshold):
                sobelmag[i][j]=255.0
            else:
                sobelmag[i][j]=0

    print sobelmag.shape
    print sobelmag

    plt.imshow(sobelmag, cmap='gray')
    plt.show()

if __name__ == "__main__":

    main(sys.argv[1],sys.argv[2])
