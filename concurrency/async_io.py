import asyncio
import time

from util import logger

"""
section 3
Concurrency, CPU Bound, VS I/O Bound - Async Basic
Keyword - Async I/O 
"""

"""
동시 프로그래밍 패러다임 변환
    - 싱글 코어 -> 처리향상 미미, 저하 -> 비동기 프로그래밍 -> CPU 연산, DB연동, API호출 대기 시간 늘어남
    - 파이썬 3.4 -> 비동기(asyncio) 표준 라이브러리 등장
"""


def exe_calculate_sync(name, n):
    for i in range(1, n + 1):
        logger.info(f'{name} -> {i} of {n} calculating...')
        time.sleep(1)

    logger.info(f'{name} - {n} working done')


def process_sync():
    start = time.time()

    exe_calculate_sync('one', 3)
    exe_calculate_sync('two', 2)
    exe_calculate_sync('three', 1)

    end = time.time()

    logger.info(f'total second: {end - start}')


async def process_async():
    start = time.time()

    task1 = asyncio.create_task(exe_calculate_async('one', 3))
    task2 = asyncio.create_task(exe_calculate_async('two', 2))
    task3= asyncio.create_task(exe_calculate_async('three', 1))

    await task1
    await task2
    await task3

    end = time.time()

    logger.info(f'total second: {end - start}')


async def exe_calculate_async(name, n):
    for i in range(1, n + 1):
        logger.info(f'{name} -> {i} of {n} calculating...')
        await asyncio.sleep(1)

    logger.info(f'{name} - {n} working done')

if __name__ == '__main__':
    # Sync 실행
    process_sync()

    # Async 실행
    asyncio.run(process_async())