import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# setting properties such as colors, line width, etc
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#alpha is the transcription
#line style available ls for line style
# marker the dots for example on the line
# marker face color to change the clor of the marker
# you can also edit the marker's width
ax.plot(x, y, label = 'X Squared', color = '#FF8C00', linewidth = 2,
    alpha = 0.7, ls = '-', marker = 'o', markersize = 9,
    markerfacecolor = 'blue', markeredgewidth = 3,
    markeredgecolor = 'purple')

# set the axes appearance style
#ax.set_xlim([0, 1])
#ax.set_ylim([0, 2])

ax.legend(loc = 0)
plt.show()

# special plot types
