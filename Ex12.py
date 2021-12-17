# 2021-12-17_ex03
# Marcel Karbach, 4000031
# Course: Applications of Accelerators

import numpy as np
import matplotlib.pyplot as plt

filename = '2016-07-11_ipm_data.txt'
data = np.genfromtxt(filename)


plt.plot(data, linewidth=1, markersize=1)
plt.plot((np.where(data == np.amax(data))[0]), np.amax(data), 'ro', markersize=1, label ='maximum')
plt.grid(color='k', linewidth=0.5)
plt.legend()
plt.ylabel('Intensity')
plt.xlabel('Distance')
plt.savefig('ipm_plot', dpi=200)
