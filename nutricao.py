# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:16:50 2015

@author: Dani Bento
"""

arquivoa = open("alimentos.csv", encoding="latin1")
alimentos = arquivoa.readlines()

arquivou = open("usuario.csv", encoding = "utf-8")
usuario = arquivou.readlines()
# print(usuario)

print("Ola, voce esta no nosso programa de dietas!")
print("")

linha1 = usuario[1]
dados1 = linha1.split(",")
print(dados1)
print("")

peso = int(dados1[2])
altura = float(dados1[4])*100
idade = int(dados1[1])

if dados1[3]=="M":
    formulah = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    print("A quantidade diaria de calorias ideal para seu corpo eh:", formulah)
    print("")
if dados1[3]=="F":
    formulam = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    print("A quantidade diaria de calorias ideal para seu corpo eh:", formulam)
    print("")

dic_cal = {}
for linha in alimentos:
    comidas = linha.split(",")
    chave = comidas[0]
    calorias = comidas[2]
    dic_cal[chave] = calorias

dic_datas = {}
listadatas =[]
caldia = {}

for i in usuario[3::]:
    if i[0] not in listadatas:
        x = i.split(",")
        caldia[x[0]]= 0
        
for i in usuario[3::]:
    if i[0] not in listadatas:
        x = i.split(",")
#        print(x)
        listadatas.append(x[0])
        dic_datas[x[0]]= {}
    caloriasingeridas = int((int(dic_cal[x[1]])/100)*float(x[2]))
#    print(caloriasingeridas)
    caldia[x[0]] += caloriasingeridas
    
print("A quantidade diaria de calorias ingeridas no dia 1 foi de:", caldia["6/4/15"])
print("A quantidade diaria de calorias ingeridas no dia 2 foi de:", caldia["7/4/15"])            

dic_pro = {}
for linha in alimentos:
    comidas = linha.split(",")
    chave = comidas[0]
    proteinas = comidas[3]
    dic_pro[chave] = proteinas

dic_carb = {}
for linha in alimentos:
    comidas = linha.split(",")
    chave = comidas[0]
    carboidratos = comidas[4]
    dic_carb[chave] = carboidratos

dic_gord = {}
for linha in alimentos:
    comidas = linha.split(",")
    chave = comidas[0]
    gorduras = comidas[5]
    dic_gord[chave] = gorduras