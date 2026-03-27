class Calculus: #Realizará os cálculos hipotéticos dos processos, cujo resultado será o tempo médio dos processos e da espera.
    def __init__(self) -> None:
        pass

    def calcular_metricas(self, valores:list) -> tuple[float, float]:
        numero_valores = len(valores)
        espera_acumulada = 0
        tempos_espera = list()
        tempo_atual = 0

        for tempo_exec in valores:
            tempos_espera.append(tempo_atual)
            espera_acumulada += tempo_atual
            tempo_atual += tempo_exec
        
        tempo_medio_espera = espera_acumulada/numero_valores #Cálculo do TME.

        tempo_medio_processo = (espera_acumulada + sum(valores))/numero_valores #Cálculo do TMP.
        return tempo_medio_espera, tempo_medio_processo
    
    def processar_fifo(self, processos_originais: list):
        return self.calcular_metricas(processos_originais) #Apenas retorna as métricas calculadas.

    def processar_sjf(self, processos_originais:list):
        lista_ordenada = sorted(processos_originais) #Reordenação da lista, de acordo com o funcionamento do algoritmo SJF.
        return self.calcular_metricas(lista_ordenada)
    