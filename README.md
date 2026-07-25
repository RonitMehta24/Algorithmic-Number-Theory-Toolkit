# Algorithmic Number Theory Toolkit

A custom Python library built from scratch to handle symbolic algebra, polynomial operations, and the algorithmic generation of specific mathematical sequences. This project demonstrates the translation of pure mathematical logic into functional, object-oriented code, alongside empirical analysis of algorithmic complexity.

## Key Features

* **Symbolic Algebra:** Custom Object-Oriented implementations of mathematical fractions and polynomials, built without relying on external symbolic math libraries.


* **Bernoulli Polynomials:** Algorithmic generation and graphical visualization of Bernoulli polynomials using their recursive definition.


* **Farey Sequences:** Implementation of both a naive and an optimized algorithm for generating Farey sequences.


* **Complexity Analysis:** Empirical runtime analysis comparing the computational efficiency of the different Farey sequence generation methods, visualized with Matplotlib.



## Prerequisites & Installation

This project runs on standard Python. The only external dependency required for plotting and performance visualization is `matplotlib`.

You can install it via pip:

```bash
pip install matplotlib

```

## Usage & Examples

The foundational module, `algebra.py`, allows you to easily instantiate, evaluate, and visualize custom polynomials.

Below is a quick example demonstrating how to create a polynomial from a list of coefficients, evaluate it at a specific point, and generate a plot:

```python
from algebra import *
import matplotlib.pyplot as plt

# Instantiate the polynomial: 4 + 2x + 8x^2
mypolynomial = polynomial([4, 2, 8])

# Print the polynomial to the console
mypolynomial.show()

# Evaluate the polynomial at x = 1.5
print(mypolynomial.value(1.5))

# Graph the polynomial over the interval [-1, 1] with 100 partitions
mypolynomial.graph_and_show(-1, 1, 100)

```

To run the algorithmic generation scripts and view their outputs and performance graphs, simply execute them directly:

```bash
python bernoulli_2.py
python farey_2.py

```



## Mathematical Context

### Bernoulli Polynomials

Bernoulli polynomials, denoted as $B_k(x)$, are generated utilizing Bernoulli numbers, $B_k$.This toolkit first calculates the required Bernoulli numbers using the implicit recursive formula:  $$B_k = -\frac{1}{k+1} \sum_{j=0}^{k-1} \binom{k+1}{j} B_j$$
with the base case $B_0 = 1$.  

It then leverages the recursive calculus definition of Bernoulli polynomials to inductively find and plot the first $n$ polynomials using the relation: 
$$B_k(x) = k \int B_{k-1}(x) \, dx + B_k$$
This is achieved programmatically by scaling the previous polynomial by $k$ and computing its antiderivative, with the corresponding $k$-th Bernoulli number acting as the constant of integration.  

### Farey Sequences

The Farey sequence of order $n$, denoted as $F_n$, is the sequence of completely reduced fractions between $0$ and $1$ which, when in lowest terms, have denominators less than or equal to $n$.

Generating these sequences efficiently requires careful algorithmic design. This toolkit implements two different generation methods:

1. A **naive algorithm** that iteratively calculates and inserts intermediate fractions using Farey addition, which adds two fractions $\frac{a}{b}$ and $\frac{c}{d}$ as $\frac{a+b}{c+d}$(The way most people think addition of fractions works at first). 


2. An **optimized algorithm** that directly computes successive terms, significantly reducing computational overhead. For more information on how this is implemented check out the wikipedia page mentioned below.

## References

For more detailed information regarding the mathematical foundations of the concepts implemented in this toolkit, please refer to the following:

* **Bernoulli Polynomials:** *Montgomery, & Vaughan, Multiplicative Number Theory Part 1*, Appendix B (provides comprehensive theoretical background on Bernoulli polynomials).
* **Farey Sequences:** [Farey sequence - Wikipedia](https://en.wikipedia.org/wiki/Farey_sequence)




