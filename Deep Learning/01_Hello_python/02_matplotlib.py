import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y = np.sin(x)
print(y)

plt.Figure(x,y)
plt.show()
