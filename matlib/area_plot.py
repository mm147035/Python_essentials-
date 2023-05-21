import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 6, 8, 9]
y2 = [2, 2, 7, 10, 12]

plt.stackplot(x, y1, y2, labels=['Y1', 'Y2'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Plot')
plt.legend()
plt.show()
