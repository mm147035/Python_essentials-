import matplotlib.pyplot as plt
import numpy as np

data = np.random.random((10, 10))

plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')
plt.show()
