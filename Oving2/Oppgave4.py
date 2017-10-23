def beregn_celsius ():
	fahrenheit = float(input("Fahrenheit: "))
	print (fahrenheit, "fahrenheit" , "=", format( 5*(fahrenheit-32)/9 , ".1f") , "celcius")
	
beregn_celsius()
