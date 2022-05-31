import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('a1_freq_done.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        if int(row[2]) >= 4:
            y.append(row[1])
            x.append(int(row[2]))

plt.bar(x, y, color='g', width=0.72, label="Total")
plt.xlabel('Words')
plt.ylabel('Count')
plt.title('Dictionary')
plt.margins(tight=False)
plt.legend()
plt.show()