#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 20:55:52 2020

@author: zhouziyi
"""

real = []
imag = []
i = 0

with open("00_Data.txt") as Data:
    readCSV = csv.reader(Data, delimiter=',')
    next(readCSV)

    for row in readCSV:
        betar = float(row[1].split(",")[0])
        #if (betar == beta) & (i == 0):
        #    n = row[0]
        #    s_raw = row[2].strip('[').strip(']').strip(' ').split(',')
        #    s = [int(i) for i in s_raw]
        #    print('********Input********')
            
        #    print('n:', n)
        #    print('beta:', beta)
        #    print('encoded string:', s)
        #    i = 1
        #elif betar < beta:
        it_raw = row[2].strip('[').strip(']').strip(' ').split(',')
        it = [int(i) for i in it_raw]
        n = int(row[0])
        coe = [0 for i in range(n + 1)] 
        coe[0] = 1 
        coe[n] = -1 
        for j in it:
            sumit = it.index(j) 
            coe[j + 1] = coe[j + 1] + (-2) * (sumit%2 * (-2) + 1) 
        roots = np.roots(coe)
        for j in roots:
            real.append(j.real)
            imag.append(j.imag)
                
#for c in clist:
    #print('c:', complex(c[0], c[1]))
    #print('********Slice of Teapot when beta = ', beta,', c =',c, '********')

plt.show()
fig, ax = plt.subplots(figsize=(15, 15))


plt.scatter(real,imag,s=.0003,marker='.')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)


for i in Max:
    R = i
    n = 64

    t = np.linspace(0, 2*np.pi, n+1)
    x = R*np.cos(t)
    y = R*np.sin(t)

    plt.plot(x,y,'#4b8bbe')
    
for i in Min:
    R = i
    n = 64

    t = np.linspace(0, 2*np.pi, n+1)
    x = R*np.cos(t)
    y = R*np.sin(t)

    plt.plot(x,y,'orange')      
    
    
nlist = [i+3 for i in range(len(Max))]

from matplotlib.pyplot import MultipleLocator


fig, ax = plt.subplots(figsize=(10, 5))
l1, = plt.plot(nlist, Max)
l2, = plt.plot(nlist, Min)
plt.legend(handles=[l1,l2],labels=['Maximum','Minimum'])

plt.xlabel('orbit length')
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)


plt.xlim(3, 24)
plt.show()


rate_Max = []
for i in range(len(Max)-1):
    rate = Max[i + 1] / Max[i]
    rate_Max.append(rate)
nlist2 = [i+3 for i in range(len(rate_Max))]



rate_Min = []
for i in range(len(Min)-1):
    rate =  Min[i + 1] / Min[i]
    rate_Min.append(rate)

fig, ax = plt.subplots(figsize=(10, 5))
l1, = plt.plot(nlist2, rate_Max)
l2, = plt.plot(nlist2, rate_Min)




plt.legend(handles=[l1,l2],labels=['Maximum','Minimum'])

plt.xlabel('orbit length')
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)


plt.axhline(y=1, color='r', linestyle=':')
plt.show()

    


#plt.show() 