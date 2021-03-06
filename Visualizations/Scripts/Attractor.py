import itertools
import matplotlib.pyplot as plt

def generator(s,i,n,union_all_small_s):
    small_s = []
    all_small_s = []
    potential_ones = [i for i in range(i + 1,n)]
    for j in range(n - i):
        new_s = itertools.combinations(potential_ones, j)
        small_s = [s+list(i) for i in new_s]
        all_small_s = all_small_s + small_s
    return all_small_s

def attractor(s,n,c,z):
    union_all_small_s = []

    for i in range(n):
        if (i in s) and (s.index(i)%2 == 0):
            s2 = s[:(s.index(i))]
            union_all_small_s = union_all_small_s + generator(s2,i,n,union_all_small_s)
        elif ((i in s) == 0) and sum(j < i for j in s)%2 ==1:
            s2 = s[:sum(j < i for j in s)]+[i]      
            union_all_small_s = union_all_small_s + generator(s2,i,n,union_all_small_s)

    real = []
    imag = []

    for i in range(len(union_all_small_s)):
        for j in range(n):
            if j in union_all_small_s[i]:
                z = c * z
            else:
                z = 2 - c * z
        real.append(z.real)
        imag.append(z.imag)
    
    plt.scatter(real,imag,s=.1,marker='.') 
    plt.show()
    
s = [int(i) for i in input('Please input the string for sup.att. beta s, seperate with space:').split()]
n = int(input('Please input n:'))
c = [float(i) for i in input('Please input complex number c:').split()]
c = complex(c[0], c[1])
z = 0

attractor(s,n,c,z)