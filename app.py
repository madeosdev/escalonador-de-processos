from time import sleep
# Importa a classe Calculus do módulo calculus, responsável pelos cálculos de escalonamento
import calculus


print('-'*40)
print('Escalonador de Processos by MadeosDev!')
print('-'*40)
lista_processos = list()
calc = calculus.Calculus()
sleep(2)

while True:
    lista_processos.clear()
    num_processos = int(input('Quantos processos você quer calcular?'))
    for i in range(0, num_processos):
        tempo_processo = int(input(f'Qual é o tempo de duração do Processo {i+1}?'))
        lista_processos.append(tempo_processo)
    
    print('CALCULANDO...')
    sleep(3.5)
    tme_fifo, tmp_fifo = calc.processar_fifo(lista_processos)
    tme_sjf, tmp_sjf = calc.processar_sjf(lista_processos)
    print(('-'*15), 'RESULTADO CÁLCULO DO FIFO', ('-'*15))
    print(f"TEMPO MÉDIO DE ESPERA: {tme_fifo} segundos.")
    print(f'TEMPO MÉDIO DE PROCESSO: {tmp_fifo} segundos.')
    sleep(2)      
    print(('-'*15), 'RESULTADO CÁLCULO DO SJF', ('-'*15))
    print(f'TEMPO MÉDIO DE ESPERA: {tme_sjf} segundos. ')
    print(f'TEMPO MÉDIO DE PROCESSO: {tmp_sjf} segundos')

    escolha = str(input('Quer continuar?[S/N]: ')).upper().strip()
    while escolha not in 'SN':
        print('Escolha inválida! Tente novamente!')
        escolha = str(input('Quer continuar?[S/N]: ')).upper().strip()
    if escolha in 'N':
        print('ENCERRANDO...')
        sleep(3)
        break
    