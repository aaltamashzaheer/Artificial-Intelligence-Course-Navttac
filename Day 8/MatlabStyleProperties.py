import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([0,10,0,15,0,20])
x2 = np.array([10,0,15,0,20,0])
plt.plot(x1 ,marker = "o", ls = ":", c = "r", lw = 1,)
plt.plot(x2,marker = "o", ls = "", c = "b", lw = 10,)

plt.show()