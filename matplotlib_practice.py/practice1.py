import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# creating multiple plots on same canvas
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r--')
plt.subplot(1, 2, 2)
plt.plot(y, x, 'r*-')
plt.show()


## object oriented programming, here it's gonna create a larger and a smaller
# plot (figure)
fig = plt.figure()

axes1 = fig.add_axes([0.05, 0.05, 0.9, 0.9])
axes2 = fig.add_axes([0.2, 0.5, 0.5, 0.4])

axes1.plot(x, y, 'r--')
axes1.set_title('Larger Plot')
axes1.set_xlabel('X')
axes1.set_ylabel('Y')

axes2.plot(y, x, 'b*-')
axes2.set_title('Smaller Plot')
axes2.set_xlabel('x')
axes2.set_ylabel('y')

plt.show()
