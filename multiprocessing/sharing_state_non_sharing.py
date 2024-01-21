import os
from multiprocessing import current_process, Process

from util import logger

"""
section 2
Parallelism with Multiprocessing - Sharing state
Keyword - memory sharing, array, value
"""


# 프로세스 메모리 비공유

def main():
    parent_process_id = os.getpid()
    logger.info(f'Parent process ID = {parent_process_id}')

    processes = []
    share_value = 0

    for _ in range(10):
        process_ = Process(target=generate_update_number, args=(share_value,))
        processes.append(process_)
        process_.start()

    for proc in processes:
        proc.join()

    logger.info(f'Parent share_value = {share_value}')


def generate_update_number(value: int):
    for _ in range(50):
        value += 1

    logger.info(f'{current_process().name} | data = {value}')


if __name__ == '__main__':
    main()