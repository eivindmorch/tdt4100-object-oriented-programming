import sys
import time
antall_kvinner = 0
antall_menn = 0
antall_sosmedier = 0
antall_facebook = 0
antall_timer_sosmedier = 0
a = 1

def main():
    while a == 1 :
        hent_kjonn_alder()
        hent_tid()
    
def hent_kjonn_alder():
    global antall_kvinner
    global antall_menn
    print('Undersøkelse')
    kjonn = input('Kjønn (m/k): ')
    check_break(kjonn)
    alder = input('Alder: ')
    check_break(alder)        
    
    alder = int(alder)
    check_alder(alder)
    if kjonn == 'm':
        antall_menn += 1
    else:
        antall_kvinner += 1
    get_aktiv(kjonn)
        
def check_break(svar):
    if svar == 'hade':
        print(antall_kvinner, antall_menn, antall_sosmedier, antall_facebook, antall_timer_sosmedier)
        time.sleep(3)
        exit()
        

def check_alder(age):
    if age < 16 or age > 25:
        print ('denne undersøkelsen gjelder for personer i aldergruppen 16-25 år.')
        get_kjonn_alder()

def face(svar):
    global antall_facebook
    if svar == 'ja':
        antall_facebook += 1
                     
def get_aktiv(k):
    aktiv_sosmedier = input('benytter du deg av ett eller flere sosiale medier? (ja/nei): ')
    check_break(aktiv_sosmedier)
    get_facebook(aktiv_sosmedier, k)

def get_facebook(aktiv, kjonn):
    global antall_sosmedier
    if aktiv == 'ja' and kjonn == 'k':
        antall_sosmedier += 1
        medlem_facebook = input('mellom 55-60% av facebook sine brukere er kvinner. er du en av disse? (ja/nei): ')
        check_break(medlem_facebook)
        face(medlem_facebook)
    elif aktiv == 'ja' and kjonn == 'm':
        antall_sosmedier += 1
        medlem_facebook = input('mellom 40-45% av facebook sine brukere er menn. er du en av disse? (ja/nei): ')
        check_break(medlem_facebook)
        face(medlem_facebook)
    else:
        get_kjonn_alder()            
            
def get_timer():
    global antall_timer_sosmedier
    timer_sosmedier = input('hvor mange timer bruker du i snitt daglig på sosiale medier? ')
    check_break(timer_sosmedier)
    timer_sosmedier = int(timer_sosmedier)
    antall_timer_sosmedier += timer_sosmedier

main()