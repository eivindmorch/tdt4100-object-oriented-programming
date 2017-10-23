import math
import time
start_time = time.clock()
n=500

for a in range (1, n):
	for b in range (a+1, n):
		if a+b+ math.sqrt((a**2+b**2)) == 1000:
			print(a, b, math.sqrt((a**2+b**2)), a * b * math.sqrt((a**2+b**2)))
			break
			
print ( time.clock() - start_time)