#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:08:18 2020

@author: zhouziyi
"""

# all the beta that has orbit less than n

import numpy as np # Library for nulti-dimension arraies or matrices
import itertools # For the sake of finding combination
import pandas as pd
import matplotlib.pyplot as plt

def supertt(n): # Define a function that gives us all the supperattracting beta with orbits less than n
    
    betaorbit = [[] for i in range (n)]
    
    for n in range(3, n + 1): # while orbits is 3, 4, 5, ... , n
        
        allbeta= []
        
        # The following function is to shift the itenarary string
        def shift(x):
            d = x[1] - x[0]
            for i in range(len(x) - 1):
                x[i] = x[i + 1] - d
            x[len(x) - 1] = n - d
            return x

        # The followintg function is to determine if the itenarary string satiafies the twisting
        def admissible(x):
            x0 = [i for i in x] # x0 is the original string
            i = 0
            while i < len(x) - 1: # For each itenarary string, we compare it for at most len(x) - 1 times
                shift(x) # shift the x
                for j in range(len(x)):
                    if x0[j]*(-1)**j > x[j]*((-1)**j): # If the ith digit is different and does not satisfies the twist relation, it falses the admissible test
                        return False
                    if x0[j] == x[j]:
                        if j == len(x) - 1: # If x0 and x are the same after some shift, then this sequence is a repitition, and we ruled it out
                            return False 
                    else: # If the ith digit between x0 and x are different, satisties the twist, and is not a repitition, then this shift of x pass the test
                        break
                i = i + 1
            return True # If all the shift pass the test, then this string is admissible, and we return true
        
        # This section is to generate the string for Itenarary which sum of digits are even
        itlist = []
        even = [i for i in range(2,n) if i%2==0] # The possible even numbers of digits are 2, 4, ...
        for l in even: 
            num = [i for i in range(2, n)] # The possible posistions for the ones are 2, 3, ..., n - 1
            it = list(itertools.combinations(num, l - 1)) # we pick L - 1 numbers of positions (the first one is fixed at the position 0 so we - 1)
            it = [list(i) for i in it] # convert the elements from set to list
            for i in range(len(it)):
                it[i] = list(it[i]) # We converge the combinations as list
                it[i].insert(0,0) # We insert the first 1 at index 0
                z = [i for i in it[i]]
                if admissible(it[i]) == True: # We add this string to the itlist if it satisfies the admissible test
                    it[i] = z
                    itlist.append(it[i])
                    

        # This section we find the coefficient of Parry polynomials for all the strings in itlist
        coelist = [[] for i in range(len(itlist))] # initial the list with propriate numbers of entries
        for i in range(len(coelist)): # Generate the coefficitent
            coe = [0 for i in range(n + 1)] # initial the list with propriate numbers of entries, note that there are n + 1 coefficitents for orbit n
            coe[0] = 1 # The first one is 0 according to the formula
            coe[n] = -1 #The constant -1 according to the formula
            for j in itlist[i]:
                sumit = itlist[i].index(j) # To see how many 1 are there in front of the jth index
                coe[j + 1] = coe[j + 1] + (-2) * (sumit%2 * (-2) + 1) # The coefficitent for the (j + 1)th position
            coelist[i] = coe # The list of coefficitents
            
        # This section is to find the largest real roots for each Parry polynomial
        for i in range(len(coelist)):
            roots = np.roots(coelist[i]) # All the roots for coelist[i]
            real = []
            for j in roots: # Find the largest real root and add it to real[]
                if np.imag(j) == 0:
                    real.append(np.real(j))
            allbeta.append(max(real, default=0))
            betaorbit[n - 1] = allbeta 
        
    def histogram():
        fig = plt.figure()
        size, scale = 1000, 10
        commutes = pd.Series(list(allbeta))
        commutes.plot.hist(grid=False, bins=30, rwidth=0.9,
                           color='#607c8e')
        plt.title('Distribution of Superattracting Beta')
        plt.xlabel('I')
        plt.ylabel('number of Superatt. beta')
        plt.grid(axis='y', alpha=0.75)
        #plt.scatter(A,B,s=.01,marker='.')
        plt.show()  
        
    def distribution_orbit():
        A = []
        B = []
        for i in range(len(betaorbit)):
            for j in betaorbit[i]:
                A.append(j)
                B.append(i + 1)
                        
        plt.scatter(A,B,s=.5,marker='.') 
        plt.xlabel('Value of Superatt. Beta')
        plt.ylabel('orbit')
        plt.show()
        
    histogram()
    distribution_orbit()

supertt(22) # Input n




