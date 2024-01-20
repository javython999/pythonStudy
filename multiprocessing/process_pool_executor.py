import urllib.request
from concurrent.futures import ProcessPoolExecutor, as_completed

from util import logger

"""
section 2
Parallelism with Multiprocessing - Process Pool Executor
Keyword - ProcessPoolExecutor, as_completed, future, timeout, dictionary
"""

# 조회 URL
URLS = [
    'https://www.daum.net/',
    'https://edition.cnn.com/',
    'https://naver.com/',
    'https://bbs.ruliweb.com/',
    'https://some-made-up-domain.com'
]


# 실행함수
def main():
    # 프로세스 풀 Context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        # Future 로드
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

        # 실행
        for future in as_completed(future_to_url):
            # Key값이 Future 객체
            url = future_to_url[future]

            try:
                # 결과
                data = future.result()
            except Exception as e:
                logger.error(f'{url} generated an exception: {e}')
            else:
                # 결과 확인
                logger.info(f'{url} page is {format(len(data), ",")} bytes')



def load_url(url, timeout):
    with urllib.request.urlopen(url=url, timeout=timeout) as conn:
        return conn.read()



if __name__ == '__main__':
    main()

