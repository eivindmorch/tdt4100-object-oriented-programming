def billettpris():
	alder = float (input ("Alder :"))
	if alder > 60 :
		print ("Gratis")
	elif alder >= 25 :
		print ("40kr")
	elif alder >= 21 :
		print ("30kr")
	elif alder >= 16 :
		print ("20kr")
	elif alder >= 5 :
		print ("10kr")
	else :
		print ("Gratis")

billettpris()