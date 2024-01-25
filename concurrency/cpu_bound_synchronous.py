import time

from util import logger

"""
section 3
Concurrency, CPU Bound, VS I/O Bound - Synchronous
Keyword - CPU Bound
"""


def main():
    numbers = [10_000_000 + x for x in range(30)]

    start_time = time.time()

    total = find_sums(numbers)

    logger.info(f'Total list = {total}')
    logger.info(f'Sum = {sum(total)}')

    duration = time.time() - start_time
    logger.info(f'Duration = {round(duration, 3)} seconds')


def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    return result


def cpu_bound(number):
    return sum(i * i for i in range(number))


if __name__ == '__main__':
    main()