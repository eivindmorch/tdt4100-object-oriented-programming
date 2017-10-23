n = float (input ("Heltall: "))
num = 0
sum = 0

if sum > n or n%1 != 0:
	print ("Tallet du skrev inn er ikke et heltall")

else:	
	while n >= sum:
		num += 1
		sum += (num)**2
	
		if sum > n:
			sum -= (num)**2
			num -= 1
			print ("Summen: " , sum, "Antall elementer: ", num)
			break
		
