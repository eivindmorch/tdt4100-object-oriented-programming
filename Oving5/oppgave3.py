def gcd (a,b):
	while b!=0:
		gammel_b = b
		b = a%b
		a = gammel_b
	return a
	
def reduce_fraction ():
	a = input ("a: ")
	b = input ("b: ")
	gcd (a,b)
	return a, b
	
reduce_fraction()