import math
import numpy as np
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5, 6]
y = np.sin(x)

''' Zonder numpy
y = []
for xs in x:
    y.append(math.sin(xs))
'''
print(y)

# Puntenwolkplot
plt.scatter(x,y)
plt.plot(x,y)


# Data 2
x2 = np.linspace(0, 2*np.pi, 1000)
y2 = np.sin(x2)

plt.plot(x2, y2)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("titel")
plt.show()
