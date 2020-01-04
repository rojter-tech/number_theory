#!/usr/local/bin/python3.8

from matplotlib import pyplot as plt

def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]

# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    """Returns the tuple (F(n), F(n+1)).
    
    Arguments:
        n {int} -- n'th fibonacci number
    """
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

if __name__ == "__main__":
    fibratios = []
    for i in range(50):
        fibtuple = _fib(i+1)
        fibratios.append(fibtuple[1]/float(fibtuple[0]))
    
    print(fibratios)
    plt.plot(fibratios)
    plt.show()