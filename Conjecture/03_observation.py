#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 00:38:18 2021

@author: zoezhou
"""
import math
import csv
import random

orbit = []
itinerary = []
beta = []
q = math.sqrt((1+math.sqrt(5))/2)

#read the csv file
with open("02_multi_roots.txt") as Data:
    readCSV = csv.reader(Data, delimiter= ",")
    next(readCSV)
    for row in readCSV:
        orbit.append(int(row[0]))
        It_raw = row[1].strip('[').strip(']').strip(' ').split(',')
        It = [int(i) for i in It_raw]
        itinerary.append(It)
        b_raw = row[2].strip('[').strip(']').strip(' ').split(',')
        b = [float(i) for i in b_raw]
        beta.append(b)

def itin(orbit,itinerary):
    it = [0 for i in range(orbit)]
    for i in itinerary:
        it[i] = 1
    return it

def newit(beta,orbit):
    x = 1
    it = []
    for i in range(orbit):
        if x < 1/beta:
            x = beta * x
            it.append(0)
        else:
            x = 2 - beta * x
            it.append(1)
    return(it,x)
   
    

#observation: the larger real root is always the critical period beta 
n = len(orbit)
for i in range(5):
    r = random.randint(0, n)
    print('*** random row #',r,"***")
    print(" orbit:",orbit[r])
    print(" itinerary:",itin(orbit[r],itinerary[r]))
    print(" beta:",beta[r])
    print(" the itinerary for beta1 is", newit(beta[r][0],orbit[r])[0])
    print(" f^",orbit[r],"(1)=",newit(beta[r][0],orbit[r])[1])
    print(" the itinerary for beta2 is", newit(beta[r][1],orbit[r])[0])
    print(" f^",orbit[r],"(1)=",newit(beta[r][1],orbit[r])[1])
    


        