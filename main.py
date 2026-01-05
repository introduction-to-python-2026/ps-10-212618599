import matplotlib as plt
import numpy as np
from skimage.filters import median
from skimage.morphology import ball
from PIL import Image
from image_utils import load_image , edge_detection


test=load_image("Road_runner.jpg")
clean_image = median(test,ball(3))
edge_test=edge_detection(clean_image)
threshold_value=50
edge_binary = edge_test > threshold_value

plt.figure(figsuze=((10,5))
plt.imshow(edge_binary, cmap='gray')
plt.axis('off')
plt.show()

edge_image = Image.fromarray(edge_binary*255)
edge_image.save('my_edges.png')
