#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:16:38 2023

@author: malinpaulsen
Oppgave I
En måte å sjekke trender i temperatur gjennom året er å ta gjennomsnittet av temperaturen
for en tidsperiode (for eksempel ei uke eller en måned) og så sjekke om snittet endrer seg.
Ved å ta gjennomsnittet så fjerner man at temperaturen går opp og ned fra en dag til den
neste. Regn ut gjennomsnittstemperaturen for hver måned (for eksempel april 2007) og legg
disse gjennomsnittene i ei ny liste. Bruk funksjonen fra del 1 deloppgave e) for å regne ut ei
liste med differanser. Plott både lista over gjennomsnittstemperaturer og lista over
differanser med måned og år på x-aksen
"""

import datetime
import matplotlib.pyplot as plt

#leser værdata
def les_værdata(filnavn):
    værdata = {}

    with open(filnavn, 'r', encoding='utf-8') as fil:
        linjer = fil.readlines()
        
        for linje in linjer[1:]:  # Hopper over headeren, antar at første linje er overskriftene
            komponenter = linje.strip().split(";")
            
            værdata_navn = komponenter[0]
            dato = komponenter[2]
            temperatur = float(komponenter[5]) if komponenter[5] else None  # Antar at temperatur er i sjette kolonne
            
            if værdata_navn not in værdata:
                værdata[værdata_navn] = {}
            
            aar = int(dato.split(".")[2])
            maaned = int(dato.split(".")[1])
            
            if aar not in værdata[værdata_navn]:
                værdata[værdata_navn][aar] = {}
            if maaned not in værdata[værdata_navn][aar]:
                værdata[værdata_navn][aar][maaned] = []
            
            if temperatur is not None:
                værdata[værdata_navn][aar][maaned].append(temperatur)

    return værdata

def gjennomsnittstemperaturer(værdata):
    gjennomsnittstemperaturer_per_måned = []
    for stasjon, data_per_aar in værdata.items():
        for aar, vær_i_aar in data_per_aar.items():
            for måned, temperaturer in vær_i_aar.items():
                gjennomsnitt = sum(temperaturer) / len(temperaturer)
                gjennomsnittstemperaturer_per_måned.append((aar, måned, gjennomsnitt))
    
    return gjennomsnittstemperaturer_per_måned

#Del 1: oppgave e
def beregn_differanser(tall_liste):
    differanser = []
    
    for i in range(len(tall_liste) - 1):
        differanse = tall_liste[i + 1] - tall_liste[i]
        differanser.append(differanse)
        
    return differanser

#les værdata fra filen
værdata = les_værdata('snoedybder_vaer_en_stasjon_dogn.csv')

#regn ut gjennomsnittstemperaturer for hver måned
gjennomsnittstemperaturer_per_måned = gjennomsnittstemperaturer(værdata)

#lager lister med gjennomsnittstemperaturer og differanser
temperatur_liste = [gjennomsnitt[2] for gjennomsnitt in gjennomsnittstemperaturer_per_måned]
differanser = beregn_differanser(temperatur_liste)

#plotting av gjennomsnittstemperaturer og differanser
år_måned = [(datetime.date(aar, måned, 1)) for aar, måned, _ in gjennomsnittstemperaturer_per_måned]

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(år_måned, temperatur_liste, marker='o', linestyle='-')
plt.xlabel('Måned og år')
plt.ylabel('Gjennomsnittstemperatur')
plt.title('Gjennomsnittstemperatur per måned og år')

plt.subplot(2, 1, 2)
plt.plot(år_måned[:-1], differanser, marker='o', linestyle='-')
plt.xlabel('Måned og år')
plt.ylabel('Differanse i temperatur')
plt.title('Differanse i gjennomsnittstemperatur mellom måneder')

plt.tight_layout()
plt.show()




