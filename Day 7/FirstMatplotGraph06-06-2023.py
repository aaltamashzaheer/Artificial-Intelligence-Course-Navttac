import matplotlib.pyplot as plt
import numpy as np

y_axis=np.array([3 ,8 ,1 ,10])
x_axis=np.array([4,6,8,9])

plt.plot(x_axis, '*:r', y_axis)
plt.title("My first graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()