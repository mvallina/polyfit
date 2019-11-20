#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="data file")
parser.add_argument("-D", "--deg", type=int, default=1, help="degree of the polynomial")
args = parser.parse_args()

try:
    data = np.genfromtxt(args.file)
except OSError:
    print("El fichero %s no existe" % (args.file))
    exit()
    
x = data[:, 0]
y = data[:, 1]

p = np.poly1d(np.polyfit(x, y, args.degree))
t = np.linspace(x[0], x[len(x) - 1], 1000)

title = ""
n = args.degree
primera_iteracion = True
for coeff in p.coeffs:
    if primera_iteracion:
        if n == 1:
            title += r"$ %f x$" % (coeff)
        elif n == 0:
            title += r"$ %f $" % (coeff)
        else:
            title += r"$ %f x^{%d}$" % (coeff, n)
    else:
        if n == 1:
            title += r"$ %+f x$" % (coeff)
        elif n == 0:
            title += r"$ %+f $" % (coeff)
        else:
            title += r"$ %+f x^{%d}$" % (coeff, n)
    n -= 1
    primera_iteracion = False

print(p)

plt.plot(x, y, "o", t, p(t), "-")
plt.grid()
plt.title(title)
plt.xlabel(r"$v_{gs}$")
plt.ylabel(r"$i_d$")
plt.show()
#plt.savefig("test")
