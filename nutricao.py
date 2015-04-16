# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:10:51 2015

@author: david
"""

arquivoa = open("alimentos.csv", encoding="latin1")
alimentos = arquivoa.readlines()

arquivou = open("usuario.csv", encoding = "utf-8")
usuario = arquivou.readlines()
print(usuario)
print("")

linha1 = usuario[1]
dados = linha1.split(",")
print(dados)
print("")

peso = int(dados[2])
altura = float(dados[4])*100
idade = int(dados[1])

if dados[3]=="M":
    formulah = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    print("A quantidade diaria de calorias ideal para seu corpo eh:", formulah)
    print("")
if dados[3]=="F":
    formulam = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    print("A quantidade diaria de calorias ideal para seu corpo eh:", formulam)
    print("")

dic_cal = {}
for linha in alimentos:
    comidas = linha.split(",")
    chave = comidas[0]
    calorias = comidas[2]
    dic_cal[chave] = calorias
print(dic_cal)
    