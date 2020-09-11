#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 04:03:40 2020

@author: zhouziyi
"""

import numpy as np 
import itertools 
import pandas as pd
import matplotlib.pyplot as plt
import csv

clist = [[0.282888173224922, 0.645528282687951]]
betalist = [1.8260327154073]

for beta in betalist:
        
        real = []
        imag = []
        i = 0

        with open("00_Data.txt") as Data:
            readCSV = csv.reader(Data, delimiter=',')
            next(readCSV)

            for row in readCSV:
                betar = float(row[1].split(",")[0])
                if (betar == beta) & (i == 0):
                    n = row[0]
                    s_raw = row[2].strip('[').strip(']').strip(' ').split(',')
                    s = [int(i) for i in s_raw]
                    print('********Input********')
                    
                    print('n:', n)
                    print('beta:', beta)
                    print('encoded string:', s)
                    i = 1
                elif betar < beta:
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
                        
        for c in clist:
            print('c:', complex(c[0], c[1]))
            print('********Slice of Teapot when beta = ', beta,', c =',c, '********')
            plt.scatter(real,imag,s=.0003,marker='.')
            plt.xlim(c[0] - 0.45, c[0] + 0.45)
            plt.ylim(c[1] - 0.3, c[1] + 0.3)
            plt.plot(c[0], c[1], marker='o', markersize=0.8, color="red")
            plt.show() 
