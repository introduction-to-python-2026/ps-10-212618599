from PIL import Image
import numpy as np
from scipy.signal import convolve2d
from scipy import signal
import matplotlib.pyplot as plt

def load_image(path):
 img = Image.open(path)
 img_array = np.array(img)
 if img_array.ndim == 2:
  img_array = img_array[:, :, np.newaxis]
 return img_array

def edge_detection(image):
 if image.ndim == 3 and image.shape[-1] == 3:
  gray_image = np.mean(image, axis=2)
 else:
  gray_image = image
 kernelY = np.array([[ 1, 2, 1],
                        [ 0, 0, 0],
                        [ -1, -2, -1]])
 kernelX = np.array([[ 1, 0, -1],
                        [ 2, 0, -2],
                        [ 1, 0, -1]])
 edge_X = signal.convolve2d(gray_image, kernelX, mode='same')
 edge_Y = signal.convolve2d(gray_image, kernelY, mode='same')
 edgeMAG = np.sqrt(edge_X**2 + edge_Y**2)]
 return edgeMAG
