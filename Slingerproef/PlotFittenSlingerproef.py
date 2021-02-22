import numpy as np
import matplotlib.pyplot as plt
from fitcode import curve_fit

## Opdracht 1 en 2: Plot van een functie
x = np.linspace(0, 6, 1000)

# def physics(x, a, b):
#     return a*x*np.sin(b+x)*np.cos(x*x)

# Hergedefinieerd voor opdracht 4
def SlingerPlot(params, x):
    return params[0]*x

# y = physics([1,1], x)
# print(x.shape)
# print(y.shape)

# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')

## Opdracht 3: Data plotten met foutenbalken


Trauw = [11.81, 11.336, 10.939, 10.424, 9.87, 9.332]
lrauw = [135.2, 125.2, 115.2, 105.2, 95.2, 85.2]

Trilling = [ x / 5 for x in Trauw]
Lengte = [ x / 100 for x in lrauw]
print(Trilling)
print(Lengte)
xdata = [ x**2 for x in Trilling ]
ydata = [ 4 * np.pi**2 * x for x in Lengte ]
print(xdata)
print(ydata)

sxdata = [x*2*0.031623 for x in xdata]
sydata = 6*[4 * np.pi**2 * 0.007]


# Plotten
# plt.errorbar(xdata, ydata, sydata, sxdata, fmt='o')
# plt.show()

## Opdracht 4: Fitten van een functie
# Voer optimalisatie uit (oftewel: het fitten)
gok = [9.81]
parameters, onzekerheden, check = curve_fit(SlingerPlot, xdata, ydata, sxdata, sydata, gok)
if not check:
    print("FOUTMELDING!!")

for i in range(len(parameters)):
    print("{} +- {}".format(parameters[i], onzekerheden[i]))


# yfit = SlingerPlot(parameters, x)
# plt.plot(x, yfit, color='red')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Data met gefitte curve')
# plt.errorbar(xdata, ydata, sydata, sxdata, fmt='o', color='black')
# plt.grid(True)
# plt.savefig('plot_opdrachtenset.png')
# plt.show()

yfit = SlingerPlot(parameters, x)
plt.plot(yfit, x, color='red', label='Fit: 4\u03c0\u00b2l= 9,59 * T\u00b2')
# plt.plot(SlingerPlot([parameters[0] - onzekerheden[0]], x), x, ls=':', color='red')
# plt.plot(SlingerPlot([parameters[0] + onzekerheden[0]], x), x, ls=':', color='red')
plt.ylabel('T\u00b2 (s\u00b2)')
plt.xlabel('4\u03c0\u00b2l (m)')
plt.errorbar(ydata, xdata, sxdata, sydata, fmt='.', color='black', label='Metingen')
plt.grid(True)
plt.xlim(33, 55)
plt.ylim(3, 6)
plt.legend(loc="upper left")
plt.savefig('plot_opdrachtenset.png', dpi=200)
plt.show()


plt.plot(x, yfit, color='red', label='Fit: 4\u03c0\u00b2l= 9,59 * T\u00b2')
# plt.plot(SlingerPlot([parameters[0] - onzekerheden[0]], x), x, ls=':', color='red')
# plt.plot(SlingerPlot([parameters[0] + onzekerheden[0]], x), x, ls=':', color='red')
plt.xlabel('T\u00b2 (s\u00b2)')
plt.ylabel('4\u03c0\u00b2l (m)')
plt.errorbar(xdata, ydata, sydata, sxdata, fmt='.', color='black', label='Metingen')
plt.grid(True)
plt.xlim(0, 6)
plt.ylim(0, 55)                                                                                                                                                                                                                                                                                                                                     
plt.legend(loc="upper left")
plt.savefig('plot_slingerproef.png', dpi=200)
plt.show()
