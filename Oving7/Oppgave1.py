import math

# a)
def polynom (x):
	f = x**5 - 4*(x**3) - 10*(x**2)-10
	return f

def polynom_derivative (x):
	d = 5*(x**4) - 12*(x**2) + 20*x
	return d
	
# b)
def newton (func, deriv, start, threshold, max_iterations):
	
	