# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 12:59:59 2023

@author: Eline
"""
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
print(vær_info[2001]["snoedybder"])
    
                                     
    
'''    
            
   # delopg c 
def plott_egenskpaer(værdata, nokkel_liste, tittel_liste, med_trend=False):
    antall_stasjoner = len(værdata)
    antall_nokler = len(nokkel_liste)
    index = 0
    for stasjon in værdata: 
        aar_liste = list(værdata[stasjon].keys())
        aar_liste.sort()
        for i in range(antall_nokler): 
            plt.subplot(antall_stasjoner, antall_nokler, index*antall_nokler + i + 1)
            plt.title(stasjon + " " + tittel_liste[i])
            x_liste = list()
            y_liste = list()
            for aar in aar_liste: 
                if nokkel_liste[i] in værdata[stasjon][aar]:
                    x_liste.append(aar)
                    y_liste.append(værdata[stasjon][aar][nokkel_liste[i]])
                if len(x_liste) > 2: 
                    plt.plot(x_liste, y_liste, "0-")
                    
                    
                    
         
            
            
'''  
        
'''
            
        navn, stasjonsid, dato, snødybde, nedbør, temperatur, skydekke, vind = linje.strip().split(';')

        # Håndter "-" for manglende data
        if snødybde == '-':
            snødybde = None
        else:
            snødybde = float(snødybde)

        if nedbør == '-':
            nedbør = None
        else:
            nedbør = float(nedbør)

        if temperatur == '-':
            temperatur = None
        else:
            temperatur = float(temperatur)

        if skydekke == '-':
            skydekke = None
        else:
            skydekke = int(skydekke)

        if vind == '-':
            vind = None
        else:
            vind = float(vind)

        værdata.append({
            'Navn': navn,
            'Stasjonsid': stasjonsid,
            'Dato': dato,
            'Snødybde (cm)': snødybde,
            'Nedbør (mm)': nedbør,
            'Middeltemperatur': temperatur,
            'Skydekke (0-8)': skydekke,
            'Høyeste middelvind (m/s)': vind
        })

    return værdata

# Eksempel på bruk av funksjonen:
filnavn = 'snoedybder_vaer_en_stasjon_dogn.csv'
værdata = les_værdata(filnavn)
for døgn in værdata:
    print(døgn)

'''