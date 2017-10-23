# a)
li = [1, 2, 3, 4, 5, 6]

# b) Spørre stud.ass om å bruke if i%2==0 og for i in li i stedenfor:
for i in range(len(li)):
	if i%2!=0:
		print (i)
		li[i] *= -1
	
print (li)

# c) d)
print (list(reversed (li)))