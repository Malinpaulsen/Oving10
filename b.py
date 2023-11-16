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
    

#Fra oppgave d i øving 4
def funksjon_flyttall_enkelverdi(liste, verdi):
    funksjon_flyttall_enkelverdi = 0
    
    for element in liste: 
        if element >= verdi:
            funksjon_flyttall_enkelverdi += 1
    
    return funksjon_flyttall_enkelverdi

def antall_skiforedager(værdata):
    skiforedager_per_sesong = {}

    for år in værdata:
        snoedybder = værdata[år]["snoedybder"]
        skiføre_dager = funksjon_flyttall_enkelverdi(snoedybder, 20)  # Bruk funksjonen for å telle skiføre dager

        vinterår = år if år < 6 else år + 1  # Vintersesongen går fra oktober til juni
        if vinterår not in skiforedager_per_sesong:
            skiforedager_per_sesong[vinterår] = skiføre_dager
        else:
            skiforedager_per_sesong[vinterår] += skiføre_dager

    return skiforedager_per_sesong


# Du kan nå kalle funksjonen les_værdata for å hente værdataene
værdata = les_værdata(filnavn)

# Bruk funksjonen antall_skiforedager for å få antall skiføredager per vintersesong
skiføre_resultat = antall_skiforedager(værdata)

# Skriv ut resultatene eller bruk dem som nødvendig
print(skiføre_resultat)
