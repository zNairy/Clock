import time
import turtle as t
from turtle import *
h = 0;s = 0;m = 0;
while True:
     t.hideturtle();
     t.clear();
     t.write(('H:'+str(h)+'M:'+str(m)+'S:'+str(s)));
     time.sleep(1);
     s += 1
     if s == 60:
         m += 1;
         s -= 60;
     else:
         continue;
     if m == 60:
         h += 1;
         m -= 60;
     else:
         continue;

