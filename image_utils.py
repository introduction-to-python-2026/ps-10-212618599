from PIL import Image
import numpy as np
from scipy.signal import convolve2d
from scipy import signal
import matplotlib.pyplot as plt

def load_image(path):
 img = Image.open(path)
 return img
 img_array = np.array(img)
 if img_array.ndim == 2:
  img_array = img_array[:, :, np.newaxis]
 return img_array

def edge_detection(image):
 if image_to_process.ndim == 3 and image_to_process.shape[-1] == 3:
  gray_image = np.mean(image_to_process, axis=2)
 else:
  gray_image = np.squeeze(image_to_process)
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
