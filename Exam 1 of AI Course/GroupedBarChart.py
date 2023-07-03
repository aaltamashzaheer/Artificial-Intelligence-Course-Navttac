import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y1 = [1500,2200,1800,3000,2500,2800,2100,3200,2700,2300,1900,3500]
y2 = [1700,2400,2000,3200,2700,3000,2300,3400,2900,2500,2100,3700]
width = 0.40
plt.xticks(x, ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.bar(x-0.2, y1, width)
plt.bar(x+0.2, y2, width)
plt.show()
