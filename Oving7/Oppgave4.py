
def main():
	print("2", is_prime(2))
	print("11", is_prime(11))
	print("168", is_prime(168))
	separate([122,44,623,634,56,1],240)
	multiplication_table(3)
	multiplication_table(10)

# a) forsøkte å bruke if a < 2, elif a>2 med for loop, og else: true, men fikk en del rare feilmeldinger
def is_prime(a):
	if a == 2:
		primtall = True
	else:
		primtall = False
		for i in range (2,a):
			if a%i == 0:
				primtall = False
				break
			else:
				primtall = True
	return primtall
	
	
	
# b)
def separate (numbers, threshold):
	numbers_lower = []
	numbers_higher = []
	for i in numbers:
		if i < threshold:
			numbers_lower.append(i)
		else:
			numbers_higher.append(i)
	print (" Elementer under: ",numbers_lower, "\n","Elementer over: ", numbers_higher)
		

# c)
def multiplication_table(n):
	matrix = [[0 for row in range (n)] for column in range (n)]
	for i in range (n):
		for x in range (n):
			matrix[i][x] = format((i+1)*(x+1), "2.0f")
	print("Gangetabell for", n, ":")
	for row in matrix:
		print (row)
	
	
	
main()