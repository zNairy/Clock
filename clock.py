#!/usr/bin/env/python3
# coding: utf-8

__author__ = '__Nairy__'
__contact__ = 'https://www.github.com/zNairy/ or __Nairy__#7181 '
__version__ = ''

import sys
import time
import threading

class Clock(object):
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
        self._stopwatch = False

    def start(self):
        thread = threading.Thread(target=self.clock)
        thread.daemon = True
        thread.start()
        self.main()

    def main(self):
        while(self.minute < 1 and self._stopwatch == False):
            print(f'{self.second}s', end='\r')
            time.sleep(1)
        while(self.hour < 1 and self._stopwatch == False):
            print(f'{self.minute}M;{self.second}s', end='\r')
            time.sleep(1)
        while(self._stopwatch == False):
            print(f'{self.hour}H;{self.minute}M;{self.second}s', end='\r')
            time.sleep(1)

    def clock(self):
        while True is not False:
            time.sleep(1)
            if(self._stopwatch == False):
                self.second += 1
                if(self.second == 60):
                    self.minute += 1
                    self.second = 0
                if(self.minute == 60):
                    self.hour += 1
                    self.minute = 0
            else:
                break

    def stopwatch(self, h, m, s):
        def _start():
            while True is not False: 
                if(self.hour == h and self.minute == m and self.second == s):
                    self._stopwatch = True
        if(m < 60 and s < 60):
            thread = threading.Thread(target=_start)
            thread.daemon = True
            thread.start()
            self.start()
        else:
            print('Opção invalida')

def usage():
    print('Use os parâmetros --cronometro ou --clock\n --clock   > conta normalmente\n --cronometro (horas) (minutos) (segundos) ')

def main():
    if(len(sys.argv) == 1):
        usage()
    elif(sys.argv[1] == '--clock'):
        clock = Clock()
        clock.start()
    elif(sys.argv[1] == '--cronometro'):
        if(len(sys.argv) == 5):
            clock = Clock()
            clock.stopwatch(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
        else:
            print('Argumentos faltando, --cronometro (horas) (minutos) (segundos)')
                
if __name__ == '__main__':
    main()