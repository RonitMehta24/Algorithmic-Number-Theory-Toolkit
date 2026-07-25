from algebra import *
import matplotlib.pyplot as plt

mypolynomial = polynomial([4, 2, 8])
mypolynomial.show()
print(mypolynomial.value(1.5))
mypolynomial.graph_and_show(-1, 1, 100)