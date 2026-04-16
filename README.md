# Changelog
# Versão 1.1 lançada!
Algumas modificações foram feitas, sendo elas:
- Correção de erros (O programa não mais dá erro se você digitar zero ou números abaixo de zero);
- Revisões no código, e removeção de linhas de código não-funcionais.

# Versão 1.0 agora já lançada hoje!

# Escalonador de Processos

Este projeto é um aplicativo de linha de comando em Python para calcular métricas de escalonamento de processos usando os algoritmos FIFO e SJF.

## O que ele faz

- Recebe do usuário a quantidade de processos e os tempos de duração de cada um.
- Calcula o tempo médio de espera (TME) e o tempo médio de processo/retorno (TMP) para cada algoritmo.
- Compara dois esquemas de escalonamento:
  - FIFO (First In, First Out): processos são executados na ordem de entrada.
  - SJF (Shortest Job First): processos são ordenados pelo menor tempo de execução primeiro.

## Como o cálculo funciona

O aplicativo usa a classe `Calculus` definida em `calculus.py`:

- `calcular_metricas(valores: list) -> tuple[float, float]`
  - calcula o tempo médio de espera somando os tempos de espera acumulados de cada processo.
  - calcula o tempo médio de processo usando a soma dos tempos de espera mais o tempo de execução total dividido pelo número de processos.
- `processar_fifo(processos_originais: list)`
  - aplica `calcular_metricas` diretamente na lista na ordem recebida.
- `processar_sjf(processos_originais: list)`
  - ordena a lista de tempos de processo e então calcula as métricas.

## Arquivos principais

- `app.py`
  - interface interativa pelo terminal.
  - lê entradas do usuário.
  - exibe resultados de TME e TMP para FIFO e SJF.
- `calculus.py`
  - lógica de cálculo de métricas de escalonamento.
  - abstrai as fórmulas de espera e retorno.

## Fluxo de execução

1. O programa exibe um cabeçalho e solicita o número de processos.
2. Para cada processo, pede o tempo de duração.
3. Executa os cálculos para FIFO e SJF.
4. Mostra o tempo médio de espera e o tempo médio de processo para cada algoritmo.
5. Pergunta se o usuário deseja continuar ou encerrar.

## Como rodar

- Execute `app.py` com Python 3:
  - `python app.py`
- Insira quantos processos quiser e os tempos de duração.
- Veja os resultados para os dois algoritmos.
- Execute o 'escalonador de processos.exe' que já pode ser baixado!

## Propósito

O projeto demonstra conceitos básicos de escalonamento de processos, programação orientada a objetos em Python e implementação de cálculos de métricas de desempenho de execução.
