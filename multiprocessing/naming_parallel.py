import os
import random
import time
from multiprocessing import Process, current_process

from util import logger

"""
section 2
Parallelism with Multiprocessing - Naming
Keyword - Naming, Parallel procssing
"""


def square(n):
    # 랜덤 sleep
    time.sleep(random.randint(1, 3))
    process_id = os.getpid()
    process_name = current_process().name

    # 제곱
    result = n ** 2
    logger.info('-' * 40)
    logger.info(f'Process ID = {process_id}, Procss Name = {process_name}')
    logger.info(f'{n} square = {result}')


if __name__ == '__main__':
    # 부모 프로세스 ID
    parent_process_id = os.getpid()

    # 출력
    logger.info(f'Parent process ID = {parent_process_id}')

    # 프로세스 list 선언
    processes = []

    # 프로세스 생성 및 실행
    for i in range(1, 200):
        # 생성
        proc = Process(name=str(i), target=square, args=(i,))

        # 배열에 담기
        processes.append(proc)

        # 시작
        proc.start()

    for process in processes:
        process.join()

    logger.info('Main-Processing Done')
