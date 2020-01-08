def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return fib_pair(n)[0]

def fib_pair(n):
    """Returns the tuple (F(n), F(n+1)).
    
    Arguments:
        n {int} -- n'th fibonacci number
    """
    if n == 0:
        return (0, 1)
    else:
        a, b = fib_pair(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)