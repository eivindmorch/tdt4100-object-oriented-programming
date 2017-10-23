def main ():
	print(check_string ("haha", "haha"))
	print(check_string ("detteblirrart", "hei"))
	print("Reverse av Heipådeg: ",string_reverse ("Heipådeg"))
	print("Palindrom(abba): ",check_palindrom("abba"))
	print("Palindrom(reler): ",check_palindrom("reler"))
	print("Palindrom(funkerikke): ",check_palindrom("funkerikke"))
	print("Stringcontain(Vi kjørte av gårde, kjør): ",string_contain("Vi kjørte av gårde", "kjør"))
	print("Stringcontain(Drama, xyz): ",string_contain("Drama", "xyz"))
	
# a)
def check_string (string1, string2):
	if len(string1) == len(string2):
		for i in range (0, len(string1)):
			if string1[i] != string2[i]:
				return False
		return True
	else:
		return("Lengden på strengene er ikke like")
		


# b)
def string_reverse (string):
	reverse_string = ""
	for i in range (1,len(string)+1):
		reverse_string += string[-i]
	return reverse_string
	
# c)
def check_palindrom(string):
	return(check_string(string,string[::-1]))
	
# d)
def string_contain(string1, string2):
	if string2 in string1:
		for i in range (1,len(string1)):
			if string2 not in string1[i:]:
				return (i-1)
				break
	else:
		return False


	
main()