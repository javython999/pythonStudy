import time

import requests

from util import logger

"""
section 3
Concurrency, CPU Bound, VS I/O Bound - Synchronous
Keyword - I/O Bound, Request
"""


def main():
    # test URL
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com"
    ] * 3

    # 실행시간
    start_time = time.time()

    # 실행
    request_all_sites(urls)

    # 종료
    duration = time.time() - start_time

    # 결과 출력
    logger.info(f'Download {len(urls)} sites in {round(duration, 3)} seconds')


def request_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            request_site(url, session)


def request_site(url, session):
    logger.info(f'{url}')
    logger.info(f'{session.headers}')

    with session.get(url) as response:
        logger.info(f'[Read Contents : {len(response.content)} | Status Code : {response.status_code}]')


if __name__ == '__main__':
    main()
