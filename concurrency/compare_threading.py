import concurrent.futures
import threading
import time

import requests

from util import logger

"""
section 3
Concurrency, CPU Bound, VS I/O Bound - Threading
Keyword - I/O Bound, Request
"""

# 각 스레드에 생성되는 객체(독립된 네임스페이스)
thread_local = threading.local()


def main():
    # test URL
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com"
    ] * 5

    # 실행시간
    start_time = time.time()

    # 실행
    request_all_sites(urls)

    # 종료
    duration = time.time() - start_time

    # 결과 출력
    logger.info(f'Download {len(urls)} sites in {round(duration, 3)} seconds')


def request_all_sites(urls):
    # 멀티스레드 실행
    # 반드시 max_worker 개수 조정후 session 객체 확인
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)


def request_site(url):
    # session 획득
    session = get_session()

    logger.info(f'{url}')
    logger.info(f'session : {session}')
    logger.info(f'{session.headers}')

    with session.get(url) as response:
        logger.info(f'[Read Contents : {len(response.content)} | Status Code : {response.status_code} | from {url}]')


def  get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


if __name__ == '__main__':
    main()
