import math
num = int(input("Skriv inn tall: "))
prime_list = []

for i in range(2, int(math.sqrt(num)+1)):
	if num%i == 0:
		prime_list.append(i)
		num = num/i

print (prime_list, "Den største primfaktoren er:", max(prime_list))