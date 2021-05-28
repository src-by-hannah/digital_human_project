# -*- coding: utf-8 -*-
"""
Pyzmq test
- PULL / PUSH 방법
- 워커 (consumers)

Last Updated : 2021.01.07.

@author: Hannah_Noh
"""

## 동기 방식

import zmq

'''UNREAL SINK : 5556'''
'''VISION VENTILATOR : 5557'''
'''SPEECH VENTILATOR : 5557'''
vision_port = 5557
speech_port = 5558
port_push = 5556

ctx = zmq.Context()

def run_worker() :
    # 벤틸레이터와의 연결(PULL, recieve work)
    sock_vision = ctx.socket(zmq.PULL)
    sock_vision.connect(f'tcp://localhost:{vision_port}')
    
    # 벤틸레이터2와의 연결(PULL, recieve work)
    sock_speech = ctx.socket(zmq.PULL)
    sock_speech.connect(f'tcp://localhost:{speech_port}')
    
    # 싱크와의 연결(PUSH, send work)
    sock_push = ctx.socket(zmq.PUSH)
    sock_push.connect(f'tcp://localhost:{port_push}')

    for x in range(10) :
        recv_vision = sock_vision.recv_json()
        recv_speech = sock_speech.recv_json()
        
        result = {'v_발화문' : recv_vision['발화문'],
                  'v_파일주소' : recv_vision['파일주소'],
                  'v_감정' : recv_vision['감정'],
                  'v_나이' : recv_vision['나이'],
                  'v_성별' : recv_vision['성별'],
                  's_발화문' : recv_speech['발화문'],
                  's_파일주소' : recv_speech['파일주소']}

        sock_push.send_json(result)
        
    ctx.destroy()
    print("###DONE###")
    
if __name__ == '__main__' :
    run_worker()
