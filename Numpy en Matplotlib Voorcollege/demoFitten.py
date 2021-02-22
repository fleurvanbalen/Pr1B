import numpy as np
import matplotlib.pyplot as plt
from fitcode import curve_fit

x = [1, 2, 3, 4, 5, 6]
sx = [0.3, 0.22, 0.25, 0.3, 0.26, 0.3] #foutenwaarden

y = [2.1, 2.8, 3.0, 3.7, 4.2, 4.3]
sy = [0.3, 0.4, 0.6, 0.3, 0.4, 0.3]

#Curve die we willen fitten
def curve(params, x):
    return params[0]*x + params[1]

# Voer optimalisatie uit (oftewel: het fitten)
gok = [1, 0]
parameters, onzekerheden, check = curve_fit(curve, x, y, sx, sy, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))

# Coordinaten van curve bepalen
curve_x = np.linspace(0, 7, 1000)
curve_y = curve(parameters, curve_x)

# Maak plot en laat zien
plt.errorbar(x, y, sy, sx, fmt='o') #fmt='o' haalt de lijnen weg en tekent bolletjes
plt.plot(curve_x, curve_y)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('a koel fitted graph')
plt.show()