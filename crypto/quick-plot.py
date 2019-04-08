# pip install matplotlib
import matplotlib.pyplot as plt

x = []
y = []

fig, axes = plt.subplots(1, 1, sharex=True)
axes.scatter(x, y, marker=".")

#flip-y
#plt.gca().invert_yaxis()

#flip-x
#plt.gca().invert_xaxis()

plt.show()