a = int (input ("a: "))
b = int (input ("b: "))
c = int (input ("c: "))

d = b**2 - 4 * a * c

if d < 0:
	print ("Det er to imaginære løsninger")
elif d > 0:
	print ("Det er to reelle lønger")
else:
	print ("Det er én reell løsning")