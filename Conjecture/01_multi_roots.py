#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 22:19:05 2021

@author: zoezhou
"""

import numpy as np
import csv

real = []
imagine = []
betas = []

with open('02_multi_roots.txt', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['orbit', 'Itinerary_String','roots'])

    with open("00_Itinerary_String.txt") as Data:
        readCSV = csv.reader(Data, delimiter= ",")
        next(readCSV)
        for row in readCSV:
            n = int(row[0])
            
            #find the roots for the P polynomials
            It_raw = row[1].strip('[').strip(']').strip(' ').split(',')
            It = [int(i) for i in It_raw]
            coe = [0 for i in range(n + 1)]
            coe[0] = 1
            coe[n] = -1
            for j in It:
                sumit = It.index(j)
                coe[j + 1] = coe[j + 1] + (-2) * (sumit % 2 * (-2) + 1)
            roots = np.roots(coe) 
    
            #record the itinerary with more than two roots
            rep = 0
            temp = []
            for j in roots:
                if j.imag == 0.0 and j.real > 1.0000001:
                    temp.append(j.real)
            if len(temp) > 1:
                thewriter.writerow([n,row[1],temp])
