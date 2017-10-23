teeth = [95 , 103 , 71 , 99 , 114 , 64 , 95 , 53 , 97 , 114 , 109 , 11 , 2, 21 , 45 , 2, 26 , 81 , 54 , 14 , 118 , 108 , 117 , 27 , 115 , 43 , 70 , 58 , 107]

total_kroner20 = 0
total_kroner10 = 0
total_kroner5 = 0
total_kroner1 = 0
total_ore50 = 0

for i in teeth:
	kroner20 = 0
	kroner10 = 0
	kroner5 = 0
	kroner1 = 0
	ore50 = 0
	while i >= 40:
		kroner20 += 1
		total_kroner20 += 1
		i -= 40
	
	while i >= 20:
		kroner10 += 1
		total_kroner10 += 1
		i -= 20
		
	while i >= 10:
		kroner5 += 1
		total_kroner5 += 1
		i -= 10
		
	while i >= 2:
		kroner1 += 1
		total_kroner1 += 1
		i -= 2
		
	while i >= 1:
		ore50 += 1
		total_ore50 += 1
		i -= 1
	print (kroner20, kroner10, kroner5, kroner1, ore50)
	
print ("Total:", "\n",total_kroner20, total_kroner10, total_kroner5, total_kroner1, total_ore50)	
