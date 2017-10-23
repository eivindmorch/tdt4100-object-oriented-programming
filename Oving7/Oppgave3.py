import math

def main ():
	perimeter ([1,1,2],[1,2,2])
	perimeter ([1, 1, 2, 2] , [1, 2, 2, 1])
	perimeter ([1, 2, 4, 5, 3], [2, 4, 5, 4, 1])
	
	
def perimeter (x, y):
	omkrets = 0
	for i in range(-1,len(x)-1):
		omkrets += math.sqrt( ( x[i] - x[i+1] )**2 + ( y[i] - y[i+1] )**2 ) 
	print (round(omkrets,4))
	

main ()