class Calculus: #Realizará os cálculos hipotéticos dos processos, cujo resultado será o tempo médio dos processos e da espera.
    def __init__(self, resultado_FIFO, resultado_SJF) -> None: 
        self.__resultadoFIFO = resultado_FIFO
        self.__resultadoSJF = resultado_SJF
        self._processos = list()
    
    def calculo_FIFO_TME(self, processos) -> None:
        inicio, calculo = 0, 0
        for i, processos in enumerate(self._processos):
            calculo += processos

    def calculo_FIFO_TMP(self, _processos) -> None:
        pass

    def calculo_SJF_TME(self) -> None:
        pass

    def calculo_SJF_TMP(self) -> None:
        pass   
   
class Validation(Calculus):
    pass    
