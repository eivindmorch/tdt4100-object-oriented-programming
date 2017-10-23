import random

def main():
	print("Massemidtpunkt: ",mass_center(random_list(120)))

# a)
def mass_center(pole):
	half_mass = sum(pole)/2
	x = 0
	for i in range (len(pole)):
		if x >= half_mass:
			return i
			break
		x += pole[i]
		

# b)		
def random_list(length):
	list = []
	for i in range (length):
		list.append(random.randint(1,101))
	print (list)
	return list
	
	
	
main()