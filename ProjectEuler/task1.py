num = int(input("Skriv inn tall: "))
sum = 0

for i in range(1,num):
	if (i%3==0) or (i%5==0):
		sum += i
		print (i)
print (sum)