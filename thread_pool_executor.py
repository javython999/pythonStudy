from concurrent.futures import ThreadPoolExecutor
import logger

"""
section 1
Multithreading - Thread(3) - threadPoolExecutor
Keyword - Many threads, concurrent.futures, ****PoolExecutor
"""

"""
Group Thread
(1). Python 3.2 이상 표준 라이브러리 사용
(2). concurrent.futures
(3). with 사용으로 생성, 소멸 생명주기 관리 용이
(4). 디버깅 난해(단점)
(5). 대기중인 작업 -> Queue -> 완료 상태 조사 -> 결과 또는 예외 반환 -> 단일화(캡슐화)
"""

def main():
    # 실행 방법1
    # max_worker: 작업의 개수가 넘어가면 직접 설정이 유리
    #executor = ThreadPoolExecutor(max_workers=3)
    #task1 = executor.submit(task, ("First",))
    #task2 = executor.submit(task, ("Second",))

    # 결과값이 있을 경우
    #print(task1.result())
    #print(task2.result())


    # 실행 방법2
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ['First', 'Second', 'Third'])

        print(list(tasks))

def task(name):
    logger.info(f"Sub-Theard {name}: starting")
    result = 0

    for i in range(10001):
        result += i

    logger.info(f"Sub-Theard {name}: finish | result = {result}")

    return result


if __name__ == '__main__':
    main()