import os
from time import sleep
import calculus
import numpy as np

print('-'*40)
print('Escalonador de Processos by MadeosDev!')
print('-'*40)
array_processos = np.array([])
array_espera = np.array([])
lista_inicios = list()

while True:
    num_processos = int(input('Quantos processos você quer calcular?'))
    for i in range(0, num_processos):
        inicio = int(input(f'Ponto de início do Processo {i+1}?'))
        lista_inicios.append(inicio)
        tmp = int(f'Qual é o tempo de duração do Processo {i+1}?')
        tme = int(input(f'Qual é o tempo de espera do Processo {i+1}'))
        