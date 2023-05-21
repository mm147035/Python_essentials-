import matplotlib.pyplot as plt

sizes = [30, 25, 15, 10, 20]
labels = ['A', 'B', 'C', 'D', 'E']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
