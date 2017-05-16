import matplotlib.pyplot as plt
import csv

# example from https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/
x = []
y = []

with open('data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
