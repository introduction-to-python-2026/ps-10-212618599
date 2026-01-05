from skimage.morphology import ball
from skimage.filters import median
from PIL import Image
import numpy as np
from scipy.signal import convolve2d
from scipy import signal
import matplotlib.pyplot as plt

def load_image(path):
    img = Image.open(path)
    img_array = np.array(img)
    return img_array

def edge_detection(image):
    gray_image = np.mean(image, axis=2)  # Convert to grayscale   
    kernelY = np.array([[ 1, 2, 1],
                        [ 0, 0, 0],
                        [ -1, -2, -1]])
    
    kernelX = np.array([[ 1, 0, -1],
                        [ 2, 0, -2],
                        [ 1, 0, -1]])
    edge_X = signal.convolve2d(gray_image, kernelX, mode='same')
    edge_Y = signal.convolve2d(gray_image, kernelY, mode='same')
    edgeMAG = np.sqrt(edge_X**2 + edge_Y**2)
    return edgeMAG
