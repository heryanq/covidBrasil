#!/bin/env python3
#coding: utf-8
'''
Fonte dos dados utilizados: covid.saude.gov.br

Agredecimentos ao @luckjpg por me instigar a fazer esse código simples
'''

from datetime import datetime
import operator
from decimal import *
getcontext().prec = 5

def arquivo():
    abrir_arquivo = open('covidDados.csv','r')
    arquivo = abrir_arquivo.readlines()
    abrir_arquivo.close()
    return arquivo

def formatar_lista():
    lista = arquivo()
    lista_formatada = []
    for item in lista[1:]:
        lista_formatada.append(item.strip('\n'))
    return lista_formatada

def criar_dicionario():
    lista = formatar_lista()
    dicionario = {}
    for item in lista:
        lista_item = item.split(';')
        regiao = lista_item[0]
        estado = lista_item[1]
        #data = lista_item[2]
        casosNovos = lista_item[3]
        #casosAcumulados = lista_item[4]
        #obitosNovos = lista_item[5]
        #obitosAcumulados = lista_item[6]

        if lista_item[1] in dicionario.keys():
            dicionario[estado] += Decimal(casosNovos)
        else:
            dicionario[estado] = Decimal(casosNovos)
    return dicionario

def ordenar_dicionario():
    dicionario = criar_dicionario()
    dicionario = sorted(dicionario.items(), key=operator.itemgetter(1), reverse=True)
    return dicionario

def criar_arquivo():
    dicionario = ordenar_dicionario()
    arquivo = open('covidDadosComPorcentagem.csv', 'a')
    arquivo.write("Estado" + ',' "casosAcumulados")
    arquivo.write('\n')
    for tupla in dicionario:
        estado, casosAcumulados = tupla
        arquivo.write(estado + ',' + str(casosAcumulados))
        arquivo.write('\n')

criar_arquivo()

