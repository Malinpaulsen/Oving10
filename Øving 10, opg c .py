# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:04:08 2023

@author: Eline
"""



















'''
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
temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]
dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]


temperaturer_tidspunkter = list()
for index in range(len(temperaturer)):
    temperaturer_tidspunkter.append(index)



x_verdier = [1, 2, 3, 4, 5]
y_verdier = [2, 4, 5, 4, 5]

a, b = bergn_trend(temperaturer_tidspunkter, temperaturer)
print("Trend (a):", a)
print("Konstant (b):", b)

''

def har_skiføre(temperatur):
    # Anta at skiføre er tilstede når temperaturen er under 0 grader Celsius
    return temperatur < 0

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]

skiføre_dager = [har_skiføre(temp) for temp in temperaturer]

def bergn_trend(x_liste, y_liste):
    n = len(x_liste)

    # beregner gjennomsnittet av x-verdiene
    gjennomsnitt_x = sum(x_liste) / n
    gjennomsnitt_y = sum(y_liste) / n

    # Beregn a (helningen) og b (konstanten) ved hjelp av formlene
    a_teller = 0
    a_nevner = 0

    for i in range(n):
        a_teller += (x_liste[i] - gjennomsnitt_x) * (y_liste[i] - gjennomsnitt_y)
        a_nevner += (x_liste[i] - gjennomsnitt_x) ** 2 
    a = a_teller / a_nevner

    b = gjennomsnitt_y - a * gjennomsnitt_x

    return a, b

temperaturer_tidspunkter = list(range(1, len(temperaturer) + 1))

a, b = bergn_trend(temperaturer_tidspunkter, skiføre_dager)

print("Trend (a) for antall dager med skiføre:", a)
print("Konstant (b):", b)

'''

