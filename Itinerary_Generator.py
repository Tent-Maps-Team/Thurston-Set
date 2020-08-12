import itertools
import csv


# Shift the itenarary string
def shift(x, n):
    d = x[1] - x[0]
    for i in range(len(x) - 1):
        x[i] = x[i + 1] - d
    x[len(x) - 1] = n - d
    return x


# Test admissibility
def admissible(x, n):
    x0 = [i for i in x]
    i = 0
    while i < len(x) - 1:
        shift(x, n)
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


def supertt(m):
    all_beta = [[] for i in range(m)]
    all_it = [[] for i in range(m)]
    all_beta_conjugate = [[] for i in range(m)]
    all_beta_conjugate_D = [[] for i in range(m)]
    for n in range(3, m + 1):

        # Generate strings for Itenarary which sum of digits are even
        it_n = []
        even = [i for i in range(2, n) if i % 2 == 0]
        for l in even:
            num = [i for i in range(2, n)]
            it = list(itertools.combinations(num, l - 1))
            it = [list(i) for i in it]
            for i in range(len(it)):
                it[i] = list(it[i])
                it[i].insert(0, 0)
                z = [i for i in it[i]]
                if admissible(it[i], n) == True:
                    it[i] = z
                    it_n.append(it[i])
            all_it[n - 1] = it_n

        # Find coefficients for Parry polynomials
        coelist_n = [[] for i in range(len(it_n))]
        for i in range(len(coelist_n)):
            coe = [0 for i in range(n + 1)]
            coe[0] = 1
            coe[n] = -1
            for j in it_n[i]:
                sumit = it_n[i].index(j)
                coe[j + 1] = coe[j + 1] + (-2) * (sumit % 2 * (-2) + 1)
            coelist_n[i] = coe

            # write the Itinerary_String
    with open('01_Itinerary_String.txt', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['n', 'Itinerary_String'])
        for i in range(len(all_it)):
            for j in all_it[i]:
                thewriter.writerow([i + 1, j])


supertt(22)
