#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:47:45 2023

@author: chantelhelleland
"""
#Oppgave d
from datetime import datetime
import matplotlib.pyplot as plt

# Fra oppgave a
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
            
# Fra oppgave d del 1
def funksjon_flyttall_enkelverdi(liste, verdi):
    funksjon_flyttall_enkelverdi = 0
    
    for element in liste: 
        if element >= verdi:
            funksjon_flyttall_enkelverdi += 1
    
    return funksjon_flyttall_enkelverdi

# Oppgave b
#Leser værdata fra funsksjonen
vaerdata = les_værdata(filnavn)

#Lager tomme lister for vintersesong og snødybde
aarene = []
vintersesong = []
aarstall = 1980
for j in range(41):
    snødybde = []
    for i in range(len(vaerdata)-1):
        dato = datetime.strptime(vaerdata[i]["Dato"], "%d.%m.%Y")
        if (dato.year == aarstall and dato.month <= 6) or (dato.year == aarstall-1 and dato.month >= 10):
            try:
                snd = float(vaerdata[i]["Snødybde (cm)"])
                snødybde.append(snd)
            except:
                continue
        else:
            continue
   if len(snødybde) >= 200: #La til for å skjekke om det er 200 eller mer målepunkt for hvert år
           sn = funksjon_flyttall_enkelverdi(snødybde, 20)
           aarene.append(aarstall)
           vintersesong.append(sn)
    aarstall += 1

plt.plot(aarene, vintersesong)
plt.title("Skiføre")

#Fra oppgave g del 1
def bergn_trend(x_liste, y_liste):
    n = len(x_liste)


# beregner gjennomsnittet av x-verdiene
    gjennomsnitt_x = sum(x_liste) / n
    gjennomsnitt_y = sum(y_liste) / n

# Bergn a (helningen) og b (konstanten) ved hjelp av formlene

    a_teller = 0
    a_nevner = 0

    for i in range(n):
        a_teller += (x_liste [i] - gjennomsnitt_x) * (y_liste [i] - gjennomsnitt_y)
        a_nevner += (x_liste [i] - gjennomsnitt_x) **2 
    a = a_teller / a_nevner

    b = gjennomsnitt_y - a * gjennomsnitt_x

    return a, b

#Oppgave c

a,b = trend(aarene, vintersesong)

#Oppgave d
plt.plot([1980, 2020], [a*1980+b, a*2020+b ])




