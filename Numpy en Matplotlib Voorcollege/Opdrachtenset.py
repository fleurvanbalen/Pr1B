import numpy as np
import matplotlib.pyplot as plt
from fitcode import curve_fit

## Opdracht 1 en 2: Plot van een functie
x = np.linspace(0, 10, 1000)

# def physics(x, a, b):
#     return a*x*np.sin(b+x)*np.cos(x*x)

# Hergedefinieerd voor opdracht 4
def physics(params, x):
    return params[0]*x*np.sin(params[1]+x)*np.cos(x*x)

# y = physics([1,1], x)
# print(x.shape)
# print(y.shape)

# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')

## Opdracht 3: Data plotten met foutenbalken

# Importeer het csv bestand in een array
datapunten = np.genfromtxt('datapunten.csv', delimiter=',')
#print 2de kolom om te oefenen
#for i in datapunten:
#    print(i[1])

# Maak aparte arrays voor de verschillende kolommen
xdata = []
ydata = []
sxdata = []
sydata = []

for i in datapunten:
    xdata.append(i[0])
    ydata.append(i[1])
    sxdata.append(i[2])
    sydata.append(i[3])

# Plotten
# plt.errorbar(xdata, ydata, sydata, sxdata, fmt='o')
# plt.show()

## Opdracht 4: Fitten van een functie
# Voer optimalisatie uit (oftewel: het fitten)
gok = [1, 1]
parameters, onzekerheden, check = curve_fit(physics, xdata, ydata, sxdata, sydata, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))


yfit = physics(parameters, x)
plt.plot(x, yfit)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data met gefitte curve')
plt.errorbar(xdata, ydata, sydata, sxdata, fmt='o')
plt.grid(True, 'major')
plt.savefig('plot_opdrachtenset.png')
plt.show()
