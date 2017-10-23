debug = True

x = int (input ("x: "))
y = int (input ("y: "))

def add (x,y):
	if debug :
		print ("Tallene som summeres er", x , "og", y)
	print (x + y)
	
add(x,y)


