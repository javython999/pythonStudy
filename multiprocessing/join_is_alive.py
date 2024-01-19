import multiprocessing
from multiprocessing import Process
import time
import util.logger as logger

from concurrent.futures import ProcessPoolExecutor

"""
section 2
Parallelism with Multiprocessing - multiprocessing(1) - Join, is_alive
Keyword - multiprocessing, processing state
"""


def main():
    process = Process(target=process_function, args=('First',))



    logger.info('Multi-Process: before creating Process')

    #process.start()

    logger.info(f'Sub-process is alive?: {process.is_alive()}')
    logger.info('Multi-Process: During Process')

    #logger.info('Multi-Process: Terminated Process')
    #process.terminate()

    logger.info('Multi-Process: Joined Process')
    #process.join()


    logger.info(f'Sub-process is alive?: {process.is_alive()}')

    logger.warning(f'ProcessPoolExecutor Start')

    cpu_core_count = multiprocessing.cpu_count()
    logger.fatal(f'CPU COUNT = {cpu_core_count}')
    param_list = []
    for i in range(cpu_core_count, cpu_core_count+1):
        param_list.append(f'{i}')

    with ProcessPoolExecutor(max_workers=cpu_core_count) as executor:
        executor.map(process_function, param_list)




def process_function(name):
    logger.info(f"Sub-process {name}: starting")
    time.sleep(3)

    for i in range(1, 1000001):
        logger.warning(i)
    logger.info(f"Sub-process {name}: finish")


# 메인 시작
if __name__ == '__main__':
    main()
