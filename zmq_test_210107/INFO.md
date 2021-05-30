# [2021.01.07.] ZeroMQ 다중 port Test

### 1. 구현 내용

- 기본 TCP 통신
- PULL-PUSH 방식
- 동기화 → 추후 비동기화 필요
- json 통신
- for문을 통한 한정적 통신 → 추후 while문 변경 필요

### 2. port 번호

- ink(Result Collector) port : 5556
- Worker(Consumers)
- Ventilator1(Producer / for Vision AI) - port : 5557
- Ventilator2(Producer / for Speech AI) - port : 5558
