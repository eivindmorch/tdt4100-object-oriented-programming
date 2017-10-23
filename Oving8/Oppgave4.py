def main():
	print("Antall linjer: ", number_of_lines("nummer.txt"))
	print(number_frequency("nummer.txt"))
	# c)	
	dict_numbers = number_frequency("nummer.txt")
	for ele in dict_numbers:
		print (ele, ":", dict_numbers[ele])
	
# a)
def number_of_lines(filename):
	infile = open(filename,"r")
	num_lines = 0
	for line in infile:
		num_lines += 1
	infile.close()
	return num_lines
	
	
		
# b)
#def number_frequency(filename):
#	infile = open(filename,"r")
#	file_string = []
#	for line in infile:
#		file_string.append(int(line))
#	
#	num_dict = {}
#	
#	for i in range(len(file_string)):
#		num_dict[file_string[i]] = 1
#	
#	return num_dict
	
def number_frequency (filename):
	infile = open(filename,"r")
	file_string = []
	for line in infile:
		file_string.append(int(line))
	infile.close()
	return dict([(x, file_string.count(x)) for x in list(file_string)])






	
main()