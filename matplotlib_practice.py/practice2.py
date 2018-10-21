import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig,axes = plt.subplots(nrows = 1, ncols = 2)
for current_ax in axes:
    current_ax.set_xlabel('X')
    current_ax.set_ylabel('Y')

axes[0].set_title("y = x ** 2")
axes[1].set_title("x = y ** 2")
axes[0].plot(x, y, 'r--')
axes[1].plot(y, x, 'b*-')

plt.tight_layout()
#plt.show()   #uncomment this row to show the first plot

# figure size and DPI (dots per inch)
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (8, 4))

for current_ax in axes:
    current_ax.set_xlabel('X')
    current_ax.set_ylabel('Y')

axes[0].set_title("y = x ** 2")
axes[1].set_title("x = y ** 2")
axes[0].plot(x, y, 'r')
axes[1].plot(y, x, 'g')
plt.tight_layout()
# plt.show() # uncomment this row to show the second plot

# save figure methods
# uhncomment this line to save the figure
# fig.savefig('practice2.png', dpi = 300)

# figure legend
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, x ** 2, label = 'X Squared')
ax.plot(x, x ** 3, label = 'X Cubed')

ax.legend(loc = 0)
plt.show()
