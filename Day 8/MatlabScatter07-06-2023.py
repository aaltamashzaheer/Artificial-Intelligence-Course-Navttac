import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(100,size=(100))
y= np.random.randint(100,size=(100))
w = 30
plt.xlabel(w)
colors = np.random.randint(100,size=(100))
sizes = 1*np.random.randint(100,size=(100))
plt.scatter(x,y,c = colors,s = sizes,alpha=2)
plt.colorbar()
plt.grid()

plt.show()