from multiprocessing import Pool
import itertools
import os, json


def shift(x):
    d = x[1] - x[0]
    for i in range(len(x) - 1):
        x[i] = x[i + 1] - d
    x[len(x) - 1] = n - d
    return x


def admissible(x):
    x0 = [i for i in x]
    i = 0
    while i < len(x) - 1:
        shift(x)
        for j in range(len(x)):
            if x0[j] * (-1) ** j > x[j] * ((-1) ** j):
                return False
            if x0[j] == x[j]:
                if j == len(x) - 1:  # Rule out the repetition
                    return False
            else:
                break
        i = i + 1
    return True


def itinerary(l):
    fileCnt=0   
    it_j = []
    num = [i for i in range(2, n)]
    it = list(itertools.combinations(num, l - 1))
    it = [list(i) for i in it]
    for i in range(len(it)):
        it[i] = list(it[i])
        it[i].insert(0, 0)
        z = [i for i in it[i]]
        if admissible(it[i]) == True:
            path='itinResults1/'+str(n)+'/' +str(l) + '_' + str(fileCnt) +'.txt'
            with open(path,'a') as file:
                file.write(str(z) + '\n')
            if os.path.getsize(path)>200000000:
                fileCnt+=1
    return 


m = 150
allIt = []

for n in range(35, m + 1):
    os.mkdir('itinResults1/'+str(n)+'/')
    it_n = []
    even = [i for i in range(2, n) if i % 2 == 0]
    # pool = Pool()
    # result = pool.map(itinerary, even)
    # pool.close()
    for x in even:
        itinerary(x)


