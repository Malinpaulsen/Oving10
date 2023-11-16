import matplotlib.pyplot as plt

from datetime import datetime
import matplotlib.pyplot as plt

def sett_inn_konponent_hvis_gyldig(liste, komponent): 
    try: 
        komponent = komponent.replace(",",".")
        tall = float(komponent)
        liste.append(tall)
    except ValueError: 
            pass 



def initialiser__aar(dictionary, aar): 
    dictionary[aar] = dict()
    dictionary[aar]["snoedybder"] = list()
    dictionary[aar]["nedbor_dogn"] = list()
    dictionary[aar]["temperatur"] = list()
    dictionary[aar]["skydekke"] = list()
    dictionary[aar]["max_vind"] = list()
  
    
  # delopg a 
    
filnavn = 'snoedybder_vaer_en_stasjon_dogn.csv'    
def les_værdata(filnavn):
    værdata = [] 
    with open(filnavn, 'r', encoding='utf-8') as fil:
        fil.readline()
        værdata = dict()
        aar = 0 
        for linje in fil:
            komponenter = linje.split(";")
          
            dato = komponenter[2]
            dato_komponenter = dato.split(".")
            try:
                aar = int(dato_komponenter[2])
                maaned = int(dato_komponenter[1])
                snoedybder_aar = aar 
                if maaned < 6: 
                    snoedybder_aar -= 1
            except ValueError:
                    continue
            except IndexError: 
                    continue
          
            if aar not in værdata:
                initialiser__aar(værdata, aar)
            if snoedybder_aar not in værdata:
                initialiser__aar(værdata, snoedybder_aar)
            sett_inn_konponent_hvis_gyldig(værdata[snoedybder_aar]["snoedybder"], komponenter[3])
            sett_inn_konponent_hvis_gyldig(værdata[aar]["nedbor_dogn"], komponenter[4])
            sett_inn_konponent_hvis_gyldig(værdata[aar]["temperatur"], komponenter[5])
            sett_inn_konponent_hvis_gyldig(værdata[aar]["skydekke"], komponenter[6])
            sett_inn_konponent_hvis_gyldig(værdata[aar]["max_vind"], komponenter[7])
        return værdata

vær_info = les_værdata(filnavn)
print(vær_info[2001],'snødybde')

#Oppgave f fra del 1
# Funksjon for å finne den lengste sekvensen av nuller (tørkeperiode)
def finn_lengste_null_sekvens(liste):
    # Initialiser variabler for den gjeldende sekvensen og den lengste sekvensen
    gjeldende_sekvens = 0
    lengste_sekvens = 0
    
    for num in liste:
        if num == 0:
            # Hvis tallet er null, øk lengden på den gjeldende sekvensen
            gjeldende_sekvens += 1
        else:
            # Hvis tallet ikke er null, tilbakestill den gjeldende sekvensen
            gjeldende_sekvens = 0
        
        # Oppdater den lengste sekvensen hvis den gjeldende sekvensen er lengre
        if gjeldende_sekvens > lengste_sekvens:
            lengste_sekvens = gjeldende_sekvens
    
    return lengste_sekvens

# Funksjon for å finne den lengste tørkeperioden for hvert år
def finn_lengste_tork_per_aar(værdata):
    tørke_per_aar = {}

    for år, data in værdata.items():
        # Sjekk om det er nok data for året (minst 300 dager)
        if len(data["nedbor_dogn"]) >= 300:
            # Finn den lengste tørkeperioden for dette året
            lengste_tørke = finn_lengste_null_sekvens(data["nedbor_dogn"])
            tørke_per_aar[år] = lengste_tørke

    return tørke_per_aar

# Hent værdataene
vær_info = les_værdata(filnavn)

# Finn den lengste tørkeperioden for hvert gyldige år
tørke_per_aar = finn_lengste_tork_per_aar(vær_info)

# Plot resultatene
plt.figure(figsize=(10, 6))
plt.bar(tørke_per_aar.keys(), tørke_per_aar.values(), color='skyblue')
plt.xlabel('År')
plt.ylabel('Lengste tørkeperiode (dager uten nedbør)')
plt.title('Lengste tørkeperiode per år')
plt.grid(axis='y')
plt.show()