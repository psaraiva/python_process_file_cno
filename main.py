import argparse
import csv
import logging
import os
import psutil
import time

# Configuração do log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Processo atual
process = psutil.Process(os.getpid())
# Estatísticas de uso de memória, valor mínimo
memory_usage_min = -1
# Estatísticas de uso de memória, valor máximo
memory_usage_max = -1
# Quantidade de interações executadas
loop_count = 0
# Linha inicial
loop_start = -1
# Linha final
loop_end = None

def main():
    global loop_count, loop_start, loop_end

    start_time = time.time()
    loop = 0

    logging.info("Iniciando: Script.")
    parser = argparse.ArgumentParser(description='Processa uma parte do arquivo cno.csv.')
    parser.add_argument('--row-start', type=int, required=True, help='Linha inicial para processamento.')
    parser.add_argument('--row-stop', type=int, required=False, help='Linha final para processamento.')
    args = parser.parse_args()
    row_start = args.row_start
    row_stop = args.row_stop

    m = process.memory_info().rss / (1024 * 1024)
    set_statistics_memory_usage(m)
    logging.info(f"Uso de memória: {m:.2f} MB.")

    with open('cno.csv', mode='r', newline='\n', encoding='latin1') as file:
        reader = csv.reader(file)
        for line in reader:
            loop += 1
            loop_end = loop

            if loop < row_start:
                continue
            if isinstance(row_stop, int) and loop > row_stop:
                loop_end -= 1
                break
            if loop == row_start:
                loop_start = row_start

            logging.info("+------------------------------------------+")
            logging.info(f"Linha: #{loop}")
            logging.info(f"Valor da linha: {line}.")
            loop_count += 1

            m = process.memory_info().rss / (1024 * 1024)
            set_statistics_memory_usage(m)
            logging.info(f"Uso de memória: {m:.2f} MB.")

    logging.info("Finalizando: Script.")
    show_statistics()
    execution_time = time.time() - start_time
    logging.info(f"Tempo de execução: {execution_time:.3f} segundos.")

def set_statistics_memory_usage(memory_usage:float) -> None:
    """
    Atualiza as estatísticas de uso de memória RAM, uso mínimo e média.

    Args:
        memory_usage (float): A porcentagem de uso da CPU a ser registrada.

    Returns:
    None
    """
    global memory_usage_min, memory_usage_max
    if memory_usage_min == -1:
        memory_usage_min = memory_usage
    if memory_usage_max == -1:
        memory_usage_max = memory_usage
    if memory_usage > memory_usage_max:
        memory_usage_max = memory_usage
    if memory_usage < memory_usage_min:
        memory_usage_min = memory_usage

def show_statistics() -> None:
    """
    Exibe as estatísticas de uso de memória, CPU e quantidade de linhas executadas no log.

    Args:
    None

    Returns:
    None
    """
    logging.info(f"Linha inicial: {loop_start}.")
    logging.info(f"Linha final: {loop_end}.")
    logging.info(f"Total de linhas: {loop_count}.")
    logging.info(f"Memória min: {memory_usage_min:.2f} MB.")
    logging.info(f"Memória max: {memory_usage_max:.2f} MB.")

if __name__ == "__main__":
    main()
