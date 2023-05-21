import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
data = np.random.normal(100, 20, 200)

plt.violinplot(data, vert=False)
plt.xlabel('Data')
plt.ylabel('Values')
plt.title('Violin Plot')
plt.show()
