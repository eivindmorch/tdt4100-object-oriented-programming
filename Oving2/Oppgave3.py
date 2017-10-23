def main ():
	print ("Fyll inn:")
	bilnavn = input("Bilnavn: ")
	bruttop =  int ( input ("Bruttopris i kr: ") )
	vekt =  int ( input ("Vekt i kg: ") )
	hk =  int ( input ("Hestekrefter: ") )
	co2 =  int ( input ("Co2-utslipp i gram: ") )
	mvolum =  int ( input ("Motorvolum i liter: ") )
	beregn_avgift(bilnavn, bruttop, vekt, hk, co2, mvolum)
	
def beregn_avgift(bilnavn, bruttop, vekt, hk, co2, mvolum):
	nettop = (bruttop * vekt * 0.00034 + bruttop * hk * 0.00015 + bruttop * co2 * 0.004 + bruttop * mvolum * 0.00055)
	print("Nettoprisen på", bilnavn, "er:", nettop)	

main()

#Finn utsalgspris for følgende bilmodeller:
#Ford Mondeo 1.8: Motorvolum: 1800 l, Vekt: 1680 kg, Hestekrefter: 125 hk, Co2: 125g, Bruttopris: 120000 kr
#Ford Mondeo 1.0: Motorvolum: 1000 l, Vekt: 1780 kg, Hestekrefter: 125 hk, Co2: 114g, Bruttopris: 130000 kr
#BMV M5 3.0: Motorvolum: 3000 l, Vekt: 1980 kg, Hestekrefter: 350 hk, Co2: 150 g, Bruttopris: 260000 kr
#BMV M5 1.3: Motorvulum: 1300 l, Vekt: 1980 kg, Hestekrefter: 350 hk, Co2: 125 g, Bruttopris: 270000 kr