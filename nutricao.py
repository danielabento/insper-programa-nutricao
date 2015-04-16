# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:16:50 2015

@author: Dani Bento
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
