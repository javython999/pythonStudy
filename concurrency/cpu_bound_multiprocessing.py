import os
import time
from multiprocessing import current_process, Manager, Process

from util import logger

"""
section 3
Concurrency, CPU Bound, VS I/O Bound - Multiprocessing
Keyword - CPU Bound Multiprocessing
"""


def main():
    numbers = [10_000_000 + x for x in range(30)]

    processes = []

    # 프로세스 공유 매니저
    manager = Manager()

    # 프로세스 공유
    total_list = manager.list()

    start_time = time.time()

    # 프로세스 생성 및 실행
    for i in numbers:
        # 생성
        proc = Process(name=str(i), target=cpu_bound, args=(i, total_list,))
        processes.append(proc)
        proc.start()

    for proc in processes:
        proc.join()

    logger.info(f'Total list = {total_list}')
    logger.info(f'Sum = {sum(total_list)}')

    duration = time.time() - start_time
    logger.info(f'Duration = {round(duration, 3)} seconds')


def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name
    logger.info(f'Process ID = {process_id} | Process Name = {process_name}')
    total_list.append(sum(i * i for i in range(number)))


if __name__ == '__main__':
    main()
