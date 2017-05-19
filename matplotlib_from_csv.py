import matplotlib.pyplot as plt
import csv

# example from https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/
x = []
y = []
labelx = ''
labely = ''
with open('data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    counter = 0
    for row in plots:
        if counter == 0:
            labelx = row[0]
            labely = row[1]
        else:
            x.append(int(row[0]))
            y.append(int(row[1]))
        counter += 1

line1 = plt.plot(x, y, label='Loaded from file!')
plt.xlabel(labelx)
plt.ylabel(labely)
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
