#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 01:53:55 2023

@author: malinpaulsen

Oppgave G
Finn antall penværsdager for hvert år og plott dette. Man kan finne antall penværsdager ved
å sjekke gjennomsnittlig skydekke. Hver dag med verdi 3 eller lavere er en penværsdag.
Inkluder bare år hvor det er data om skydekke for mesteparten av året, det må være data for
minst 300 dager for at et år skal være gyldig.
"""
import matplotlib.pyplot as plt

#leser værdata
def les_værdata(filnavn):
    værdata = {}
    
    with open(filnavn, 'r', encoding='utf-8') as fil:
        linjer = fil.readlines()
        
        for linje in linjer [1:]:
            komponenter = linje.strip().split(";")
            
            værdata_navn = komponenter[0]
            dato = komponenter[2]
            skydekke = float(komponenter[6]) if komponenter [6] else None 
        
            if værdata_navn not in værdata:
                værdata[værdata_navn] = {}
                
            aar = int(dato.split(".")[2])
            maaned = int(dato.split(".")[1])
            snoedybder_aar = aar - 1 if maaned < 6 else aar
            
            if snoedybder_aar not in værdata[værdata_navn]:
                værdata[værdata_navn][snoedybder_aar] = {"skydekke": []}
                
            if skydekke is not None:
                værdata[værdata_navn][snoedybder_aar]["Skydekke"].append(skydekke)
                
        return penvaer_per_year
    
    
#finner antall penværsdager per år 
def finn_penvaersdager(værdata, skydekkegrense=3, minimum_dager=300):
    penvaer_per_year = {}
    
    for stasjon, data_per_aar in værdata.items():
        penvaer_per_year[stasjon] = {}
        for aar, vær_i_aar in data_per_aar.items():
            skydekke_liste = vær_i_aar.get("skydekke", [])
            if len(skydekke_liste) >= minimum_dager:
                gjennomsnitt_skydekke = sum(skydekke <= skydekkegrense for skydekke in skydekke_liste) / len(skydekke_liste)
                penvaer_per_year[stasjon][aar] = gjennomsnitt_skydekke

    return penvaer_per_year


#plotter informasjonen om antall penværsdager
def plot_penvaersdager(penvaer_per_year):
    for stasjon, data_per_aar in penvaer_per_year.items():
        år = list(data_per_aar.keys())
        penvaer_dager = list(data_per_aar.values())
        plt.figure(figsize=(10, 6))
        plt.bar(år, penvaer_dager, color='skyblue')
        plt.xlabel('År')
        plt.ylabel('Andel penværsdager')
        plt.title(f'Andel penværsdager per år for {stasjon}')
        plt.grid(True)
        plt.show()

værdata = les_værdata('snoedybder_vaer_en_stasjon_dogn.csv')
penvaer_per_year = finn_penvaersdager(værdata)
plot_penvaersdager(penvaer_per_year)

