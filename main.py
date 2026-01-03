from skimage.filters import median
from skimage.morphology import ball
from PIL import Image

test=load_image("C:\Users\noazi\Downloads\Road_runner.jpg")
clean_image = median(test)
edge_test=edge_detection(clean_image)
plt.imshow(edge_test, cmap='gray')
edge_binary = np.logical_and(edge_test > 5 ,edge_test < 7)
edge_image = Image.fromarray(edge_binary)
edge_image.save('my_edges.png')
