import numpy as np
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
from mpl_toolkits.mplot3d import Axes3D
import csv

real = []
imagine = []
betas = []
frame = 0
iter = 0
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-2, 2)
ax.set_zlim3d(.9, 2.1)

#plots some teapot values and saves the updated image as teapot.png
def plot(real, imagine, betas, ax, c):
    ax.scatter(real, imagine, betas, s=.01, alpha=1, c=betas)
    plt.savefig('teapot.png'.format(frame))

with open('itinerary.csv') as file:
    readCSV = csv.reader(file, delimiter=',')
    currentIt = -1
    next(readCSV)
    for row in readCSV:
        n = int(row[0])
        #shade each orbit length as a different color
        if n != currentIt:
            plot(real, imagine, betas, ax, cm.rainbow(np.linspace(0, 1, len(real))))
            plot(real, imagine, betas, ax, frame, [])
            real = []
            imagine = []
            betas = []
            currentIt = n
        #parse the csv
        It_raw = row[1].strip('[').strip(']').strip(' ').split(',')
        It = [int(i) for i in It_raw]
        coe = [0 for i in range(n + 1)]
        coe[0] = 1
        coe[n] = -1
        for j in It:
            sumit = It.index(j)
            coe[j + 1] = coe[j + 1] + (-2) * (sumit % 2 * (-2) + 1)
        roots = np.roots(coe)
        max_real = 0.0
        for j in roots:
            real.append(j.real)
            imagine.append(j.imag)
            if j.imag == 0.0 and j.real > max_real:
                max_real = j.real
        for i in range(0, len(roots)):
            betas.append(max_real)
        iter = iter + 1
