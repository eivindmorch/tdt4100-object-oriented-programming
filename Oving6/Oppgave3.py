import math

def main ():
	print ("Fyll inn verdiene for vektoren:")
	vec1 = vector_retrieve ()
	vector_print(vec1)
	vektorlengde1 = float(vector_length(vec1))
	print ("Vektorlengde: ", format(vektorlengde1, ".2f"))
	a = float (input ("Skalar: "))
	vec1 = vector_scalar(vec1, a)
	print ("Skalarmultiplisert vektor: ", vec1)
	vektorlengde2 = float(vector_length(vec1))
	print ("Ny vektorlengde: ", format(vektorlengde2, ".2f"))
	print ("Forhold mellom vektorlengder: ", vektorlengde2 / vektorlengde1)
	print ("Vektor nr 2:")
	vec2 = vector_retrieve()
	print ("Skalarprodukt: ", vector_product (vec1, vec2))
	
# a)
def vector_retrieve ():
	x, y, z = int(input("x: ")), int(input("y: ")), int(input("z: "))
	return [x, y, z]

# b) vakker måte? matematisk eller f.eks. x:, y:, z:????
def vector_print(vector):
	print ("Vektor: ", vector)
	
# c)
def vector_scalar (vector, a):
	new_vector= [i*a for i in vector]
	return new_vector

# d) Kan man ikke bare legge inn at forholdet mellom lengder = skalar?
def vector_length (vector):
	vector = [i*i for i in vector]
	total = 0
	for i in vector:
		total += i
	return math.sqrt(total)

# e) 
def vector_product (vector1, vector2):
	product = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
	return product

main()