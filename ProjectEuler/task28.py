import time
start_time = time.clock()

def spiral_sum(n):
	avstand = 2
	sum = 1
	cur_num = 1
	while avstand < n:
		sum += 4 * cur_num + avstand*10
		cur_num += 4*avstand
		avstand += 2
	return sum

print ("Answer: ", spiral_sum(1000), "\n" "Runtime: ", format(time.clock() - start_time,".10f"))
