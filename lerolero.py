#!/usr/bin/env python3
"""
Gerador de LEROLERO
Gera frases de efeito sem significado real.
"""
import random

# Cada frase é composa por três partes aleatórios; aqui,
# listas de possiblidades para cada uma das partes.
#

parte1 = [
    "O sistema em desenvolvimento",
    "O novo protocolo de comunicação",
    "O algoritmo otimizado"
]
parte2 = [
    "Possui excelente desempenho",
    "oferece garantias de precisão acima da média",
    "preenche uma lacum significiativa"
]
parte3 = [
    "nas aplicações a que se destina",
    "em relações às opções disponíveis no mercado",
    ", provendo ampla vantagem competitiva a seus usuários"
]
lingua = int(input("Escolha a língua: 1 - português; 2 - inglês\n"))

if lingua == 2:
    parte1 = ["hi", "como"]
    parte2 = ["apple", "pear"]
    parte3 = ["horse", "zebra"]

#SOCORRO

# Combina as partes aleatoriamentes
#
print (random.choice(parte1), random.choice(parte2), random.choice(parte3))
