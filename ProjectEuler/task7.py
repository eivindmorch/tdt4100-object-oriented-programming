import math
import time
start_time = time.clock()
prime_num = 1
check_num = 3
prime10001 = False
check = False

while prime10001 == False:
	for i in range (2, math.floor(math.sqrt(check_num))):
		if check_num%i==0:
			print (check_num, "Ikke primtall")
			check = False
			break
		else:
			check = True
	print(check_num, prime_num)
	if check == True:
		prime_num += 1
	
	if prime_num == 10001:
		print("Primtall 10001:", check_num)
		prime10001 = True
		break
	
	check_num += 2
print ( time.clock() - start_time)