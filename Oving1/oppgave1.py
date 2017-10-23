import math
pi = 3.1415

print ("Fyll inn verdiene:")

#input
r = float(input("r:"))
o = float(input("Vinkel:"))

#calc
x = r * math.cos(o)
y = r * math.sin(o)


#print
if r == 3 and o == (pi/2) :
	print ("Svaret til oppgave 1.1 er:")
elif r == 2.3 and o == (pi/3) :
	print ("Svaret til oppgave 1.2 er:")
elif r == 5 and o == 0 :
	print ("Svaret til oppgave 1.3 er:")

print ("x:", x, "y:", y)
