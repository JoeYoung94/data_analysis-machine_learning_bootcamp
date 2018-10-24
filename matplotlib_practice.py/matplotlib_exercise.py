import numpy as np
x = np.arange(0, 100)
y = x * 2
z = x ** 2

import matplotlib.pyplot as plt

fig,axes = plt.subplots(1, 2, figsize = (12, 3))
axes[0].plot(x, y, color = 'blue', ls = '--')
axes[1].plot(x, z, color = 'red', lw = 3)


plt.show()
