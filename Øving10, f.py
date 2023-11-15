#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:13:33 2023

@author: chantelhelleland
"""

#Oppgave f
"""
Bruk funksjonen fra del 1 oppgave f) til å finne den lengste perioden med tørke (ingen
nedbør) for hvert år i datasettet. Plott resultatet. Inkluder bare år hvor det er nedbørsdata
for mesteparten av året, det må være data for minst 300 dager for at et år skal være gyldig
bilde
"""

filnavn = 'snoedybder_vaer_en_stasjon_dogn.csv'

def les_værdata(filnavn):
    værdata = []
    
    with open(filnavn, 'r', encoding='UTF-8') as fil:
        linjer = fil.readline()
        værdata = dict()
        aar = 0
        for linje in linjer:
            komponenter = linje.split(";")
            if len(komponenter) < 8:
                continue
            værdata_navn = komponenter[0]
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
                if værdata_navn not in værdata:
                    værdata[værdata_navn] = dict()
                if aar not in værdata[værdata_navn]:
                    initialiser_aar(værdata[værdata_navn], aar)
                if snoedybder_aar not in værdata[værdata_navn]:
                    initialiser_aar(værdata[værdata_navn], aar)
                sett_inn_komponent_hvis_gyldig(værdata[værdata_navn][snoedybder_aar]["snoedybder"], komponenter[3])
                sett_inn_komponent_hvis_gyldig(værdata[værdata_navn][aar]["nedbør_døgn"], komponenter[4])
                sett_inn_komponent_hvis_gyldig(værdata[værdata_navn][aar]["temperatur"], komponenter[5])
                sett_inn_komponent_hvis_gyldig(værdata[værdata_navn][aar]["skydekke"], komponenter[6])
                sett_inn_komponent_hvis_gyldig(værdata[værdata_navn][aar]["max_vind"], komponenter[7])
                
                return værdata

def lengste_tørkeperiode(værdata):
    gyldige_år = set() #mengde for å lagre unike år
    resultat = [] #tom liste for å lagre resultat
    
    for data in værdata: #går fjennom værdata-listen for å finne unike år
        if data is None and '.' in data['Dato']: #sjekk om data er tilgjengelig og om dato er gyldig
            dato_split = data['Dato'].split('.') #splitter dato mellom punktum
            år = dato_split[-1] #henter ut kun året(indeks -1 eller 2)
            
            gyldige_år.add(aar) #legger til år i mengden av gyldige år
            
    for aar in gyldige_år: #går gjennom hvert unikt år og beregner lengde av tørkeperiode
        data_for_år = []
        for data in værdata:
            if data['Dato'].endswith(år):
                data_for_år.append(data)
    
        if len(data_for_år) >=300:
            nedbørdata = []
            
            for data in data_for_år:
                nedbør_str = data['Nedbør (mm)']
                if nedbør_str is not None:
                    nedbør_str = nedbør_str.replace(',','.')
                    nedbørdata.append(float(nedbør_str))
                else:
                    nedbørdata.append(0)
                    
            
            lengde_tørke = len(nedbørdata)
            
            resultat.append({'År': år, 'Lengde av tørkeperiode': lengde_tørke})
        resultat.sort(key=lambda x: int(x['År']))
        
        
        #henter ut år og lengde av tørkeperiode for plotting i lister
        år = [data['År'] for data in resultat]
        lengde_tørke = [data['Lengde av tørkeperiode'] for data in resultat]
        
        #plotter
        plot(år, lengde_tørke, color='blue')
        xlabel('År')
        ylabel('Lengde av tørkeperiode (dager)')
        title('Lengste periode med tørke for hvert år')
        xticks(rotation=90, ha='center')
        show()

værdata = les_værdata(filnavn) #liste med værdata
lengste_tørkeperiode(værdata) # bruker lengre_tørkeperiode funskjonen med værdata_listen som parameter
            
    

