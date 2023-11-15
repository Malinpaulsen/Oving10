#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:16:39 2023

@author: malinpaulsen
Oppgave E
Beregn veksten for den tenkte planten for hvert år i datasettet med bruk av funksjonen fra
del 1 oppgave h). Plott dette for hvert år i datasettet. Inkluder bare år hvor det er
temperaturdata for mesteparten av året, det må være data for minst 300 dager for at et år
skal være gyldig. Dette vil kreve at dere lager separate lister for hvert år som kan brukes som
parameter til funksjonen fra del 1 oppgave h
"""

import matplotlib.pyplot as plt


#Funkjson fra del 1: oppg. H
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
            
            if aar not in værdata[værdata_navn]:
                værdata[værdata_navn][aar] = []
            
            if temperatur is not None:
                værdata[værdata_navn][aar].append(temperatur)

    return værdata

def vekst(temperatur_liste):
    total_vekst = 0
    
    for temperatur in temperatur_liste:
        if temperatur > 5:
            vekst = temperatur - 5
            total_vekst += vekst
    
    return total_vekst

def beregn_vekst_per_år(værdata):
    vekst_per_år = {}
    
    for stasjon, data_per_aar in værdata.items():
        for aar, temperaturer in data_per_aar.items():
            if len(temperaturer) >= 300:
                vekst_per_år.setdefault(aar, []).append(vekst(temperaturer))
    
    return vekst_per_år

#plotter informasjon
def plot_vekst(vekst_per_år):
    for aar, vekst_liste in vekst_per_år.items():
        plt.figure(figsize=(8, 5))
        plt.plot([i for i in range(1, len(vekst_liste) + 1)], vekst_liste, marker='o', linestyle='-')
        plt.xlabel('Måling')
        plt.ylabel('Vekst over 5 grader')
        plt.title(f'Vekst over 5 grader for år {aar}')
        plt.grid(True)
        plt.show()

#leser værdata fra filen
værdata = les_værdata('snoedybder_vaer_en_stasjon_dogn.csv')

#beregner vekst per år med gyldige temperaturdata
vekst_per_år = beregn_vekst_per_år(værdata)

#plotter vekst for hvert år
plot_vekst(vekst_per_år)





