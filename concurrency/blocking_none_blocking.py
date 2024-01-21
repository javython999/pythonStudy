"""
section 3
Concurrency, CPU Bound, VS I/O Bound - Blocking VS Non-Blocking IO
Keyword - Blocking, Non-Blocking IO, Sync, Async
"""

"""
Blocking IO VS Non-Blocking IO

    blocking IO
        - 시스템 콜 요청시 커널 IO 작업 완료 시 까지 응답 대기
        - 제어권: IO작업 -> 커널 -> 응답 전까지 대기 (Block) : 다른 작업 수행 불가(대기)
        
    non-blocking IO
        - 시스템 콜 요청시 커널IO 완료여부 상관 없이 즉시 응답
        - 제어권: IO작업 -> 유저프로세스 : 다른작업 수행가능 (주기적으로 시스템 콜에서 IO작업 완료여부 확인)
        
    
Async VS Sync
    
    Async
        - IO작업 완료 여부에 대한 Noty는 커널(호출되는 함수) -> 유저프로세스(호출하는 함수)
    
    Sync
        - IO작업 완료 여부에 대한 Notiy는 유저프로세스(호출하는 함수) -> 커널(호출되는 함수)
         
"""