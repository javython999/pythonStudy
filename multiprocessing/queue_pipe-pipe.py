import os
import time
from multiprocessing import Process, Pipe, current_process

from util import logger

"""
section 2
Parallelism with Multiprocessing - Queue, Pipe
Keyword - Queue, Pipe, Communications between processees
"""


# 프로세스 통신 구현 pipe


def main():
    parent_process_id = os.getpid()
    logger.info(f'Parent process id = {parent_process_id}')

    start_time = time.time()

    parent_conn, child_conn = Pipe()

    process = Process(target=worker, args=(1, 100000000, child_conn))
    process.start()

    process.join()

    logger.info(f'{round(time.time() - start_time, 4)} seconds')

    logger.info(f'Main-process Total Count = {format(parent_conn.recv(), ",")}')
    logger.info(f'Main-process Done')


def worker(id, base_number, pipe):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0

    for i in range(base_number):
        sub_total += 1

    pipe.send(sub_total)
    pipe.close()

    logger.info(f'{id} process id = {process_id} | process name = {process_name}')
    logger.info(f'result = {format(sub_total, ",")}')


if __name__ == '__main__':
    main()
