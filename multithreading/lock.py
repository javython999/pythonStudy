import time
import threading
from concurrent.futures import ThreadPoolExecutor
from util import logger

"""
section 1
Multithreading - Thread(4) - lock, deadLock
Keyword - lock, deadLock, raceCondition, thread synchronization
"""

"""
(1). 세마포어(Semaphore): 프로레스가 공유된 자원에 접근시 문제 발생 가능성이 높기 때문에
    한 개의 프로세스만 접근처리 고안(경쟁 상태 예방)

(2). 뮤텍스(Mutex): 공유된 자원의 데이터를 여러 thread가 접근 하는 것을 막는 것(경쟁 상태 예방)

(3). Lock: 상호 배제를 위한 잠금처리
(4). DeadLock: 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착상태)
(5). Thread synchronization(스레드 동기화)를 통해 안정적으로 동작하게 처리한다.(동기화 메소드, 동기화 블럭)
(6). 세마포어와 뮤텍스의 차이점
    -> 세마포어와 뮤텍스는 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용한다는 공통점이 있지만
       뮤텍스는 단일 스레드가 리소스 또는 섹션을 소비 허용
       세마포어는 리소스 또는 섹션에 대해 제한된 수의 동시 엑세스를 허용
       *세마포어는 뮤텍스가 될 수 있지만 뮤텍스는 세마포어가 될 수 없다.
"""


class FakeDataStore:
    # 공유 변수
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()

    # 변수 업데이트 함수
    def update(self, name):
        logger.info(f'thread {name}: starting update')

        # 뮤텍스 or Lock 등 동기화(Thread Synchronization 필요)

        # Lock 획득 방법1
        # self._lock.acquire()
        # logger.info(f'thread {name} has lock')
        #
        # local_copy = self._value
        # local_copy += 1
        # time.sleep(0.1)
        # self._value = local_copy
        #
        # logger.info(f'thread {name} release lock')

        # Lock 반환
        #self._lock.release()


        # Lock 획득 방법2
        with self._lock:
            logger.info(f'thread {name} has lock')

            local_copy = self._value
            local_copy += 1
            time.sleep(0.1)
            self._value = local_copy

            logger.info(f'thread {name} release lock')



        logger.info(f'thread {name}: finish update')


if __name__ == "__main__":
    # 클래스 인스턴스화
    store = FakeDataStore()

    logger.info(f'Testing update. Starting value is {store._value}')

    # with Context 시작
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in ['First', 'Second', 'Third']:
            executor.submit(store.update, i)

    logger.info(f'Testing update. Ending value is {store._value}')
