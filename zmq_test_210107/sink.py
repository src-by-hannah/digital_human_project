# -*- coding: utf-8 -*-
"""
Pyzmq test
- PULL / PUSH 방법
- 싱크 (result collector)

Last Updated : 2021.01.07.

@author: Hannah_Noh
"""

## 동기 방식

import zmq

'''UNREAL SINK : 5556'''
port = 5556

ctx = zmq.Context()

def run_sink():
    sock = ctx.socket(zmq.PULL)
    sock.bind(f'tcp://*:{port}')
    
    for x in range(10) :
        result = sock.recv_json()
        
        print("[Result]")
        print(result)
        
    ctx.destroy()
    print("###DONE###")
    

if __name__ == '__main__':
    run_sink()