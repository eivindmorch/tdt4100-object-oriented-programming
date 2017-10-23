import time
start_time = time.clock()
stat = False
i = 2520
while not stat :
	stat_count = 0
	for num in range(1, 21):
		if i%num==0:
			stat_count +=1
		else:
			statcount = 0
			break
	i += 2520
	if stat_count == 20:
		print ("TADAAAAA", i)
		stat = True

print (time.clock() - start_time)