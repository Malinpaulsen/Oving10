# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:31:15 2023

@author: Eline
"""

def median(liste): 
    liste = sorted(liste)
    lengde = len(liste)
    if lengde % 2 == 0 :
        return (liste[lengde //2 - 1] + liste[lengde//2])/2
    else: 
        return liste[lengde//2]
    
def beregn_vinddata(værdata): 
    for stasjon in værdata:
        for aar in værdata[stasjon]: 
            lista = værdata[stasjon][aar]["max_vind"]
            if len(lista) > 300: 
                værdata[stasjon][aar]["middelvind"] = sum(lista)/len(lista)
                værdata[stasjon][aar]["median_vind"] = median(lista)
if__name__ == "__main__": 
    værdata = les_værdata_fil("FILNAVN")
    beregn_skifore(værdata)
    plott:egenskaper(værdata, ["dager_skifore", "Maksimum _snoedybde"], ["dager_med_skiføre", "maksimum_snødybde"],) 
    beregn_vekst(værdata)
    plott_egenskaper(værdata, ["vekstsesong", "vekstmengde"], ["vekstsesong", "vekstmengde"])
    bergn_nedbør(værdata)
    plott_egenskaper(værdata, ["lengste_torke", "aarsnedbor"], ["lengste tørke", "årsnedbør"])
    bergn_penvaersdager(værdata)
    plott_egenskaper(værdata, ["penvaersdager"], ["antall penværsdager"])
    beregn_vinddata(værdata)
    plott_egenskaper(værdata, ["middelvind", "median_vind"], ["middelvind", "median_vind"])
        
        