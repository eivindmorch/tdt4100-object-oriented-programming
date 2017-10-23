import math
import time
start_time = time.clock()
prime_sum = 2
check_num = 3
check = False

while check_num < 2000000:
	for i in range (2, math.floor(math.sqrt(check_num))):
		if check_num%i==0:
			print (check_num, "Ikke primtall")
			check = False
			break
		else:
			check = True
	print(check_num, prime_sum)
	if check == True:
		prime_sum += check_num
	
	check_num += 2

print (prime_sum, time.clock() - start_time)