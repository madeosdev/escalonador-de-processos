class Calculus: #Realizará os cálculos hipotéticos dos processos, cujo resultado será o tempo médio dos processos e da espera.
    def __init__(self, resultado_FIFO, resultado_SJF) -> None: 
        self.__resultadoFIFO = resultado_FIFO
        self.__resultadoSJF = resultado_SJF
        self._processos = int()
    
    def calculo_FIFO_TME(self, _processos: int, valores: list) -> int:
        espera, divisao = 0, 0
        for i, valor in enumerate(valores):
            if i == 0:
                espera += 0
            else:
                espera += valor
        divisao = espera/_processos
        return int(divisao)
    
    def calculo_FIFO_TMP(self, _processos: int, valores: list) -> int:
        calculo, divisao = 0, 0
        for i, valor in enumerate(valores):
            calculo += valor
        divisao = calculo/_processos
        return int(divisao)


    def calculo_SJF_TME(self) -> None:
        pass

    def calculo_SJF_TMP(self) -> None:
        pass   
   
class Validation(Calculus):
    pass    
