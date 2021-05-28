# -*- coding: utf-8 -*-
"""
Pyzmq test
- PULL / PUSH 방법
- 벤틸레이터 (producer) of Speech

Last Updated : 2021.01.07.

@author: Hannah_Noh
"""

## 동기 방식

import zmq

'''SPEECH VENTILATOR : 5558'''
port = 5558

ctx = zmq.Context()

def run_ventilator() :
    sock = ctx.socket(zmq.PUSH)
    sock.bind(f'tcp://*:{port}')
    
    text = 'Speech MSG Test'
    file_path = 'Speech file path Test'
    
    for num in range(10) :
        msg = {'발화문' : text,
               '파일주소' : file_path}
        sock.send_json(msg)
        
    ctx.destroy()
    print("###DONE###")

if __name__ == '__main__' :
    run_ventilator()

