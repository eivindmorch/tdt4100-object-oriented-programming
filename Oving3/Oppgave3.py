import math

r = float (input ("Radius: "))

def sirkel (r):
	areal = format( math.pi * r**2 , ".2f")
	omkrets = format ( math.pi * 2 * r , ".2f")
	print ("Areal:", areal)
	print ("Omkrets:", omkrets)
	
sirkel(r)