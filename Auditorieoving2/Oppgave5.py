lengder = [3, 24, 5, 10, 6, 31, 12, 7, 8, 21]
fartsgrenser = [60, 80, 60, 80, 90, 70, 60, 30, 50, 60]
veistrekning = [lengder, fartsgrenser]

lengder2 = [17, 24, 5, 10, 6, 31, 12, 7, 8, 21]
fartsgrenser2 = [80, 80, 40, 50, 120, 60, 60, 30, 50, 30]
veistrekning2 = [lengder2, fartsgrenser2]

# a)
def is_valid (path):
	for i in path:
		for ele in i:
			if ele <= 0 :
				return False
	else:
		return True
	
print (is_valid ([[103, 45, 10, 24], [30, 60, 80, 90]]))
print (is_valid ([[5, 11, 45, -13], [30, 0, 80, 90]]))

# b)
def drive_item (path):
	time = 0
	distance = path[0]
	speedlimit = path[1]
	for i in range (len(path[1])):
		time += distance[i]/speedlimit[i]
	return time
	
print (drive_item(veistrekning))

# c)
def shortest_valid(p1, p2):
	if is_valid(p1) == False or is_valid(p2) == False:
		return False
	time_p1 = drive_item(p1)
	time_p2 = drive_item(p2)
	if time_p1 > time_p2:
		return ("p2: ", time_p2)
	elif time_p1 == time_p2:
		return "De tar like lang tid"
	else:
		return ("p1: ", time_p1)
		
print (shortest_valid(veistrekning, veistrekning2))