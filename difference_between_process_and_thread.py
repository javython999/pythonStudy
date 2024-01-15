"""
section 1
Multithreading - Difference between Process and Thread
Keyword - Process, Thread
"""


"""
(1). process
    - 운영체제에서 할당 받는 자원의 단위(실행 중인 프로그램)
    - CPU 동작, 주소 공간(독립적)
    - Code, Data, Stack, Heap -> 독립적
    - 최소 1개의 메인 스레드 보유
    - 파이프, 파일, 소켓 등을 사용해서 프로레스간 통신(context switching cst가 높다)

(2). thread
    - 프로세스 내에 실행 흐름 단위
    - 프로세스 자원 사용
    - Stack만 별도 할당. 나머지(Code, Data, Heap)는 공유 
    - 메모리 공유(변수 공유)
    - 한 스레드의 결과가 다른 스레드에 영향 끼침
    - 동기화 문제는 정말 주의가 필요(디버깅 어려움)

(3). multi thread
    - 한 개의 단일 애플리케이션(응용프로그램) -> 여러 스레드로 구성 후 작업 처리
    - 시스템 자원 소모 감소(효율성 증가, 처리량 증가)
    - 통신 부담 감소, 디버깅 어려움, 단일 프로세스에는 효과 미약, 자원 공유 문제(교착 상태, 프로세스에 영향)

(4). multi process
    - 한 개의 단일 애플리케이션(응용프로그램) -> 여러 프로세스 구성 후 작업 처리
    - 한 개의 프로세스 문제 발생은 확산 없음(프로세스 kill)
    - 캐시 체인지, Cost 비용 매우 높음(오버헤드)
"""