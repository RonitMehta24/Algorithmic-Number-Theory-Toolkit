import matplotlib.pyplot as plt

def gcd(n, m):
    a, b = abs(n), abs(m)
    while b:
        a, b = b, a % b
    return a

def lcm(n,m):
    return int((n*m)/gcd(n,m))

#lengthens the given list so that it has at least n elements
def lengthen(lst, n):
    temp = lst[:]
    m = len(temp)
    if n <= m:
        return temp
    else:
        for i in range (n-m):
            temp.append(0)
        return temp

#Creates a partition of the interval [a,b] into n+1 pieces and returns the points of the partition as a list
def partition_x(a, b, n):
    delta_x = (b-a)/n
    x0 = a
    x_values = []
    for i in range(n+1):
        x_values.append(x0)
        x0 += delta_x
    return x_values


class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def show(self):
        if self.denominator == 1:
            print(f"{self.numerator}", end = " ")
        else:
            print(f"{self.numerator}/{self.denominator}", end=" ")

    #Reduces the given fraction so that the numerator and denominator are co-prime
    def reduce(self):
        a = self.numerator
        b = self.denominator
        if b<0:
            a = -a
            b = -b
        g = gcd(a, b)
        self.numerator = int(a/g)
        self.denominator = int(b/g)

    #Gives the decimal representation of the fraction as a float
    def decimal(self):
        return self.numerator/self.denominator

#Takes in two fractions and gives their sum. Works for integers as well but not for floats
def add_frac(frac1, frac2):
    
    if isinstance(frac1, fraction):
        a = frac1.numerator
        b = frac1.denominator
    else:
        a = frac1
        b = 1
    
    if isinstance(frac2, fraction):
        c = frac2.numerator
        d = frac2.denominator
    else:
        c = frac2
        d = 1
    
    frac = fraction(a*d+b*c, b*d)
    frac.reduce()
    return frac


#Takes in two fractions and gives their product. Works for integers as well but not for floats
def mul_frac(frac1, frac2):
    
    if isinstance(frac1, fraction):
        a = frac1.numerator
        b = frac1.denominator
    else:
        a = frac1
        b = 1
    
    if isinstance(frac2, fraction):
        c = frac2.numerator
        d = frac2.denominator
    else:
        c = frac2
        d = 1
        

    frac = fraction(a*c, b*d)
    frac.reduce()
    return frac

#Takes in two fractions and gives their difference. Works for integers as well but not for floats
def sub_frac(frac1, frac2):
    f2 = mul_frac(frac2, -1)
    return add_frac(frac1, f2)

#Tests if two fractions are equal
def equality(frac1, frac2):
    if frac1.numerator == frac2.numerator and frac1.denominator == frac2.denominator:
        return True
    else:
        return False

class polynomial:
    #Requires the coefficients be given as a list in increasing order of power of x 
    #for example [1, 0, 2, 5] corresponds to 1 + 2x^2 + 5x^3
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.degree = len(coefficients)-1

    def show(self):
        coeff = self.coefficients[0]
        if isinstance(coeff, fraction):
            coeff.show()
        else:
            print(coeff, end=" ")
        i = 1
        n = self.degree+1
        while i < n:
            coeff = self.coefficients[i]
            if isinstance(coeff, fraction):
                if coeff.numerator == 0:
                    i+=1
                    continue
                print(" + ", end="")
                coeff.show()
            else:
                if coeff == 0:
                    i+=1
                    continue
                print("+ ", end="")
                print(coeff, end=" ")
            print(f"x^{i}", end = "")
            i+=1
        print("")

    #Gives the value of the polynomial evaluated at x
    def value(self, x):
        s = 0
        for i in range(self.degree+1):
            coeff = self.coefficients[i]
            if isinstance(coeff, fraction):
                s =  s + coeff.decimal()*x**i
            else:
                s += coeff*x**i
        return s

    #Used for finding the y values when trying to plot the polynomial, which is returned as a list
    def plot_values(self, a, b, n):
        delta_x = (b-a)/n
        x0 = a
        y_values = []
        for i in range(n+1):
            y_values.append(self.value(x0))
            x0 += delta_x
        return y_values

    def scalar_mul(self, k):
        coefficients = self.coefficients
        new_coefficients = []
        for coeff in coefficients:
            new_coeff = mul_frac(coeff, k)
            new_coefficients.append(new_coeff)
        return polynomial(new_coefficients)



    def graph_and_show(self, a, b, n):
        x_values = partition_x(a, b, n)
        y_values = self.plot_values(a, b, n)
        plt.plot(x_values, y_values)
        plt.show()

    def graph(self, a, b, n, l="plot"):
        x_values = partition_x(a, b, n)
        y_values = self.plot_values(a, b, n)
        plt.plot(x_values, y_values, label=l)



def add_poly(poly1, poly2):
    f = poly1.coefficients[:]
    g = poly2.coefficients[:]
    m = poly1.degree - poly2.degree

    if m > 0:
        for i in range(m):
            f.append(0)
    else:
        for j in range(-m):
            g.append(0)
    h = []
    n = len(f)
    for k in range(n):
        h.append(add_frac(f[k], g[k]))
    return polynomial(h)

#Gives the product of two polynomials
def mul_poly(poly1, poly2):
    f = poly1.coefficients
    g = poly2.coefficients
    deg = poly1.degree + poly2.degree
    f = lengthen(f, deg+1)
    g = lengthen(g, deg+1)
    h = []
    for k in range(deg+1):
        c = 0
        for j in range(k+1):
            c = add_frac(c, mul_frac(f[j], g[k-j]))
        h.append(c)
    return polynomial(h)

#Gives the derivative of a polynomial
def diff_poly(poly):
    n = poly.degree
    dpoly = []
    for i in range(1, n+1):
        dpoly.append(mul_frac(i, poly.coefficients[i]))
    return polynomial(dpoly)

#Gives the antiderivative  of a polynomial with constant of integration C
def antiderivative(poly, C):
    n = poly.degree
    ipoly = [C]
    for i in range(n+1):
        ipoly.append(mul_frac(fraction(1, i+1), poly.coefficients[i]))
    return polynomial(ipoly)


