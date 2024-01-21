import os
from multiprocessing import current_process, Process, Value

from util import logger

"""
section 2
Parallelism with Multiprocessing - Sharing state
Keyword - memory sharing, array, value
"""


# 프로세스 메모리 공유

def main():
    parent_process_id = os.getpid()
    logger.info(f'Parent process ID = {parent_process_id}')

    processes = []
    # 프로세스 메모리 공유
    # from multiprocess import shared_memory
    # from multiprocess import Manager
    share_value = Value('i', 0)

    for _ in range(10):
        process_ = Process(target=generate_update_number, args=(share_value,))
        processes.append(process_)
        process_.start()

    for proc in processes:
        proc.join()

    logger.info(f'Parent share_value = {share_value.value}')


def generate_update_number(sharing_value: int):
    for _ in range(50):
        sharing_value.value += 1

    logger.info(f'{current_process().name} | data = {sharing_value.value}')


if __name__ == '__main__':
    main()