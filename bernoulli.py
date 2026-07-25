import time
import matplotlib.pyplot as plt
from algebra import *

#Program for printing the first n bernoulli polynomials

def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def choose(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))



n = 5
Bernoulli_number = [fraction(1,1)]
k = 1

#First we calculate the required Bernoulli numbers 
#that will be the constant terms in the corresponding Bernoulli polynomials
while k < n+1:
    B = 0 
    for j in range(k):
        B = add_frac(B, mul_frac(choose(k+1, k+1-j), Bernoulli_number[j]))
    B = mul_frac(fraction(-1, k+1), B)
    Bernoulli_number.append(B)
    k+=1


B = polynomial([1])
k = 1
B.graph(0, 1, 100, "B0(x)")
B.show()
print("")
#Now using the definition of Bernoulli Polynomials we inductively find the first n of them and print them
while k < n+1:
    B = B.scalar_mul(k)
    B = antiderivative(B, Bernoulli_number[k])
    B.graph(0, 1, 100, "B"+str(k)+"(x)")
    B.show()
    print("")

    k+=1
plt.legend()
plt.show()




