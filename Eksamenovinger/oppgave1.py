# C:\Users\Eivind\Dropbox\EivindDropbox\Python\Eksamenovinger
import time
start_time = time.clock()
avstand = 2
sum = 1
counter = 0
cur_num = 1
while avstand < 1002:
	sum += 4 * cur_num + avstand*10
	cur_num += 4*avstand
	avstand += 2
print("Runtime: ",time.clock() - start_time,"Answer :",sum)
