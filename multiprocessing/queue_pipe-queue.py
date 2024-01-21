import os
import time
from multiprocessing import Process, Queue, current_process

from util import logger

"""
section 2
Parallelism with Multiprocessing - Queue, Pipe
Keyword - Queue, Pipe, Communications between processees
"""

# 프로세스 통신 구현 Queue


def main():
    parent_process_id = os.getpid()
    logger.info(f'Parent process id = {parent_process_id}')

    processes = []

    start_time = time.time()

    queue_ = Queue()

    for i in range(10):
        process = Process(target=worker, args=(i, 10000000, queue_))
        processes.append(process)
        process.start()

    for proc in processes:
        proc.join()

    logger.info(f'{round(time.time() - start_time, 4)} seconds')

    # 종료 flag
    queue_.put('exit')

    # 대기
    total = 0
    while True:
        temp = queue_.get()

        if temp == 'exit':
            break
        else:
            total += temp

    logger.info(f'Main-process Total Count = {format(total, ",")}')
    logger.info(f'Main-process Done')

def worker(id, base_number, queue):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0

    for i in range(base_number):
        sub_total += 1

    queue.put(sub_total)

    logger.info(f'{id} process id = {process_id} | process name = {process_name}')
    logger.info(f'result = {format(sub_total, ",")}')



if __name__ == '__main__':
    main()