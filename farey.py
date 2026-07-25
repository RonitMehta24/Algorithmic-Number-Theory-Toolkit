import time
import matplotlib.pyplot as plt
from algebra import *

def farey_add(frac1, frac2):
    frac = fraction(frac1.numerator + frac2.numerator, frac1.denominator + frac2.denominator)
    frac.reduce()
    return frac

def farey(n):
    list = [fraction(0, 1), fraction(1, 1)]
    i = 2
    while i<= n:
        j = 0
        while j < len(list)-1:
            new_frac = farey_add(list[j], list[j+1])
            if new_frac.denominator<=n:
                list.insert(j+1, farey_add(list[j], list[j+1]))
                j+=1
            else:
                j += 2
        i += 1
    return list

def alt_farey(n):
    list = [fraction(0, 1), fraction(1, n)]
    while True:
        l = len(list)
        frac1 = list[l-2]
        frac2 = list[l-1]
        a = frac1.numerator
        b = frac1.denominator
        c = frac2.numerator
        d = frac2.denominator
        k = (n+b)//d
        new_frac = fraction(k*c-a, k*d-b)
        list.append(new_frac)
        if new_frac.denominator == 1:
            break
    return list


input_sizes1 = [i for i in range(1, 50)]
input_sizes2 = [i for i in range(1, 100)]
runtimes1 = []
runtimes2 = []
for size in input_sizes1:
    
    start_time = time.perf_counter()
    farey(size)
    end_time = time.perf_counter()
    elapsed_time = end_time-start_time
    runtimes1.append(elapsed_time)

for sizes in input_sizes2:

    start_time = time.perf_counter()
    alt_farey(sizes)
    end_time = time.perf_counter()   
    elapsed_time = end_time-start_time   
    runtimes2.append(elapsed_time)

plt.figure(figsize=(10, 6))
plt.plot(input_sizes1, runtimes1, marker='o', linestyle='-', color='b', label = "naive algorithm")
plt.plot(input_sizes2, runtimes2, marker='o', linestyle='-', color='r', label = "optimized algorithm")
plt.legend()

# Labeling the axes
plt.xlabel('Input Size (N)')
plt.ylabel('Runtime (Seconds)')
plt.title('Empirical Runtime of generation of farey sequence')

plt.show()

flist = alt_farey(8)
for f in flist:
    f.show()
    print("")