# This program uses the Matplotlib library to create a line graph.

import matplotlib.pyplot as plt

# Define x and y values
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line graph using the plot() function
plt.plot(x, y)

# Add labels and a title to the graph
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph')

# Display the graph
plt.show()
