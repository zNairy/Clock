#/usr/bin/env/python3
# coding: utf-8
__author__ = '__Nairy__'
__contact__ = 'https://www.github.com/zNairy/ or "__Nairy#7181" '
__version__ = '1.0.3'

import sys;
import time;

def usage():
    string = "    clock by: \033[31m__Nairy__\033[m    ";
    print(string.center(60));
    print('[\033[31mx\033[m] Use a opcao \033[31m--\033[m\033[32mc\033[m ou \033[31m--\033[m\033[32mcronometro\033[m para cronometrar um tempo. hora minutos segundos');
    print('Ex: python clock.py \033[31m--\033[m\033[32mc\033[m 10 20 30');
    print('[\033[34m*\033[m] Usando a opcao \033[31m--\033[m\033[31mclock\033[m, iniciara o contador normal.\n');

class Clock():
    def __init__(self):
        print('\033[31mClock\033[m'.center(50))
    def Cronometro(self, hours, minutes, seconds):
        if int(seconds) >= 60 or int(minutes) >= 60:
            print('Coloque numeros equivalentes...')
            sys.exit()
        hour = 0;minute = 0;second = 0; 
        while True:
            if int(hours) == hour and int(minutes) == minute and int(seconds) == second:
                print(str(second)+'s');    
                print('\033[31mbye...\033[m')
                sys.exit();
            print(str(second) + 's', end='\r')
            second += 1;time.sleep(1);
            if second == 60:
                minute += 1;second -= 60;
                while True:
                    if int(hours) == hour and int(minutes) == minute and int(seconds) == second:
                        print(str(minute)+'M;'+str(second)+'s', end='\r');
                        print('\033[32mbye...\033[m')
                        sys.exit();
                    print(str(minute)+'M;'+str(second)+'s', end='\r');
                    second += 1;time.sleep(1);
                    if second == 60:
                        minute += 1;second -= 60;
                    else:
                        continue;
                    if minute == 60:
                        hour += 1;minute -= 60;
                        while True:
                            if int(hours) == hour and int(minutes) == minute and int(seconds) == second:
                                print(str(hour)+'H;'+str(minute)+'M;'+str(second)+'s', end='\r');
                                print('\033[32mbye...\033[m')
                                sys.exit();
                            print(str(hour)+'H;'+str(minute)+'M;'+str(second)+'s', end='\r');
                            second += 1;time.sleep(1);
                            if second == 60:
                                minute += 1;second -= 60;
                            else:
                                continue;
                            if minute == 60:
                                hour += 1;minute -= 60;
                            else:
                                continue;

    def Clock(self):
        hour = 0;minute = 0;second = 0;
        while True:
            print(str(second)+'s', end='\r');
            second += 1;time.sleep(1);
            if second == 60:
                minute += 1;second -= 60;
                while True:
                    print(str(minute)+'M;'+str(second)+'s', end='\r');
                    second += 1;time.sleep(1);
                    if second == 60:
                        minute += 1;second -= 60;
                    else:
                        continue;
                    if minute == 60:
                        hour += 1;minute -= 60;
                        while True:
                            print(str(hour)+'H;'+str(minute)+'M;'+str(second)+'s', end='\r');
                            second += 1;time.sleep(1);
                            if second == 60:
                                minute += 1;second -= 60;
                            else:
                                continue;
                            if minute == 60:
                                hour += 1;minute -= 60;
                            else:
                                continue;


if __name__ == '__main__':
    if len(sys.argv) == 1:
        usage();
        sys.exit()
    else:
        if sys.argv[1] == '--cronometro' or sys.argv[1] == '--c':
            if len(sys.argv) == 5:
                try:
                    clock = Clock()
                    clock.Cronometro(sys.argv[2], sys.argv[3], sys.argv[4])
                except KeyboardInterrupt:
                    print('\n \033[32m[*] bye...\033[m')
                    sys.exit();
            else:
                print('\033[31m[x] Faltando argumentos...\033[m \n')
                usage();
                sys.exit()
        else:
            if sys.argv[1] == '--clock':
                try:
                    clock = Clock()
                    clock.Clock();
                except KeyboardInterrupt:
                    print("\n[x] See u later...");
                    sys.exit();
            else:
                print("[x] Faltando argumentos...");
                usage();
