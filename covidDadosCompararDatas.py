#!/bin/env python3
#coding: utf-8
'''
Fonte dos dados utilizados: covid.saude.gov.br

Agredecimentos ao @luckjpg por me instigar a fazer esse código simples
'''

from datetime import datetime
import operator

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
        ano, mes, dia = lista_item[2].split('-')
        data = '/'.join([dia, mes, ano])
        casosAcumulados = lista_item[4]

        if data in dicionario.keys():
            dicionario[data] += float(casosAcumulados)
        else:
            dicionario[data] = float(casosAcumulados)
    return dicionario


def ordenar_dicionario():
    dicionario = criar_dicionario()
    dicionario = sorted(dicionario.items(), key=operator.itemgetter(1))
    return dicionario


def datasRequisitadas():
    print("\nAs datas devem ser inseridas no formato dd/mm/YYYY e após 29/01/2020.\n")

    dataInicial = datetime.strptime(input('Insira a data inicial: '), '%d/%m/%Y')
    dataFinal = datetime.strptime(input('Insira a data final: '), '%d/%m/%Y')

    return dataInicial.strftime('%d/%m/%Y'), dataFinal.strftime('%d/%m/%Y')


def comparaDatas():
    dicionario = criar_dicionario()

    inicio, fim = datasRequisitadas()
    casosDataInicial = 0
    casosDataFinal = 0

    if inicio in dicionario.keys():
        casosDataInicial = dicionario[inicio]

    if fim in dicionario.keys():
        casosDataFinal = dicionario[fim]

    print(f"\nNo dia {str(inicio)} haviam: {str(casosDataInicial)} casos")
    print(f"No dia {str(fim)} haviam: {str(casosDataFinal)} casos")

    return casosDataInicial, casosDataFinal


def obtemPorcentagem():
    casosInicio, casosFim = comparaDatas()
    porcentagemDeAumento = 0

    porcentagemDeAumento = ((casosFim - casosInicio) / casosInicio if casosInicio != 0 else 1) * 100

    return porcentagemDeAumento

def mostraAoUsuario():
    porcentagem = obtemPorcentagem()
    porcentagem = round(porcentagem, 2)

    print(f"\nPortando, houve um aumento de {str(porcentagem)}% de casos de COVID-19 no Brasil durante esse período.\n")

mostraAoUsuario()