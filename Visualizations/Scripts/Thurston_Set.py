import numpy as np
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import csv
import random as rand
import ast

real = []
imagine = []


def f0(z, alpha):
    return alpha * z


def f1(z, alpha):
    return 2 - alpha * z



def do_ifs(axis, alpha, z):
    output = f0(z, alpha)
    for j in range(1000):
        for i in range(100):
            random = rand.randint(0, 99)

            if random % 2 == 0:
                output = f0(output, alpha)
            else:
                output = f1(output, alpha)
        axis.scatter(output.real, output.imag, marker='.', color='c')

with open("24.txt") as r:
    for line in r:
        n = 24
        It = ast.literal_eval(line)
        coe = [0 for i in range(n + 1)]
        coe[0] = 1
        coe[n] = -1
        for j in It:
            sumit = It.index(j)
            coe[j + 1] = coe[j + 1] + (-2) * (sumit % 2 * (-2) + 1)
        roots = np.roots(coe)
        for j in roots:
            real.append(j.real)
            imagine.append(j.imag)

figsrc, axsrc = plt.subplots()
figzoom, axzoom = plt.subplots()
figifs, axifs = plt.subplots()

axsrc.set(xlim=(-2, 2), ylim=(-2, 2), autoscale_on=False,
          title='Click to zoom')
axzoom.set(xlim=(-2, 2), ylim=(-2, 2), autoscale_on=False,
           title='Zoom window')


axsrc.scatter(real, imagine, s=.0003, marker='.', color='c')
axzoom.scatter(real, imagine, s=3, marker='.', color='c')

def onpress(event):
    if event.button != 1:
        return
    axifs.clear()
    axifs.set(title="IFS")
    x, y = event.xdata, event.ydata
    temp = axzoom.scatter(x, y, s=10, marker='.', color='r')
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)
    figzoom.canvas.draw()
    do_ifs(axifs, complex(x, y), 0)
    figifs.canvas.draw()
    temp.remove()

figsrc.canvas.mpl_connect('button_press_event', onpress)
plt.show()

#plt.scatter(.4, .55, color='red')
#plt.xlim(.35, .45)
#plt.ylim(.5, .6)
#plt.show()

#.4 + 55i