#!/usr/bin/env python3
"""
Gerador de LEROLERO
Gera frases de efeito sem significado real.
"""
import random

# Cada frase é composa por três partes aleatórios; aqui,
# listas de possiblidades para cada uma das partes.
#

parte1 = ["oi", "como"]
parte2 = ["maçã", "pera"]
parte3 = ["cavalo", "zebra"]

lingua = int(input("Escolha a língua: 1 - português; 2 - inglês\n"))

if lingua == 2:
	parte1 = ["hi", "como"]
	parte2 = ["apple", "pear"]
	parte3 = ["horse", "zebra"]

#SOCORRO

# Combina as partes aleatoriamentes
#
print (random.choice(parte1), random.choice(parte2), random.choice(parte3))
