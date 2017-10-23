from skumleskogen2 import *

unopened_doors = 0 # for å sjekke at det ikke er noe galt med labyrinten, ikke implementert.
node_stat = [0]*100 #finnes det bedre metode?
step_amm = 0
#1 = har gått/kan ikke venstre
#2 = har gått/kan ikke høyre
#3 = har vært/kan ikke begge

def new_movement(node):
	if node_stat[node] == 0:
		if gaa_venstre():
			node_stat[node] = 1
		elif gaa_hoyre() == 0:        #egentlig unødvendig 
			node_stat[node] = 2
			print("troll")
		else:
			node_stat[node] = 3
			gaa_tilbake()
	
	elif node_stat[node] == 1:
		if gaa_hoyre():
			node_stat[node] = 2
		else:
			node_stat[node] = 3
			gaa_tilbake()
	
	else:
		node_stat[node] = 3
		print("lol")
		gaa_tilbake()
	
	
while not (er_utgang()):
	n = nummer()
	
	if node_stat[n] == 3:
		while not (er_inngang()):
			gaa_tilbake()
		node_stat = [0]*100
		continue
	
	if (er_stank()):
		node_stat[n] = 3
		gaa_tilbake()
		continue
	
	if (er_nokkel()):
		plukk_opp()
		
	if (er_laas()):
		if not(laas_opp()):
			gaa_tilbake()
			unopened_doors += 1
			continue
	
	new_movement(n)
	step_amm += 1
	
gaa_ut()
print("Labyrinten ble fullført på", step_amm, "steg")