# -*- coding: utf-8 -*-
"""
Pyzmq test
- PULL / PUSH 방법
- 벤틸레이터 (producer) of Vision

Last Updated : 2021.01.07.

@author: Hannah_Noh
"""

## 동기 방식

import zmq

'''VISION VENTILATOR : 5557'''
port = 5557

ctx = zmq.Context()

def run_ventilator() :
    # sock push 소켓 : 워커들에게 데이터를 전송하기 위한 것
    sock = ctx.socket(zmq.PUSH)
    sock.bind(f'tcp://*:{port}') # 따라서 sock은 바인딩
    
    text = 'Vision MSG Test'
    file_path = 'Vision file path Test'
    emotion = 'Vision emotion Test'
    age = 0
    gender = 'Vision gender Test'
    
    for num in range(10) :
        # send msg
        msg = {'발화문' : text,
               '파일주소' : file_path,
               '감정' : emotion,
               '나이': age,
               '성별' : gender}
        sock.send_json(msg)
        
    ctx.destroy()
    print("###DONE###")

if __name__ == '__main__' :
    run_ventilator()