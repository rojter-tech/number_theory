#!/usr/local/bin/python3.8
from matplotlib import pyplot as plt
from utils.ntools import fib_pair

if __name__ == "__main__":
    fibratios = []
    for i in range(50):
        fibtuple = fib_pair(i+1)
        fibratios.append(fibtuple[1]/float(fibtuple[0]))
    
    print(fibratios)
    plt.plot(fibratios)
    plt.show()