#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:40:12 2023

@author: chantelhelleland
"""

# Oppgave b
"""
Dere kan regne med at det er skiføre om snødybden på værstasjonen er 20 centimeter eller
mer. Regn ut antall dager med skiføre for hver vintersesong i datasettet. En vintersesong
strekker seg fra oktober ett år til juni året etterpå. Bruk funksjonen fra del 1 oppgave d) til å
beregne antall dager med skiføre i hver skisesong. Dette vil kreve at dere lager egne lister for
hver skisesong som dere kan bruke som input til funksjonen fra del 1 oppgave d
"""

#Fra oppgave a

from datetime import datetime

def sett_inn_komponent_hvis_gyldig(liste, komponent):
    try:
        komponent = komponent.replace(",",".")
        tall = float(komponent)
        liste.append(tall)
    except ValueError:
        pass


def initialiser_aar(dictionary, aar):
    dictionary[aar] = dict()
    dictionary[aar]["snoedybder"] = list()
    dictionary[aar]["nedbor_dogn"] = list()
    dictionary[aar]["temperatur"] = list()
    dictionary[aar]["skydekke"] = list()
    dictionary[aar]["max_vind"] = list()

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
    
    

#Fra oppgave d i øving 4
def funksjon_flyttall_enkelverdi(liste, verdi):
    funksjon_flyttall_enkelverdi = 0
    
    for element in liste: 
        if element >= verdi:
            funksjon_flyttall_enkelverdi += 1
    
    return funksjon_flyttall_enkelverdi

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
    sn = funksjon_flyttall_enkelverdi(snødybde, 20)
    aarene.append(aarstall)
    vintersesong.append(sn)
    aarstall += 1

plt.plot(aarene, vintersesong)
plt.title("Skiføre")


