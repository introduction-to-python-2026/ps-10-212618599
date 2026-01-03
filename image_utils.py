from PIL import Image
import numpy as np
from scipy.signal import convolve2d
from scipy import signal
import matplotlib.pyplot as plt

def load_image(path):
 img = Image.open(path)
 return img

def edge_detection(image):
 gray_image = np.mean(image, axis=2)
 plt.axis('off')
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
